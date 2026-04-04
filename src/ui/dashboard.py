import cv2
import numpy as np

class Dashboard:

    def __init__(self):
        self.dashboard = np.zeros((300, 500, 3), dtype=np.uint8)

    # Overlay on camera
    def draw(self, frame, people_count, queue_status, waiting_time):

        cv2.putText(frame,"AI Smart Queue Management System",
                    (20,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

        cv2.putText(frame,f"People: {people_count}",
                    (20,70),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

        cv2.putText(frame,f"Queue Status: {queue_status}",
                    (20,110),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)

        cv2.putText(frame,f"Waiting Time: {waiting_time} mins",
                    (20,150),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)

        return frame

    # Separate dashboard window
    def show_dashboard(self, people_count, queue_status, waiting_time):

        self.dashboard[:] = (0,0,0)

        cv2.putText(self.dashboard,"SMART QUEUE DASHBOARD",
                    (60,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

        cv2.putText(self.dashboard,f"People Count: {people_count}",
                    (50,100),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

        cv2.putText(self.dashboard,f"Queue Status: {queue_status}",
                    (50,150),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)

        cv2.putText(self.dashboard,f"Waiting Time: {waiting_time} min",
                    (50,200),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

        cv2.imshow("Smart Queue Dashboard", self.dashboard)