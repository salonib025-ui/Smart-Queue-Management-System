import cv2

from src.detection.people_detector import PeopleDetector
from src.analytics.queue_analyzer import QueueAnalyzer
from src.analytics.waiting_time import WaitingTimeEstimator
from src.analytics.analytics_visualizer import AnalyticsVisualizer

from src.ui.dashboard import Dashboard
from src.data.data_logger import DataLogger


def main():

    # ===== Modules =====
    detector = PeopleDetector()
    queue_analyzer = QueueAnalyzer()
    waiting_estimator = WaitingTimeEstimator(service_rate=0.5)
    dashboard = Dashboard()
    logger = DataLogger()

    # ===== Camera =====
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

    # ===== Main Loop =====
    while True:

        ret, frame = cap.read()
        if not ret:
            break

        # People Detection
        detected_frame, people_count = detector.detect(frame)

        # Queue Analysis
        queue_status = queue_analyzer.update(people_count)

        # Waiting Time Prediction
        waiting_time = waiting_estimator.estimate(people_count)

        # Save Data
        logger.log(people_count, queue_status, waiting_time)

        print("People:", people_count)

        # Overlay UI
        final_frame = dashboard.draw(
            detected_frame,
            people_count,
            queue_status,
            waiting_time
        )

        # Separate Dashboard
        dashboard.show_dashboard(
            people_count,
            queue_status,
            waiting_time
        )

        cv2.imshow("Smart Queue Management System", final_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # ===== Analytics After Closing =====
    visualizer = AnalyticsVisualizer()
    visualizer.plot_people_trend()
    visualizer.plot_waiting_time()
    visualizer.peak_time()


if __name__ == "__main__":
    main()
    
    
    
