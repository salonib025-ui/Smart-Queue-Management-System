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

        print("People:", count)

        cv2.putText(
            detected_frame,
            f"People Count: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Smart Queue System", detected_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
