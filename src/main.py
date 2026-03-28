import cv2
from camera.camera_input import CameraInput


def main():
    camera = CameraInput(0)

    while True:
        frame = camera.get_frame()

        if frame is None:
            break

        cv2.imshow("Smart Queue Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()


if __name__ == "__main__":
    main()