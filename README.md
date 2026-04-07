# iPhone, iPad & Mac Screenshot Resizer 🇵🇸

A Python CLI tool that automatically resizes screenshots to fit various iPhone, iPad, and Mac display resolutions for App Store submissions.

## Features

- 📱 Support for multiple iPhone screen sizes (5.5", 6.5", 6.7", 6.9")
- 📱 Support for multiple iPad screen sizes (10.9", 11", 12.9", 13")
- 💻 Support for Mac displays (iMac, MacBook Pro, MacBook Air)
- ✅ Interactive checkbox selection for device types and target resolutions
- 🖼️ Batch processing of multiple images
- 🎨 High-quality image resizing with LANCZOS algorithm
- 📐 Maintains aspect ratio with smart padding
- 🚀 Simple command-line interface

## Supported Resolutions

### iPhone Resolutions

| Display Size | Orientation | Resolution | Devices |
|--------------|-------------|------------|---------|
| 6.5" | Portrait | 1242 × 2688px | iPhone 11 Pro Max, XS Max |
| 6.5" | Landscape | 2688 × 1242px | iPhone 11 Pro Max, XS Max |
| 6.7" | Portrait | 1284 × 2778px | iPhone 12/13/14 Pro Max |
| 6.7" | Landscape | 2778 × 1284px | iPhone 12/13/14 Pro Max |
| 6.9" | Portrait | 1320 × 2868px | iPhone 15/16 Pro Max |
| 6.9" | Landscape | 2868 × 1320px | iPhone 15/16 Pro Max |
| 5.5" | Portrait | 1242 × 2208px | iPhone 6s Plus, 7 Plus, 8 Plus |
| 5.5" | Landscape | 2208 × 1242px | iPhone 6s Plus, 7 Plus, 8 Plus |

### iPad Resolutions

| Display Size | Orientation | Resolution | Devices |
|--------------|-------------|------------|---------|
| 13" | Portrait | 2064 × 2752px | iPad Pro 13" (M4, 2024) |
| 13" | Landscape | 2752 × 2064px | iPad Pro 13" (M4, 2024) |
| 12.9" | Portrait | 2048 × 2732px | iPad Pro 12.9" (all generations) |
| 12.9" | Landscape | 2732 × 2048px | iPad Pro 12.9" (all generations) |
| 11" | Portrait | 1668 × 2388px | iPad Pro 11", iPad Air (4th & 5th gen) |
| 11" | Landscape | 2388 × 1668px | iPad Pro 11", iPad Air (4th & 5th gen) |
| 10.9" | Portrait | 1640 × 2360px | iPad Air (10th gen), iPad (10th gen) |
| 10.9" | Landscape | 2360 × 1640px | iPad Air (10th gen), iPad (10th gen) |

### Mac Resolutions

| Display Type | Resolution | Devices |
|--------------|------------|---------|
| 27" 5K iMac | 5120 × 2880px | iMac 27" 5K Retina |
| 24" 4.5K iMac | 4480 × 2520px | iMac 24" 4.5K (M1, M3) |
| 16" MacBook Pro | 3456 × 2234px | MacBook Pro 16" (M1/M2/M3 Pro/Max) |
| 15" MacBook Pro | 2880 × 1800px | MacBook Pro 15" Retina |
| 14" MacBook Pro | 3024 × 1964px | MacBook Pro 14" (M1/M2/M3 Pro/Max) |
| 13" MacBook | 2560 × 1600px | MacBook Pro 13", MacBook Air 13" Retina |
| Standard HD | 1440 × 900px | Standard resolution displays |
| Minimum | 1280 × 800px | Minimum App Store requirement |

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download this project**
   ```bash
   cd ~/projects/image-resolution
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Using the Bash Script (macOS/Linux)

The easiest way to run the tool:

```bash
./run.sh
```

### Manual Usage

```bash
python3 resize_screenshots.py
```

### Step-by-Step Process

1. Run the script using one of the methods above
2. Enter the path to your folder containing screenshots
3. Use the arrow keys to navigate the resolution list
4. Press `spacebar` to select/deselect resolutions
5. Press `Enter` to confirm your selection
6. The tool will process all images and save them to a `resized_screenshots` folder

### Example

```
iPhone, iPad & Mac Screenshot Resizer
============================================================

Enter the path to the folder containing screenshots: /path/to/screenshots

Found 3 image(s) to process.

? Select device types (use spacebar to select, enter to confirm)
 ❯ ◉ iPhone
   ◉ iPad
   ◉ Mac

? Select resolutions (use spacebar to select, enter to confirm)
 ❯ ◉ iPhone 6.5" - Portrait (1242 × 2688)
   ⬢ iPhone 6.5" - Landscape (2688 × 1242)
   ◉ iPad Pro 12.9" - Portrait (2048 × 2732)
   ⬢ iPad Pro 12.9" - Landscape (2732 × 2048)
   ◉ Mac 27" 5K iMac (5120 × 2880)

Processing for iPhone 6.5" - Portrait (1242 × 2688)...
  ✓ Created: screenshot1_1242x2688.png
  ✓ Created: screenshot2_1242x2688.png
  ✓ Created: screenshot3_1242x2688.png

Processing for iPad Pro 12.9" - Portrait (2048 × 2732)...
  ✓ Created: screenshot1_2048x2732.png
  ✓ Created: screenshot2_2048x2732.png
  ✓ Created: screenshot3_2048x2732.png

============================================================
✓ Successfully processed 3 image(s)
✓ Created 6 resized screenshot(s)
✓ Output location: /path/to/screenshots/resized_screenshots
============================================================
```

## How It Works

1. **Image Detection**: Scans the input folder for PNG, JPG, and JPEG files
2. **Device Selection**: Choose between iPhone, iPad, and/or Mac device types
3. **Resolution Selection**: Presents an interactive checkbox menu to select target resolutions for chosen device types
4. **Smart Resizing**: 
   - Maintains the original aspect ratio
   - Adds white padding if needed to fit exact dimensions
   - Uses high-quality LANCZOS resampling
5. **Output**: Saves resized images with descriptive filenames in a dedicated output folder

## Output File Naming

Resized images are named with the following pattern:
```
{original_filename}_{width}x{height}.png
```

Example: `app_screenshot_1242x2688.png`

## Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)

All output images are saved as PNG for maximum quality.

## Troubleshooting

### "No image files found"
- Ensure your folder contains PNG or JPEG files
- Check that file extensions are correct (.png, .jpg, .jpeg)

### "Module not found" error
- Activate your virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### "Permission denied"
- Make the bash script executable: `chmod +x run.sh`

## Tips for Best Results

1. **Use high-resolution source images**: Start with images that are at least as large as your target resolution
2. **Maintain aspect ratio**: Source images with similar aspect ratios to target resolutions will have less padding
3. **Check output**: Always review the resized images before uploading to App Store Connect

## License

MIT License - feel free to use this tool for any purpose.

## Contributing

Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## Author

Created for easy iPhone, iPad, and Mac screenshot management for App Store submissions.

