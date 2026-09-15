import cv2

from src.detection.people_detector import PeopleDetector
from src.analytics.queue_analyzer import QueueAnalyzer
from src.analytics.waiting_time import WaitingTimeEstimator
from src.ui.dashboard import Dashboard
from src.data.data_logger import DataLogger


def main():

    cap = cv2.VideoCapture(0)

    detector = PeopleDetector()
    analyzer = QueueAnalyzer()
    estimator = WaitingTimeEstimator()
    dashboard = Dashboard()
    logger = DataLogger()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Detect people
        detected_frame, count = detector.detect(frame)

        # Update and calculate moving average status
        status = analyzer.update(count)

        # Estimate waiting time
        wait_time = estimator.estimate(count)

        # Log metrics to CSV
        logger.log(count, status, wait_time)

        # Alert evaluation
        alert_message = ""
        if count > 6:
            alert_message = "ALERT: Queue Too Long!"

        print("People:", count)
        print("Queue:", status)
        print("Waiting Time:", wait_time)

        # Create dashboard display
        dashboard_frame = dashboard.create_dashboard(count, status, wait_time)

        # Show alerts on display windows
        if alert_message != "":
            cv2.putText(
                detected_frame,
                alert_message,
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

            cv2.putText(
                dashboard_frame,
                "CROWD ALERT!",
                (20, 250),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 0, 255),
                2
            )

        # Display output frames
        cv2.imshow("Camera Feed", detected_frame)
        cv2.imshow("Dashboard", dashboard_frame)

        # Press 'q' to quit application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()