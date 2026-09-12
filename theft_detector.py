import cv2
from ultralytics import YOLO

# Load the AI model
model = YOLO("yolo11n.pt")

# Start the camera
camera = cv2.VideoCapture(0)

# Number of bananas when we start
starting_count = None

print("Starting Banana Security System...")
print("Show the banana to the camera.")

while True:
    success, frame = camera.read()

    if not success:
        print("Camera error!")
        break

    # Detect objects
    results = model(frame, verbose=False)

    # Count bananas
    banana_count = 0

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        if class_name == "banana":
            banana_count += 1

    # Set the starting number
    if starting_count is None and banana_count > 0:
        starting_count = banana_count
        print(f"Starting bananas: {starting_count}")

    # Check for theft
    if starting_count is not None and banana_count < starting_count:
        status = "THEFT DETECTED!"
        print("🚨 THEFT DETECTED!")
    else:
        status = "SECURE"

    # Draw AI boxes
    frame = results[0].plot()

    # Display status on camera
    cv2.putText(
        frame,
        f"Bananas: {banana_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        status,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255) if "THEFT" in status else (0, 255, 0),
        2
    )

    cv2.imshow("🍌 Banana Security System", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()