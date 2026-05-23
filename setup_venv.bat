@echo off
REM =========================================================
REM 🐍 SNAKE DETECTION SYSTEM - VIRTUAL ENVIRONMENT SETUP
REM =========================================================
REM This batch script sets up a complete virtual environment
REM for the AI-powered Snake Detection System on Windows
REM =========================================================

setlocal enabledelayedexpansion

cls
echo.
echo ╔════════════════════════════════════════════════════╗
echo ║   🐍 SNAKE DETECTION SYSTEM - SETUP WIZARD 🐍     ║
echo ╚════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
echo 🔍 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH.
    echo    Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% detected
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
if exist venv (
    echo ⚠️  Virtual environment 'venv' already exists
    set /p recreate="Do you want to recreate it? (y/n): "
    if /i "!recreate!"=="y" (
        rmdir /s /q venv
        python -m venv venv
        echo ✅ Virtual environment recreated
    ) else (
        echo ⏭️  Skipping virtual environment creation
    )
) else (
    python -m venv venv
    echo ✅ Virtual environment created successfully
)
echo.

REM Activate virtual environment
echo 🚀 Activating virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo.

REM Upgrade pip
echo 📥 Upgrading pip...
python -m pip install --upgrade pip wheel setuptools
echo ✅ pip upgraded successfully
echo.

REM Install requirements
echo 📚 Installing dependencies from requirements.txt...
if exist requirements.txt (
    pip install -r requirements.txt
    echo ✅ All dependencies installed successfully
) else (
    echo ❌ requirements.txt not found!
    pause
    exit /b 1
)
echo.

REM Create necessary directories
echo 📁 Creating necessary directories...
if not exist detections mkdir detections
if not exist logs mkdir logs
if not exist models mkdir models
echo ✅ Directories created
echo.

REM Setup environment file
echo ⚙️  Setting up environment configuration...
if not exist .env (
    if exist .env.example (
        copy .env.example .env
        echo ✅ .env file created from .env.example
        echo ⚠️  Please edit .env and add your actual configuration values
    )
) else (
    echo ✅ .env file already exists
)
echo.

REM Display summary
cls
echo.
echo ╔════════════════════════════════════════════════════╗
echo ║            ✅ SETUP COMPLETED SUCCESSFULLY         ║
echo ╚════════════════════════════════════════════════════╝
echo.
echo 📋 Next Steps:
echo    1. Edit .env file with your configuration:
echo       - TELEGRAM_BOT_TOKEN
echo       - TELEGRAM_CHAT_ID
echo       - EMERGENCY_CONTACT
echo       - LOCATION
echo.
echo    2. Activate virtual environment (if not already):
echo       venv\Scripts\activate.bat
echo.
echo    3. Run the snake detection system:
echo       python snake_detector.py
echo.
echo    4. Press 'q' to quit the application
echo.
echo 🐍 Happy Snake Detecting! 🐍
echo.
pause
