#!/bin/bash
# Smart Resume Analyzer - Linux/Mac Startup Script

echo ""
echo "====================================="
echo "Smart Resume Analyzer"
echo "====================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"

# Create uploads folder if not exists
mkdir -p uploads

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
source venv/bin/activate
echo "✓ Virtual environment activated"

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -q -r requirements.txt
    echo "✓ Dependencies installed"
else
    echo "WARNING: requirements.txt not found"
fi

echo ""
echo "✓ Starting Smart Resume Analyzer..."
echo ""
echo "🌐 Open your browser and go to: http://localhost:5000"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

python app.py
