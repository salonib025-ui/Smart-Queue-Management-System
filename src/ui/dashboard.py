import cv2
import numpy as np
<<<<<<< HEAD

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
=======


class Dashboard:

    def __init__(self):
        self.dashboard = np.zeros((300, 500, 3), dtype=np.uint8)

    def show_dashboard(self, people_count, queue_status, waiting_time, decision):

        # Clear dashboard
        self.dashboard[:] = (0, 0, 0)

        # Title
        cv2.putText(
            self.dashboard,
            "AI SMART QUEUE DASHBOARD",
            (40, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        # People Count
        cv2.putText(
            self.dashboard,
            f"People: {people_count}",
            (40, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        # Queue Status
        cv2.putText(
            self.dashboard,
            f"Queue Status: {queue_status}",
            (40, 130),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 0),
            2
        )

        # Waiting Time
        cv2.putText(
            self.dashboard,
            f"Waiting Time: {waiting_time:.1f} mins",
            (40, 170),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

        # Decision
        cv2.putText(
            self.dashboard,
            f"Decision: {decision}",
            (40, 210),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 128, 255),
            2
        )

        cv2.imshow("Smart Queue Dashboard", self.dashboard)
>>>>>>> 4ad1d51ca5fc7882d79953ababdad8a15a44ef2e
