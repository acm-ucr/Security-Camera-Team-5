from ultralytics import YOLO
import cv2

# Load your trained YOLOv11 model
model = YOLO("best.pt")  # or 'yolov11n.pt', 'yolov11s.pt', etc.

# Open webcam (0 = default webcam)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
  print("Error: Could not open webcam.")
  exit()

while True:
  ret, frame = cap.read()
  if not ret:
    print("Failed to grab frame.")
    break

  # Run YOLOv11 inference on the frame
  results = model.predict(source=frame, conf=0.3, verbose=False)

  # Plot results on the frame
  annotated_frame = results[0].plot()

  # Display the result
  cv2.imshow("YOLOv11 Live Inference", annotated_frame)

  # Press 'q' to exit the live stream
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()
