import cv2
from detection.people_detector import PeopleDetector
from analytics.analytics_visualizer import AnalyticsVisualizer
from analytics.data_logger import DataLogger

def main():

    cap = cv2.VideoCapture(0)
    detector = PeopleDetector()
logger = DataLogger()
    while True:

        ret, frame = cap.read()

        if not ret:
            break

        detected_frame, count = detector.detect(frame)
# Queue logic
if count == 0:
    status = "No Queue"
elif count <= 3:
    status = "Short"
elif count <= 6:
    status = "Moderate"
else:
    status = "Long"

waiting_time = count * 2

# Save data
logger.log(count, status, waiting_time)
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

    # ✅ Step 9 Analytics (runs after camera stops)
    visualizer = AnalyticsVisualizer()
    visualizer.plot_people_trend()
    visualizer.plot_waiting_time()
    visualizer.peak_time()


if __name__ == "__main__":
    main()
