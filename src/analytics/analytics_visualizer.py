import pandas as pd
import matplotlib.pyplot as plt

class AnalyticsVisualizer:

    def __init__(self):
        self.file = "data/queue_data.csv"

    def load_data(self):
        return pd.read_csv(self.file)

    def plot_people_trend(self):
        data = self.load_data()

        plt.figure()
        plt.plot(data["Timestamp"], data["People"])
        plt.xlabel("Time")
        plt.ylabel("People Count")
        plt.title("People Trend Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_waiting_time(self):
        data = self.load_data()

        plt.figure()
        plt.plot(data["Timestamp"], data["WaitingTime"])
        plt.xlabel("Time")
        plt.ylabel("Waiting Time")
        plt.title("Waiting Time Trend")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def peak_time(self):
        data = self.load_data()

        max_row = data.loc[data["People"].idxmax()]

        print("\n🔥 Peak Crowd Time:")
        print("Time:", max_row["Timestamp"])
        print("People:", max_row["People"])
