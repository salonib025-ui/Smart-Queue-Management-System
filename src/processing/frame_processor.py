import cv2


class FrameProcessor:

    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height

    def process(self, frame):
        """
        Process incoming frame before AI detection
        """

        # Resize frame (speed improvement)
        frame = cv2.resize(frame, (self.width, self.height))

        # Convert color (optional optimization)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return frame