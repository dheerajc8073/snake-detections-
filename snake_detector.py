import cv2
import time
import os
import numpy as np
import pyttsx3
import winsound
import requests

from datetime import datetime
from ultralytics import YOLO

# =========================================================
# TELEGRAM CONFIG
# =========================================================

BOT_TOKEN = "8916940301:AAEyg-E5QQrTsa-R2zvRUQ1lUF8a3fo8F5g"

CHAT_ID = "8259476397"

TELEGRAM_URL = (
    f"https://api.telegram.org/bot{BOT_TOKEN}"
)

# =========================================================
# EMERGENCY DETAILS
# =========================================================

EMERGENCY_CONTACT = "8277100200"

LOCATION = "College Classroom"

# =========================================================
# LOAD YOLO MODEL
# =========================================================

model = YOLO(
    r"C:\Users\Dheeraj c\Desktop\SnakeDetectionProject\snake_model.pt"
)

# =========================================================
# SETTINGS
# =========================================================

CONF_THRESHOLD = 0.80

ALERT_COOLDOWN = 120

last_alert = 0

# =========================================================
# CREATE DETECTION FOLDER
# =========================================================

os.makedirs("detections", exist_ok=True)

# =========================================================
# VOICE ENGINE
# =========================================================

engine = pyttsx3.init()

engine.setProperty('rate', 150)

engine.setProperty('volume', 1.0)

# =========================================================
# START CAMERA
# =========================================================

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("\n" + "=" * 70)
print("🐍 AI SNAKE EMERGENCY SYSTEM STARTED")
print("=" * 70)

print("✅ Snake Detection Enabled")
print("✅ Telegram Alerts Enabled")
print("✅ Voice Warning Enabled")
print("✅ Alarm Enabled\n")

# =========================================================
# TELEGRAM MESSAGE
# =========================================================


def send_telegram_message(message):

    try:

        requests.post(

            f"{TELEGRAM_URL}/sendMessage",

            data={
                "chat_id": CHAT_ID,
                "text": message
            }
        )

        print("✅ Telegram Message Sent")

    except Exception as e:

        print("Telegram Message Error:", e)

# =========================================================
# TELEGRAM PHOTO
# =========================================================


def send_telegram_photo(filepath, caption):

    try:

        with open(filepath, "rb") as photo:

            requests.post(

                f"{TELEGRAM_URL}/sendPhoto",

                data={
                    "chat_id": CHAT_ID,
                    "caption": caption
                },

                files={
                    "photo": photo
                }
            )

        print("✅ Telegram Photo Sent")

    except Exception as e:

        print("Telegram Photo Error:", e)

# =========================================================
# ALERT FUNCTION
# =========================================================


def trigger_alert(frame, confidence):

    global last_alert

    now = time.time()

    if now - last_alert < ALERT_COOLDOWN:
        return

    last_alert = now

    # =====================================================
    # SAVE IMAGE
    # =====================================================

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"detections/snake_{ts}.jpg"

    cv2.imwrite(filename, frame)

    print("\n📸 Image Saved:", filename)

    # =====================================================
    # ALARM SOUND
    # =====================================================

    winsound.Beep(1500, 1200)

    # =====================================================
    # VOICE WARNING
    # =====================================================

    engine.say("Warning! Snake detected nearby")

    engine.runAndWait()

    # =====================================================
    # SIMPLE RISK ANALYSIS
    # =====================================================

    if confidence > 0.90:

        risk = "HIGH RISK"

    elif confidence > 0.80:

        risk = "MEDIUM RISK"

    else:

        risk = "LOW RISK"

    analysis = f"""

🐍 SNAKE DETECTED

⚠️ Risk Level: {risk}

🎯 Confidence: {confidence:.0%}

📌 Safety Instructions:
• Stay away from snake
• Do not attempt handling
• Alert nearby people
• Contact wildlife rescue
• Maintain safe distance

"""

    print("\n" + "=" * 70)
    print("SNAKE ALERT")
    print("=" * 70)
    print(analysis)

    # =====================================================
    # TELEGRAM MESSAGE
    # =====================================================

    telegram_message = (

        f"🚨 AI SNAKE ALERT 🚨\n\n"

        f"🎯 Detection Confidence: {confidence:.0%}\n\n"

        f"⚠️ Risk Level: {risk}\n\n"

        f"📍 Location: {LOCATION}\n\n"

        f"🕒 Time:\n"
        f"{datetime.now().strftime('%I:%M:%S %p')}\n\n"

        f"📌 Safety Instructions:\n"
        f"• Stay away from snake\n"
        f"• Do not attempt handling\n"
        f"• Alert nearby people\n"
        f"• Contact wildlife rescue\n\n"

        f"📞 Emergency Contact:\n"
        f"{EMERGENCY_CONTACT}"
    )

    # =====================================================
    # SEND TELEGRAM TEXT
    # =====================================================

    send_telegram_message(
        telegram_message
    )

    # =====================================================
    # SEND TELEGRAM PHOTO
    # =====================================================

    send_telegram_photo(
        filename,
        "🚨 Snake Detection Image"
    )

    print("\n✅ Telegram Alert Sent")

# =========================================================
# MAIN LOOP
# =========================================================


while True:

    ret, frame = cap.read()

    if not ret:

        print("❌ Camera Error")

        break

    # =====================================================
    # IMAGE ENHANCEMENT
    # =====================================================

    frame = cv2.convertScaleAbs(
        frame,
        alpha=1.2,
        beta=15
    )

    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    frame = cv2.filter2D(
        frame,
        -1,
        kernel
    )

    # =====================================================
    # YOLO DETECTION
    # =====================================================

    results = model(
        frame,
        conf=CONF_THRESHOLD,
        verbose=False
    )

    snake_detected = False

    best_conf = 0

    for r in results:

        for box in r.boxes:

            conf = float(box.conf[0])

            if conf < CONF_THRESHOLD:
                continue

            if conf > best_conf:

                best_conf = conf

                snake_detected = True

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                # =============================================
                # DRAW DETECTION BOX
                # =============================================

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    3
                )

                text = (
                    f"SNAKE ({conf:.0%})"
                )

                cv2.putText(
                    frame,
                    text,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2
                )

    # =====================================================
    # STATUS BAR
    # =====================================================

    cv2.rectangle(
        frame,
        (0, 0),
        (1280, 60),
        (0, 0, 0),
        -1
    )

    if snake_detected:

        cv2.putText(
            frame,
            "🚨 SNAKE DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        trigger_alert(
            frame,
            best_conf
        )

    else:

        cv2.putText(
            frame,
            "🟢 Monitoring... No Snake Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    # =====================================================
    # SHOW WINDOW
    # =====================================================

    cv2.imshow(
        "🐍 AI Snake Emergency Detection System",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):

        break

# =========================================================
# CLEANUP
# =========================================================

cap.release()

cv2.destroyAllWindows()

print("\n✅ System Closed")
