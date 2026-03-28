import cv2

# ==========================
# Select Camera Source
# ==========================

# 0 → Laptop Webcam
# Change later for CCTV or video file
cap = cv2.VideoCapture(0)

# Check camera opened
if not cap.isOpened():
    print("Error: Camera not detected")
    exit()

print("Camera started successfully")

# ==========================
# Video Streaming Loop
# ==========================

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Show live camera feed
    cv2.imshow("Smart Queue Management - Live Feed", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ==========================
# Release Resources
# ==========================

cap.release()
cv2.destroyAllWindows()