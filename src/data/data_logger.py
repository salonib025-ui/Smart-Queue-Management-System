import csv
import os
from datetime import datetime


class DataLogger:

    def __init__(self, filename="queue_data.csv"):

        self.filename = filename

        # Create file if not exists
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Timestamp",
                    "People_Count",
                    "Queue_Status",
                    "Waiting_Time"
                ])

    def log(self, people, status, wait):

        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%H:%M:%S"),
                people,
                status,
                wait
            ])