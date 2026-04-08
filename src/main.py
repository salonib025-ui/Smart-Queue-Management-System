import cv2

from detection.people_detector import PeopleDetector
from analytics.queue_analyzer import QueueAnalyzer
from analytics.waiting_time import WaitingTimeEstimator
from ui.dashboard import Dashboard


def main():

    cap = cv2.VideoCapture(0)

    detector = PeopleDetector()
    analyzer = QueueAnalyzer()
    estimator = WaitingTimeEstimator()
    dashboard = Dashboard()

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Detect people
        detected_frame, count = detector.detect(frame)


        status = analyzer.analyze(count)
        wait_time = estimator.estimate(count)

        # Analyze queue
        status = analyzer.analyze(count)

        # Estimate waiting time
        wait_time = estimator.estimate(count)


        # Alert system
        alert_message = ""


        if count > 6:
            alert_message = "ALERT: Queue Too Long!"

        print("People:", count)
        print("Queue:", status)
        print("Waiting Time:", wait_time)

        dashboard_frame = dashboard.create_dashboard(count, status, wait_time)

        if count > 6:
            alert_message = "ALERT: Queue Too Long!"

        # Create dashboard
        dashboard_frame = dashboard.create_dashboard(count, status, wait_time)


        # Show alert on camera
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

            # Show alert on dashboard
            cv2.putText(
                dashboard_frame,
                "CROWD ALERT!",
                (20, 250),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 0, 255),
                2
            )

        # Display windows
        cv2.imshow("Camera Feed", detected_frame)
        cv2.imshow("Dashboard", dashboard_frame)

        # Exit when pressing Q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()