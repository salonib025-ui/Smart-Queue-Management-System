import cv2
from detection.people_detector import PeopleDetector
from analytics.queue_analyzer import QueueAnalyzer
from analytics.waiting_time import WaitingTimeEstimator


def main():

    cap = cv2.VideoCapture(0)

    detector = PeopleDetector()
    analyzer = QueueAnalyzer()
    waiting_estimator = WaitingTimeEstimator(service_rate=0.5)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Detect people
        detected_frame, count = detector.detect(frame)

        # Analyze queue
        queue_status = analyzer.update(count)

        # Estimate waiting time
        waiting_time = waiting_estimator.estimate(count)

        print("People:", count)

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

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
