import cv2

class Dashboard:

    def display(self, frame, count, status, wait):

        cv2.putText(frame, f"People: {count}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.putText(frame, f"Queue: {status}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        cv2.putText(frame, f"Wait: {wait} min", (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        return frame