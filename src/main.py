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

        print("People:", count)
        print("Queue:", status)
        print("Waiting Time:", wait_time)

        final_frame = dashboard.display(detected_frame, count, status, wait_time)

        cv2.imshow("Smart Queue Management System", final_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()