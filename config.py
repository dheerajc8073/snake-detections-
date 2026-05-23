"""
🐍 Configuration Module for Snake Detection System

This module handles all configuration management using environment variables.
It provides a clean interface for accessing system settings.

Author: AI Snake Detection Team
Version: 1.0.0
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# =========================================================
# PROJECT CONFIGURATION
# =========================================================

PROJECT_NAME = "AI Snake Detection System"
PROJECT_VERSION = "1.0.0"
PROJECT_DESCRIPTION = "Real-time snake detection using YOLOv8"

# =========================================================
# TELEGRAM CONFIGURATION
# =========================================================

TELEGRAM_BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN",
    ""
)
"""Telegram Bot Token from @BotFather"""

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID",
    ""
)
"""Your Telegram Chat ID"""

TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
"""Telegram API Base URL"""

# =========================================================
# EMERGENCY CONFIGURATION
# =========================================================

EMERGENCY_CONTACT = os.getenv(
    "EMERGENCY_CONTACT",
    "911"
)
"""Emergency Contact Number"""

LOCATION = os.getenv(
    "LOCATION",
    "Unknown Location"
)
"""Location/Area Name"""

# =========================================================
# DETECTION CONFIGURATION
# =========================================================

CONF_THRESHOLD = float(os.getenv(
    "CONF_THRESHOLD",
    "0.80"
))
"""Confidence Threshold (0.0 - 1.0)
Higher values = more accurate but fewer detections
"""

ALERT_COOLDOWN = int(os.getenv(
    "ALERT_COOLDOWN",
    "120"
))
"""Alert Cooldown in Seconds
Prevents alert spam for same detection
"""

# =========================================================
# CAMERA CONFIGURATION
# =========================================================

CAMERA_WIDTH = int(os.getenv(
    "CAMERA_WIDTH",
    "1280"
))
"""Camera Frame Width in Pixels"""

CAMERA_HEIGHT = int(os.getenv(
    "CAMERA_HEIGHT",
    "720"
))
"""Camera Frame Height in Pixels"""

CAMERA_INDEX = int(os.getenv(
    "CAMERA_INDEX",
    "0"
))
"""Camera Index (0 = default webcam)"""

# =========================================================
# MODEL CONFIGURATION
# =========================================================

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "./snake_model.pt"
)
"""Path to YOLOv8 Model File"""

# =========================================================
# OUTPUT & STORAGE CONFIGURATION
# =========================================================

DETECTIONS_FOLDER = os.getenv(
    "DETECTIONS_FOLDER",
    "detections"
)
"""Folder to Save Detection Images"""

SAVE_DETECTIONS = os.getenv(
    "SAVE_DETECTIONS",
    "true"
).lower() == "true"
"""Whether to Save Detection Images"""

LOGS_FOLDER = os.getenv(
    "LOGS_FOLDER",
    "logs"
)
"""Folder for System Logs"""

# =========================================================
# ALERT CONFIGURATION
# =========================================================

ENABLE_VOICE_ALERT = os.getenv(
    "ENABLE_VOICE_ALERT",
    "true"
).lower() == "true"
"""Enable Voice Alerts"""

ENABLE_SOUND_ALERT = os.getenv(
    "ENABLE_SOUND_ALERT",
    "true"
).lower() == "true"
"""Enable Sound/Beep Alerts"""

ENABLE_TELEGRAM_ALERT = os.getenv(
    "ENABLE_TELEGRAM_ALERT",
    "true"
).lower() == "true"
"""Enable Telegram Message Alerts"""

ENABLE_TELEGRAM_PHOTO = os.getenv(
    "ENABLE_TELEGRAM_PHOTO",
    "true"
).lower() == "true"
"""Enable Telegram Photo Alerts"""

# =========================================================
# VOICE CONFIGURATION
# =========================================================

VOICE_SPEED = int(os.getenv(
    "VOICE_SPEED",
    "150"
))
"""Voice Speed (words per minute)"""

VOICE_VOLUME = float(os.getenv(
    "VOICE_VOLUME",
    "1.0"
))
"""Voice Volume (0.0 - 1.0)"""

# =========================================================
# DEBUG & LOGGING CONFIGURATION
# =========================================================

DEBUG = os.getenv(
    "DEBUG",
    "false"
).lower() == "true"
"""Debug Mode (verbose output)"""

VERBOSE = os.getenv(
    "VERBOSE",
    "false"
).lower() == "true"
"""Verbose Logging"""

# =========================================================
# UTILITY FUNCTIONS
# =========================================================


def create_directories():
    """Create necessary directories if they don't exist."""
    directories = [
        DETECTIONS_FOLDER,
        LOGS_FOLDER,
        "models"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)


def validate_config():
    """Validate critical configuration settings."""
    errors = []
    
    # Check Telegram configuration
    if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == "your_bot_token_here":
        errors.append(
            "❌ TELEGRAM_BOT_TOKEN not configured in .env file"
        )
    
    if not TELEGRAM_CHAT_ID or TELEGRAM_CHAT_ID == "your_chat_id_here":
        errors.append(
            "❌ TELEGRAM_CHAT_ID not configured in .env file"
        )
    
    # Check model file exists
    if not os.path.exists(MODEL_PATH):
        errors.append(
            f"❌ Model file not found: {MODEL_PATH}"
        )
    
    # Check confidence threshold
    if not (0.0 <= CONF_THRESHOLD <= 1.0):
        errors.append(
            f"❌ CONF_THRESHOLD must be between 0.0 and 1.0, got {CONF_THRESHOLD}"
        )
    
    return errors


def print_config():
    """Print current configuration (for debugging)."""
    print("\n" + "=" * 70)
    print("🐍 CURRENT CONFIGURATION")
    print("=" * 70)
    print(f"Project: {PROJECT_NAME} v{PROJECT_VERSION}")
    print(f"\n📷 Camera Configuration:")
    print(f"   Resolution: {CAMERA_WIDTH}x{CAMERA_HEIGHT}")
    print(f"   Camera Index: {CAMERA_INDEX}")
    print(f"\n🎯 Detection Configuration:")
    print(f"   Confidence Threshold: {CONF_THRESHOLD:.0%}")
    print(f"   Alert Cooldown: {ALERT_COOLDOWN}s")
    print(f"\n🚨 Alert Configuration:")
    print(f"   Voice Alert: {'Enabled' if ENABLE_VOICE_ALERT else 'Disabled'}")
    print(f"   Sound Alert: {'Enabled' if ENABLE_SOUND_ALERT else 'Disabled'}")
    print(f"   Telegram Alert: {'Enabled' if ENABLE_TELEGRAM_ALERT else 'Disabled'}")
    print(f"   Photo Upload: {'Enabled' if ENABLE_TELEGRAM_PHOTO else 'Disabled'}")
    print(f"\n📍 Location Details:")
    print(f"   Location: {LOCATION}")
    print(f"   Emergency Contact: {EMERGENCY_CONTACT}")
    print(f"\n💾 Storage Configuration:")
    print(f"   Detections Folder: {DETECTIONS_FOLDER}")
    print(f"   Logs Folder: {LOGS_FOLDER}")
    print(f"   Model Path: {MODEL_PATH}")
    print(f"\n🔧 System Configuration:")
    print(f"   Debug Mode: {'ON' if DEBUG else 'OFF'}")
    print(f"   Verbose Logging: {'ON' if VERBOSE else 'OFF'}")
    print("=" * 70 + "\n")


# =========================================================
# INITIALIZATION
# =========================================================

if __name__ == "__main__":
    # Create necessary directories
    create_directories()
    
    # Validate configuration
    errors = validate_config()
    if errors:
        print("\n⚠️  CONFIGURATION VALIDATION ERRORS:\n")
        for error in errors:
            print(f"   {error}")
        print("\n   Please configure .env file properly.\n")
    else:
        print("\n✅ Configuration validation passed!\n")
    
    # Print current configuration
    print_config()
