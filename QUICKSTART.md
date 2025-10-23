# Quick Start Guide

Get started with the iPhone Screenshot Resizer in 3 simple steps!

## 🚀 Quick Start

### 1. Run the Script
```bash
cd ~/projects/image-resolution
./run.sh
```

The script will automatically:
- Create a virtual environment (if needed)
- Install all dependencies (if needed)
- Start the resizer tool

### 2. Select Your Screenshots
When prompted, enter the path to your screenshots folder:
```
Enter the path to the folder containing screenshots: /path/to/your/screenshots
```

**Tip**: You can drag and drop the folder into the terminal to auto-fill the path!

### 3. Choose Resolutions
Use your keyboard to select the iPhone resolutions you need:
- `↑/↓` arrows to navigate
- `SPACE` to select/unselect
- `ENTER` to confirm

```
? Select iPhone resolutions (use spacebar to select, enter to confirm)
 ❯ ◉ iPhone 6.5" - Portrait (1242 × 2688)
   ◉ iPhone 6.7" - Portrait (1284 × 2778)
   ◯ iPhone 6.5" - Landscape (2688 × 1242)
   ◯ iPhone 6.7" - Landscape (2778 × 1284)
```

### 4. Done! ✅
Your resized screenshots will be in:
```
/path/to/your/screenshots/resized_screenshots/
```

## 📱 Common Use Cases

### App Store Submission (Portrait Only)
Select these resolutions:
- iPhone 6.5" - Portrait (1242 × 2688)
- iPhone 6.7" - Portrait (1284 × 2778)

### App Store Submission (With Landscape)
Select these resolutions:
- iPhone 6.5" - Portrait (1242 × 2688)
- iPhone 6.5" - Landscape (2688 × 1242)
- iPhone 6.7" - Portrait (1284 × 2778)
- iPhone 6.7" - Landscape (2778 × 1284)

### Legacy Support
Also include:
- iPhone 5.5" - Portrait (1242 × 2208)
- iPhone 5.5" - Landscape (2208 × 1242)

## 🆘 Need Help?

### "Permission denied" error
```bash
chmod +x run.sh
```

### Start fresh
```bash
rm -rf venv/
./run.sh
```

### Check what's installed
```bash
source venv/bin/activate
pip list
deactivate
```

## 💡 Pro Tips

1. **High-Quality Sources**: Use screenshots larger than your target resolution for best results
2. **Batch Processing**: Put all your screenshots in one folder and process them all at once
3. **Naming Convention**: Output files include dimensions in the filename for easy identification
4. **White Background**: Padding uses white background by default - perfect for App Store

## 📖 More Information

For detailed documentation, see [README.md](README.md)

