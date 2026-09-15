import cv2


class FrameProcessor:

    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height

    def process(self, frame):
        """
        Resize incoming frame for inference speed optimization.
        """
        frame = cv2.resize(frame, (self.width, self.height))
        return frame