import cv2
from camera.camera_input import CameraInput


def main():
    camera = CameraInput(0)

    while True:
        import cv2
from camera.camera_input import CameraInput
from processing.frame_processor import FrameProcessor


def main():

    camera = CameraInput(0)
    processor = FrameProcessor()

    while True:

        frame = camera.get_frame()

        if frame is None:
            break

        processed_frame = processor.process(frame)

        # Convert back for display
        display_frame = cv2.cvtColor(processed_frame, cv2.COLOR_RGB2BGR)

        cv2.imshow("Smart Queue System", display_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()


if __name__ == "__main__":
    main()