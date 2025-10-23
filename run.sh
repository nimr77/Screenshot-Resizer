#!/bin/bash

# iPhone Screenshot Resizer - Run Script
# This script handles the setup and execution of the screenshot resizer tool

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================"
echo "iPhone Screenshot Resizer"
echo "================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if ! python3 -c "import PIL" 2>/dev/null || ! python3 -c "import inquirer" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
    echo ""
fi

# Run the main script
echo "Starting screenshot resizer..."
echo ""
python3 resize_screenshots.py

# Deactivate virtual environment
deactivate

echo ""
echo "Done! Virtual environment deactivated."

