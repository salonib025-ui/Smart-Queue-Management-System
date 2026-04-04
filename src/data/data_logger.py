import pandas as pd
import os
from datetime import datetime


class DataLogger:

    def __init__(self):
        self.file = "queue_data.csv"

        # Create file if not exists
        if not os.path.exists(self.file):
            df = pd.DataFrame(columns=["Timestamp", "People", "Queue", "Waiting"])
            df.to_csv(self.file, index=False)

    def log(self, people, queue, waiting):
        data = {
            "Timestamp": datetime.now(),
            "People": people,
            "Queue": queue,
            "Waiting": waiting
        }

        df = pd.DataFrame([data])
        df.to_csv(self.file, mode='a', header=False, index=False)
