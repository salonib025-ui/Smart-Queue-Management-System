import cv2
import numpy as np

class Dashboard:

    def create_dashboard(self, count, status, wait):

        dashboard = np.zeros((300, 500, 3), dtype=np.uint8)

        cv2.putText(dashboard, "SMART QUEUE DASHBOARD", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

        cv2.putText(dashboard, f"People Count: {count}", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        cv2.putText(dashboard, f"Queue Status: {status}", (20, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

        cv2.putText(dashboard, f"Waiting Time: {wait} min", (20, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        return dashboard