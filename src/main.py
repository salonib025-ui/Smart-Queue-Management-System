import cv2

from src.detection.people_detector import PeopleDetector
from src.analytics.queue_analyzer import QueueAnalyzer
from src.analytics.waiting_time import WaitingTimeEstimator
from src.ai.decision_engine import DecisionEngine

from src.ui.dashboard import Dashboard
from src.data.data_logger import DataLogger


print(DecisionEngine.__module__)


def main():

    # =========================
    # Initialize Modules
    # =========================
    detector = PeopleDetector()
    queue_analyzer = QueueAnalyzer()
    waiting_estimator = WaitingTimeEstimator(service_rate=0.5)
    decision_engine = DecisionEngine()

    dashboard = Dashboard()
    logger = DataLogger()

    # =========================
    # Camera Setup
    # =========================
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("Smart Queue Management System", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Smart Queue Dashboard", cv2.WINDOW_NORMAL)

    cv2.moveWindow("Smart Queue Management System", 50, 50)
    cv2.moveWindow("Smart Queue Dashboard", 900, 50)

    cv2.resizeWindow("Smart Queue Management System", 800, 600)
    cv2.resizeWindow("Smart Queue Dashboard", 500, 300)

    if not cap.isOpened():
        print("Camera not detected")
        return

    print("Camera started successfully")

    # =========================
    # Main Loop
    # =========================
    while True:

        ret, frame = cap.read()
        if not ret:
            break

        # --- People Detection ---
        detected_frame, people_count = detector.detect(frame)

        # --- Queue Analysis ---
        queue_status = queue_analyzer.update(people_count)

        # --- Waiting Time ---
        waiting_time = waiting_estimator.estimate(people_count)

        # --- Smart Decision Engine ---
        decision = decision_engine.make_decision(
            people_count,
            queue_status,
            waiting_time
        )

        # --- Log Data ---
        logger.log(people_count, queue_status, waiting_time)

        print(
            f"People: {people_count} | "
            f"Status: {queue_status} | "
            f"Waiting: {waiting_time:.1f} | "
            f"Decision: {decision}"
        )

        # =========================
        # SHOW WINDOWS
        # =========================

        # Camera → ONLY video
        cv2.imshow("Smart Queue Management System", detected_frame)

        # Dashboard → ALL analytics
        dashboard.show_dashboard(
            people_count,
            queue_status,
            waiting_time,
            decision
        )

        # Exit Key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    logger.show_visualization()


if __name__ == "__main__":
    main()