import cv2
from detection.people_detector import PeopleDetector
from analytics.queue_analyzer import QueueAnalyzer
from analytics.waiting_time import WaitingTimeEstimator
<<<<<<< HEAD
from ui.dashboard import Dashboard
=======
>>>>>>> a0a44b523fb1c07881eefd634b0b8a84b39377ed


def main():

    cap = cv2.VideoCapture(0)

    detector = PeopleDetector()
    analyzer = QueueAnalyzer()
<<<<<<< HEAD
    estimator = WaitingTimeEstimator()
    dashboard = Dashboard()
=======
    waiting_estimator = WaitingTimeEstimator(service_rate=0.5)
>>>>>>> a0a44b523fb1c07881eefd634b0b8a84b39377ed

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Detect people
        detected_frame, count = detector.detect(frame)

<<<<<<< HEAD
        status = analyzer.analyze(count)

        wait_time = estimator.estimate(count)
=======
        # Analyze queue
        queue_status = analyzer.update(count)

        # Estimate waiting time
        waiting_time = waiting_estimator.estimate(count)
>>>>>>> a0a44b523fb1c07881eefd634b0b8a84b39377ed

        print("People:", count)
        print("Queue:", status)
        print("Waiting Time:", wait_time)

<<<<<<< HEAD
        final_frame = dashboard.display(detected_frame, count, status, wait_time)

        cv2.imshow("Smart Queue Management System", final_frame)
=======
        # Display People Count
        cv2.putText(
            detected_frame,
            f"People Count: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Display Queue Status
        cv2.putText(
            detected_frame,
            f"Queue Status: {queue_status}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

        # Display Waiting Time
        cv2.putText(
            detected_frame,
            f"Waiting Time: {waiting_time} mins",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.imshow("Smart Queue System", detected_frame)
>>>>>>> a0a44b523fb1c07881eefd634b0b8a84b39377ed

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()