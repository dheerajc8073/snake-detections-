```markdown
# 🐍 AI Snake Detection System - Complete Setup Guide

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Quick Setup](#quick-setup)
3. [Detailed Setup Instructions](#detailed-setup-instructions)
4. [Configuration Guide](#configuration-guide)
5. [Troubleshooting](#troubleshooting)
6. [Project Structure](#project-structure)

---

## 🖥️ System Requirements

### Minimum Requirements
- **Python Version**: 3.8 or higher
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: 8GB minimum (16GB recommended)
- **GPU**: NVIDIA GPU recommended for faster inference (CUDA 11.8+)
- **Storage**: 5GB free space (for model and dependencies)

### Required Hardware
- **Webcam**: USB webcam or built-in camera
- **Microphone**: For voice alerts (optional)
- **Speaker**: For sound alerts

### Software Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git (optional, for cloning repository)

---

## ⚡ Quick Setup

### 🪟 Windows Setup (Easiest)

1. **Double-click the setup script:**
   ```
   setup_venv.bat
   ```
   The wizard will automatically:
   - Check Python installation
   - Create virtual environment
   - Install all dependencies
   - Create necessary directories
   - Setup configuration file

2. **Edit configuration:**
   ```
   .env
   ```
   Add your Telegram credentials and emergency contact

3. **Run the system:**
   ```
   venv\Scripts\activate.bat
   python snake_detector.py
   ```

### 🐧 Linux/macOS Setup

1. **Make script executable:**
   ```bash
   chmod +x setup_venv.sh
   ```

2. **Run the setup script:**
   ```bash
   ./setup_venv.sh
   ```

3. **Edit configuration:**
   ```bash
   nano .env
   ```

4. **Run the system:**
   ```bash
   source venv/bin/activate
   python snake_detector.py
   ```

---

## 📖 Detailed Setup Instructions

### Step 1️⃣: Verify Python Installation

**Windows:**
```cmd
python --version
python -m pip --version
```

**Linux/macOS:**
```bash
python3 --version
python3 -m pip --version
```

Expected output: Python 3.8+ and pip 21.0+

### Step 2️⃣: Create Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 3️⃣: Upgrade pip

```bash
pip install --upgrade pip wheel setuptools
```

### Step 4️⃣: Install Dependencies

```bash
pip install -r requirements.txt
```

**Installation will include:**
- 🎯 **YOLOv8**: For snake detection
- 📹 **OpenCV**: For video processing
- 🌐 **FastAPI**: For web API
- 💬 **Telegram Bot**: For notifications
- 🔊 **pyttsx3**: For voice alerts
- 🔢 **NumPy/PyTorch**: For ML operations

### Step 5️⃣: Create Required Directories

```bash
mkdir detections
mkdir logs
mkdir models
```

### Step 6️⃣: Configure Environment Variables

```bash
# Copy example file
cp .env.example .env

# Edit the file with your actual values
# Windows: notepad .env
# Linux/macOS: nano .env
```

---

## ⚙️ Configuration Guide

### 🤖 Telegram Setup

1. **Get Bot Token:**
   - Open Telegram and search for `@BotFather`
   - Send `/start` command
   - Send `/newbot` command
   - Follow instructions and copy the bot token
   - Keep it secret! ⚠️

2. **Get Chat ID:**
   - Search for `@userinfobot` on Telegram
   - Send any message
   - Copy the Chat ID

3. **Update .env file:**
   ```
   TELEGRAM_BOT_TOKEN=your_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   ```

### 🎯 Detection Settings

```
# Confidence threshold (0.0-1.0)
# Higher = more accurate but fewer detections
CONF_THRESHOLD=0.80

# Alert cooldown in seconds
# Prevents alert spam
ALERT_COOLDOWN=120

# Camera resolution
CAMERA_WIDTH=1280
CAMERA_HEIGHT=720

# Camera index (0 for default)
CAMERA_INDEX=0
```

### 🚨 Alert Settings

```
# Enable/disable different alerts
ENABLE_VOICE_ALERT=true
ENABLE_SOUND_ALERT=true
ENABLE_TELEGRAM_ALERT=true
ENABLE_TELEGRAM_PHOTO=true

# Voice properties
VOICE_SPEED=150
VOICE_VOLUME=1.0
```

### 📍 Emergency Details

```
EMERGENCY_CONTACT=+91XXXXXXXXXX
LOCATION=Your Location Name
```

---

## 🐛 Troubleshooting

### ❌ "Python not found" Error

**Windows:**
```cmd
# Add Python to PATH
setx PATH "%PATH%;C:\Users\YourUsername\AppData\Local\Programs\Python\Python311"
```

**Linux/macOS:**
```bash
# Install Python using package manager
sudo apt-get install python3.11 python3.11-venv  # Ubuntu/Debian
brew install python3                              # macOS
```

### ❌ "No module named 'cv2'" Error

```bash
# Reinstall OpenCV
pip uninstall opencv-python
pip install opencv-python==4.8.1.78
```

### ❌ Camera Not Detected

```bash
# Check camera index
python -c "import cv2; cap = cv2.VideoCapture(0); print(cap.isOpened())"

# Try different camera index in .env
CAMERA_INDEX=1  # or 2, 3, etc.
```

### ❌ Telegram Not Sending Messages

1. **Check internet connection**
2. **Verify bot token:**
   ```bash
   # Test bot token validity
   curl "https://api.telegram.org/botYOUR_TOKEN/getMe"
   ```
3. **Verify chat ID is correct**
4. **Check firewall settings**

### ❌ Low GPU Performance

```bash
# Install CUDA support (NVIDIA GPUs only)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### ❌ Model Download Issues

```bash
# Manually download model
python -c "from ultralytics import YOLO; YOLO('yolov8s.pt')"

# Copy to project
cp ~/.config/Ultralytics/models/snake_model.pt ./
```

---

## 📁 Project Structure

```
snake-detections/
│
├── 📄 snake_detector.py          # Main detection script
├── 🤖 snake_model.pt             # YOLO model (22.5 MB)
├── 📦 requirements.txt            # Python dependencies
├── 🔑 .env                        # Configuration (git ignored)
├── 📋 .env.example               # Configuration template
│
├── 🛠️ Setup Scripts
│   ├── setup_venv.sh             # Linux/macOS setup
│   ├── setup_venv.bat            # Windows setup
│   └── SETUP_GUIDE.md            # This file
│
├── 📚 Documentation
│   ├── README.md                 # Project overview
│   └── ARCHITECTURE.md           # System architecture
│
├── 📁 detections/                # Saved detection images
│   └── snake_YYYYMMDD_HHMMSS.jpg
│
├── 📁 logs/                      # System logs
│   └── system.log
│
├── 📁 models/                    # Additional models
│   └── (custom models here)
│
└── 📁 venv/                      # Virtual environment
    ├── bin/ or Scripts/
    ├── lib/
    └── pyvenv.cfg
```

---

## 🚀 Running the System

### First Time Run

```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate.bat

# Linux/macOS:
source venv/bin/activate

# Run the detector
python snake_detector.py
```

### Expected Output

```
======================================================================
🐍 AI SNAKE EMERGENCY SYSTEM STARTED
======================================================================
✅ Snake Detection Enabled
✅ Telegram Alerts Enabled
✅ Voice Warning Enabled
✅ Alarm Enabled

🟢 Monitoring... No Snake Detected
[System waits for snake detection...]
```

### During Detection

```
======================================================================
SNAKE ALERT
======================================================================

🐍 SNAKE DETECTED

⚠️ Risk Level: HIGH RISK

🎯 Confidence: 95%

📌 Safety Instructions:
• Stay away from snake
• Do not attempt handling
• Alert nearby people
• Contact wildlife rescue
• Maintain safe distance

======================================================================
✅ Image Saved: detections/snake_20260523_104530.jpg
✅ Telegram Message Sent
✅ Telegram Photo Sent
```

### Stopping the System

Press `q` key to gracefully exit the application.

---

## 🔐 Security Best Practices

1. **Never commit .env file**
   ```bash
   # Already in .gitignore
   echo ".env" >> .gitignore
   ```

2. **Use environment variables in production**
   ```bash
   export TELEGRAM_BOT_TOKEN="your_token"
   ```

3. **Rotate bot token if compromised**
   - Go to @BotFather
   - Select your bot
   - Click /revoke_token

4. **Use strong passwords**
   - Keep emergency contact secure
   - Restrict access to logs

---

## 📞 Support & Help

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Camera lag | Reduce CAMERA_WIDTH/HEIGHT |
| High false positives | Increase CONF_THRESHOLD |
| Missed detections | Decrease CONF_THRESHOLD |
| Telegram timeout | Check internet, verify token |
| Memory issues | Close other applications |

### Getting More Help

- 📖 Check `README.md` for overview
- 🔍 Search GitHub issues
- 💬 Create GitHub issue with details
- 📧 Contact project maintainer

---

## 📊 Performance Tips

1. **Optimize for speed:**
   ```
   CONF_THRESHOLD=0.85  # Higher threshold = faster
   CAMERA_WIDTH=640
   CAMERA_HEIGHT=480
   ```

2. **GPU Acceleration:**
   - Install NVIDIA CUDA
   - Install cuDNN
   - PyTorch will auto-detect and use GPU

3. **Reduce Alert Spam:**
   ```
   ALERT_COOLDOWN=300  # 5 minutes
   ```

---

## ✅ Verification Checklist

After setup, verify:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (pip list)
- [ ] .env file configured with valid credentials
- [ ] Directories created (detections, logs, models)
- [ ] Camera accessible (cv2.VideoCapture works)
- [ ] Telegram bot token valid
- [ ] Model file present (snake_model.pt)
- [ ] No errors in terminal output
- [ ] System runs without crashes

---

## 🎓 Additional Resources

### YOLOv8 Documentation
- https://docs.ultralytics.com/

### FastAPI
- https://fastapi.tiangolo.com/

### OpenCV
- https://docs.opencv.org/

### Telegram Bot API
- https://core.telegram.org/bots/api

---

**🐍 Happy Snake Detecting! Stay Safe! 🐍**

Last Updated: 2026-05-23
Version: 1.0.0
```
