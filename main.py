import cv2

# ==========================
# Import Project Modules
# ==========================

from detection.people_detector import PeopleDetector
from analytics.queue_analyzer import QueueAnalyzer
from analytics.waiting_time import WaitingTimeEstimator
from ui.dashboard import Dashboard


# ==========================
# Initialize Modules
# ==========================

detector = PeopleDetector()
queue_analyzer = QueueAnalyzer()
waiting_estimator = WaitingTimeEstimator(service_rate=0.5)
dashboard = Dashboard()

# ==========================
# Camera Source
# ==========================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not detected")
    exit()

print("Camera started successfully")

# ==========================
# Main Loop
# ==========================

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # ===== Step 4: People Detection =====
    annotated_frame, people_count = detector.detect(frame)

    # ===== Step 5: Queue Analysis =====
    queue_status = queue_analyzer.update(people_count)

    # ===== Step 6: Waiting Time Prediction =====
    waiting_time = waiting_estimator.estimate(people_count)

    # ===== Step 7: Dashboard UI =====
    final_frame = dashboard.draw(
        annotated_frame,
        people_count,
        queue_status,
        waiting_time
    )

    # ===== Show Output =====
    cv2.imshow("Smart Queue Management System", final_frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ==========================
# Cleanup
# ==========================

cap.release()
cv2.destroyAllWindows()