#!/usr/bin/env python3
"""
iPhone, iPad & Mac Screenshot Resizer
Resizes images to fit various iPhone, iPad, and Mac display resolutions for App Store submissions.
"""

import os
import sys
from PIL import Image
import inquirer


# Define iPhone resolutions with both portrait and landscape orientations
IPHONE_RESOLUTIONS = {
    "iPhone 6.5\" - Portrait (1242 × 2688)": (1242, 2688),
    "iPhone 6.5\" - Landscape (2688 × 1242)": (2688, 1242),
    "iPhone 6.7\" - Portrait (1284 × 2778)": (1284, 2778),
    "iPhone 6.7\" - Landscape (2778 × 1284)": (2778, 1284),
    "iPhone 6.9\" - Portrait (1320 × 2868)": (1320, 2868),
    "iPhone 6.9\" - Landscape (2868 × 1320)": (2868, 1320),
    "iPhone 5.5\" - Portrait (1242 × 2208)": (1242, 2208),
    "iPhone 5.5\" - Landscape (2208 × 1242)": (2208, 1242),
}

# Define iPad resolutions with both portrait and landscape orientations
IPAD_RESOLUTIONS = {
    "iPad Pro 13\" - Portrait (2064 × 2752)": (2064, 2752),
    "iPad Pro 13\" - Landscape (2752 × 2064)": (2752, 2064),
    "iPad Pro 12.9\" - Portrait (2048 × 2732)": (2048, 2732),
    "iPad Pro 12.9\" - Landscape (2732 × 2048)": (2732, 2048),
    "iPad Pro 11\" - Portrait (1668 × 2388)": (1668, 2388),
    "iPad Pro 11\" - Landscape (2388 × 1668)": (2388, 1668),
    "iPad 10.9\" - Portrait (1640 × 2360)": (1640, 2360),
    "iPad 10.9\" - Landscape (2360 × 1640)": (2360, 1640),
}

# Define Mac resolutions for macOS App Store screenshots
MAC_RESOLUTIONS = {
    "Mac 27\" 5K iMac (5120 × 2880)": (5120, 2880),
    "Mac 24\" 4.5K iMac (4480 × 2520)": (4480, 2520),
    "Mac 16\" MacBook Pro Retina (3456 × 2234)": (3456, 2234),
    "Mac 15\" MacBook Pro Retina (2880 × 1800)": (2880, 1800),
    "Mac 14\" MacBook Pro Retina (3024 × 1964)": (3024, 1964),
    "Mac 13\" MacBook Retina (2560 × 1600)": (2560, 1600),
    "Mac Standard HD (1440 × 900)": (1440, 900),
    "Mac Minimum (1280 × 800)": (1280, 800),
}


def get_image_files(folder_path):
    """Get all image files from the specified folder."""
    supported_formats = ('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG')
    image_files = []
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(supported_formats):
            image_files.append(os.path.join(folder_path, filename))
    
    return image_files


def resize_image(image_path, target_size, output_folder, resolution_name):
    """
    Resize an image to fit the target resolution.
    Uses LANCZOS resampling for high-quality results.
    """
    try:
        with Image.open(image_path) as img:
            # Get original dimensions
            original_width, original_height = img.size
            target_width, target_height = target_size
            
            # Calculate aspect ratios
            original_ratio = original_width / original_height
            target_ratio = target_width / target_height
            
            # Determine if we should fit or cover
            # Fit: image fits entirely within target dimensions (may have padding)
            # Cover: image covers entire target dimensions (may crop)
            
            # Using 'contain' approach - resize to fit within bounds, maintaining aspect ratio
            if original_ratio > target_ratio:
                # Image is wider than target
                new_width = target_width
                new_height = int(target_width / original_ratio)
            else:
                # Image is taller than target
                new_height = target_height
                new_width = int(target_height * original_ratio)
            
            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Create a new image with the target size and paste the resized image
            # Using white background
            final_img = Image.new('RGB', target_size, (255, 255, 255))
            
            # Calculate position to center the resized image
            x_offset = (target_width - new_width) // 2
            y_offset = (target_height - new_height) // 2
            
            # Paste the resized image onto the background
            if resized_img.mode == 'RGBA':
                final_img.paste(resized_img, (x_offset, y_offset), resized_img)
            else:
                final_img.paste(resized_img, (x_offset, y_offset))
            
            # Save the final image
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            output_filename = f"{base_name}_{target_width}x{target_height}.png"
            output_path = os.path.join(output_folder, output_filename)
            
            final_img.save(output_path, 'PNG', quality=100)
            print(f"  ✓ Created: {output_filename}")
            
    except Exception as e:
        print(f"  ✗ Error processing {os.path.basename(image_path)}: {str(e)}")


def main():
    """Main function to run the screenshot resizer."""
    print("=" * 60)
    print("iPhone, iPad & Mac Screenshot Resizer".center(60))
    print("=" * 60)
    print()
    
    # Get input folder
    input_folder = input("Enter the path to the folder containing screenshots: ").strip()
    
    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a valid directory.")
        sys.exit(1)
    
    # Get image files
    image_files = get_image_files(input_folder)
    
    if not image_files:
        print(f"No image files found in '{input_folder}'")
        sys.exit(1)
    
    print(f"\nFound {len(image_files)} image(s) to process.")
    print()
    
    # Prompt user to select device type
    device_questions = [
        inquirer.Checkbox(
            'device_types',
            message="Select device types (use spacebar to select, enter to confirm)",
            choices=['iPhone', 'iPad', 'Mac'],
            default=['iPhone'],
        ),
    ]
    
    device_answers = inquirer.prompt(device_questions)
    
    if not device_answers or not device_answers['device_types']:
        print("No device types selected. Exiting.")
        sys.exit(0)
    
    # Combine resolutions based on selected device types
    available_resolutions = {}
    if 'iPhone' in device_answers['device_types']:
        available_resolutions.update(IPHONE_RESOLUTIONS)
    if 'iPad' in device_answers['device_types']:
        available_resolutions.update(IPAD_RESOLUTIONS)
    if 'Mac' in device_answers['device_types']:
        available_resolutions.update(MAC_RESOLUTIONS)
    
    # Prompt user to select resolutions using checkboxes
    resolution_questions = [
        inquirer.Checkbox(
            'resolutions',
            message="Select resolutions (use spacebar to select, enter to confirm)",
            choices=list(available_resolutions.keys()),
        ),
    ]
    
    answers = inquirer.prompt(resolution_questions)
    
    if not answers or not answers['resolutions']:
        print("No resolutions selected. Exiting.")
        sys.exit(0)
    
    selected_resolutions = answers['resolutions']
    
    # Create output folder
    output_folder = os.path.join(input_folder, "resized_screenshots")
    os.makedirs(output_folder, exist_ok=True)
    
    print(f"\nOutput folder: {output_folder}")
    print()
    
    # Process each image for each selected resolution
    total_images = len(image_files) * len(selected_resolutions)
    current = 0
    
    for resolution_name in selected_resolutions:
        target_size = available_resolutions[resolution_name]
        print(f"Processing for {resolution_name}...")
        
        for image_path in image_files:
            current += 1
            resize_image(image_path, target_size, output_folder, resolution_name)
    
    print()
    print("=" * 60)
    print(f"✓ Successfully processed {len(image_files)} image(s)")
    print(f"✓ Created {total_images} resized screenshot(s)")
    print(f"✓ Output location: {output_folder}")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)

