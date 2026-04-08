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

        detected_frame, count = detector.detect(frame)

        status = analyzer.analyze(count)
        wait_time = estimator.estimate(count)

        alert_message = ""

        if count > 6:
            alert_message = "ALERT: Queue Too Long!"

        print("People:", count)
        print("Queue:", status)
        print("Waiting Time:", wait_time)

        dashboard_frame = dashboard.create_dashboard(count, status, wait_time)

        if alert_message != "":
            cv2.putText(detected_frame, alert_message, (20,80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

            cv2.putText(dashboard_frame, "CROWD ALERT!", (20,250),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

        cv2.imshow("Camera Feed", detected_frame)
        cv2.imshow("Dashboard", dashboard_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()