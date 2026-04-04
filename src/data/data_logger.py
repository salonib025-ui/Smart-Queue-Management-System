import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

class DataLogger:

    def __init__(self):
        self.file = "queue_data.csv"

        # Create file if not exists
        if not os.path.exists(self.file):
            df = pd.DataFrame(columns=["Timestamp", "People_Count", "Queue_Status", "Waiting_Time"])
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

    def show_visualization(self):
        # Read CSV
        df = pd.read_csv(self.file, parse_dates=["Timestamp"])

        if df.empty:
            print("No data to visualize")
            return

        # Plot People, Queue, and Waiting Time over time
        plt.figure(figsize=(10, 5))
        plt.plot(df["Timestamp"], df["People_Count"], label="People Count", marker='o')
        plt.plot(df["Timestamp"], df["Queue_Status"], label="Queue Status", marker='x')
        plt.plot(df["Timestamp"], df["Waiting_Time"], label="Waiting Time", marker='s')

        plt.xlabel("Timestamp")
        plt.ylabel("Values")
        plt.title("Queue Analytics Over Time")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()