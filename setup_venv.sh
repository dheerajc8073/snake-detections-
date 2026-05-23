#!/bin/bash

# =========================================================
# 🐍 SNAKE DETECTION SYSTEM - VIRTUAL ENVIRONMENT SETUP
# =========================================================
# This script sets up a complete virtual environment
# for the AI-powered Snake Detection System
# =========================================================

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║   🐍 SNAKE DETECTION SYSTEM - SETUP WIZARD 🐍     ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
echo "🔍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python $PYTHON_VERSION detected"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment 'venv' already exists"
    read -p "Do you want to recreate it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf venv
        python3 -m venv venv
        echo "✅ Virtual environment recreated"
    else
        echo "⏭️  Skipping virtual environment creation"
    fi
else
    python3 -m venv venv
    echo "✅ Virtual environment created successfully"
fi
echo ""

# Activate virtual environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "📥 Upgrading pip..."
pip install --upgrade pip wheel setuptools
echo "✅ pip upgraded successfully"
echo ""

# Install requirements
echo "📚 Installing dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ All dependencies installed successfully"
else
    echo "❌ requirements.txt not found!"
    exit 1
fi
echo ""

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p detections
mkdir -p logs
mkdir -p models
echo "✅ Directories created"
echo ""

# Setup environment file
echo "⚙️  Setting up environment configuration..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "✅ .env file created from .env.example"
        echo "⚠️  Please edit .env and add your actual configuration values"
    fi
else
    echo "✅ .env file already exists"
fi
echo ""

# Display summary
echo "╔════════════════════════════════════════════════════╗"
echo "║            ✅ SETUP COMPLETED SUCCESSFULLY         ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "📋 Next Steps:"
echo "   1. Edit .env file with your configuration:"
echo "      - TELEGRAM_BOT_TOKEN"
echo "      - TELEGRAM_CHAT_ID"
echo "      - EMERGENCY_CONTACT"
echo "      - LOCATION"
echo ""
echo "   2. Activate virtual environment (if not already):"
echo "      source venv/bin/activate"
echo ""
echo "   3. Run the snake detection system:"
echo "      python snake_detector.py"
echo ""
echo "   4. Press 'q' to quit the application"
echo ""
echo "🐍 Happy Snake Detecting! 🐍"
echo ""
