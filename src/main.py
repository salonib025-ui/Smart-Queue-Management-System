import cv2
from camera.camera_input import CameraInput
from processing.frame_processor import FrameProcessor
from detection.people_detector import PeopleDetector


def main():

    camera = CameraInput(0)
    processor = FrameProcessor()
    detector = PeopleDetector()

    while True:

        frame = camera.get_frame()

        if frame is None:
            break

        processed_frame = processor.process(frame)

        detected_frame, count = detector.detect(processed_frame)

        print("People count:", count)

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

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
