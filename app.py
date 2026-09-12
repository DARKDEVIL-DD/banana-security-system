from flask import Flask, render_template, Response, jsonify
import cv2
from ultralytics import YOLO
import time

app = Flask(__name__)

# Load AI model
model = YOLO("yolo11n.pt")

# Phone camera URL
camera_url = "http://10.196.196.61:8080/video"

# Camera
camera = None

# Banana information
banana_count = 0
starting_banana_count = None

# Theft information
theft_alerts = 0
security_status = "SECURE"

# Prevent false alarms
missing_frames = 0


def connect_camera():
    global camera

    print("Connecting to phone camera...")

    camera = cv2.VideoCapture(camera_url)

    if camera.isOpened():
        print("📱 Phone camera connected!")
        return True

    print("❌ Phone camera not available.")

    camera.release()
    camera = None

    return False


def generate_frames():

    global camera
    global banana_count
    global starting_banana_count
    global theft_alerts
    global security_status
    global missing_frames

    while True:

        # Try to connect if camera is unavailable
        if camera is None:

            connect_camera()

            if camera is None:
                time.sleep(0.2)
                continue

        # Read camera frame
        success, frame = camera.read()

        # Camera disconnected
        if not success:

            print("⚠️ Camera connection lost.")

            camera.release()
            camera = None

            time.sleep(0.2)

            continue

        # Detect ONLY bananas
        results = model(
            frame,
            classes=[46],
            verbose=False
        )

        # Count bananas
        current_count = 0

        for box in results[0].boxes:

            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            if class_name.lower() == "banana":
                current_count += 1

        banana_count = current_count

        # Set starting banana count
        if starting_banana_count is None and banana_count > 0:

            starting_banana_count = banana_count

            security_status = "SECURE"

            print(
                "Starting banana count:",
                starting_banana_count
            )

        # Theft detection
        if starting_banana_count is not None:

            if banana_count < starting_banana_count:

                missing_frames += 1

                if missing_frames >= 15:

                    if security_status != "THEFT DETECTED":

                        theft_alerts += 1

                        security_status = "THEFT DETECTED"

                        print("🚨 THEFT DETECTED!")

            else:

                missing_frames = 0

                if security_status == "THEFT DETECTED":

                    security_status = "SECURE"

                    print(
                        "🛡️ Banana returned - SYSTEM SECURE"
                    )

        # Draw detection boxes
        frame = results[0].plot()

        # Convert to JPEG
        success, buffer = cv2.imencode(
            ".jpg",
            frame
        )

        if not success:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame_bytes
            + b"\r\n"
        )


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/banana_count")
def get_banana_count():

    return jsonify({
        "count": banana_count
    })


@app.route("/security_status")
def get_security_status():

    return jsonify({
        "status": security_status,
        "alerts": theft_alerts
    })


if __name__ == "__main__":

    app.run(debug=True)