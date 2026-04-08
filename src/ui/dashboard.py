import cv2
import numpy as np

class Dashboard:

    def create_dashboard(self, count, status, wait):

        # Create blank dashboard image
        dashboard = np.zeros((300, 500, 3), dtype=np.uint8)

        # Title
        cv2.putText(
            dashboard,
            "SMART QUEUE DASHBOARD",
            (40, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # People count
        cv2.putText(
            dashboard,
            f"People Count: {count}",
            (40, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # Queue status
        cv2.putText(
            dashboard,
            f"Queue Status: {status}",
            (40, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

        # Waiting time
        cv2.putText(
            dashboard,
            f"Waiting Time: {wait} min",
            (40, 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

        return dashboard