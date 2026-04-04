import cv2

from detection.people_detector import PeopleDetector
from analytics.queue_analyzer import QueueAnalyzer
from analytics.waiting_time import WaitingTimeEstimator
from ui.dashboard import Dashboard
from data.data_logger import DataLogger


def main():

    detector = PeopleDetector()
    queue_analyzer = QueueAnalyzer()
    waiting_estimator = WaitingTimeEstimator(service_rate=0.5)
    dashboard = Dashboard()
    logger = DataLogger()

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

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        detected_frame, people_count = detector.detect(frame)

        queue_status = queue_analyzer.update(people_count)

        waiting_time = waiting_estimator.estimate(people_count)

        # Overlay dashboard
        final_frame = dashboard.draw(
            detected_frame,
            people_count,
            queue_status,
            waiting_time
        )

        # Separate dashboard window
        dashboard.show_dashboard(
            people_count,
            queue_status,
            waiting_time
        )

        # Log data
        logger.log(people_count, queue_status, waiting_time)

        cv2.imshow("Smart Queue Management System", final_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()