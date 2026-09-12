import cv2
from ultralytics import YOLO

# Load the AI model
model = YOLO("yolo11n.pt")

# Start the laptop camera
camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        print("Camera could not be opened.")
        break

    # Ask YOLO to detect objects
    results = model(frame, verbose=False)

    # Draw the detection boxes
    annotated_frame = results[0].plot()

    # Show the camera with AI detection
    cv2.imshow("Banana AI Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()