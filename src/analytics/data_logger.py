import csv
from datetime import datetime
import os

class DataLogger:

    def __init__(self):
        os.makedirs("data", exist_ok=True)
        self.file = "data/queue_data.csv"

        if not os.path.exists(self.file):
            with open(self.file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["Timestamp", "People", "QueueStatus", "WaitingTime"]
                )

    def log(self, people, status, waiting_time):

        with open(self.file, "a", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                datetime.now().strftime("%H:%M:%S"),
                people,
                status,
                waiting_time
            ])
