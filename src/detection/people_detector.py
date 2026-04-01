from ultralytics import YOLO


class PeopleDetector:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):

        results = self.model(frame)

        # Use YOLO built-in plotting (THIS WORKS FOR YOU)
        annotated_frame = results[0].plot()

        people_count = 0

        # Count people
        if results[0].boxes is not None:
            for box in results[0].boxes:
                if int(box.cls.item()) == 0:
                    people_count += 1

        return annotated_frame, people_count