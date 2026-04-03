import cv2

class Dashboard:

    def draw(self, frame, people_count, queue_status, waiting_time):

        # ===== Title =====
        cv2.putText(
            frame,
            "AI Smart Queue Management System",
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        # ===== People Count =====
        cv2.putText(
            frame,
            f"People: {people_count}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # ===== Queue Status =====
        cv2.putText(
            frame,
            f"Queue Status: {queue_status}",
            (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        # ===== Waiting Time =====
        cv2.putText(
            frame,
            f"Waiting Time: {waiting_time} mins",
            (20, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

        return frame