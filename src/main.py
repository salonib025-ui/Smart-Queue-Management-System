import cv2
from detection.people_detector import PeopleDetector
from analytics.queue_analyzer import QueueAnalyzer


def main():

    cap = cv2.VideoCapture(0)
    detector = PeopleDetector()
    analyzer = QueueAnalyzer()

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        detected_frame, count = detector.detect(frame)

        # 🔥 NEW (Queue Analysis)
        queue_status = analyzer.update(count)

        print("People:", count)

        # People Count Display
        cv2.putText(
            detected_frame,
            f"People Count: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # 🔥 NEW (Queue Status Display)
        cv2.putText(
            detected_frame,
            f"Queue Status: {queue_status}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

        cv2.imshow("Smart Queue System", detected_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
