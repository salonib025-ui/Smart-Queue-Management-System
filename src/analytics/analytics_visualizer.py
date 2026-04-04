import pandas as pd
import matplotlib.pyplot as plt


class AnalyticsVisualizer:

    def __init__(self):
        # File where data is stored
        self.file = "queue_data.csv"

    def load_data(self):
        try:
            return pd.read_csv(self.file)
        except FileNotFoundError:
            print("No data file found. Run the system first!")
            return None

    def plot_people_trend(self):
        data = self.load_data()
        if data is None:
            return

        plt.figure()
        plt.plot(data["People"])
        plt.title("People Count Over Time")
        plt.xlabel("Time Index")
        plt.ylabel("Number of People")
        plt.grid()

        plt.show()

    def plot_waiting_time(self):
        data = self.load_data()
        if data is None:
            return

        plt.figure()
        plt.plot(data["Waiting"])
        plt.title("Waiting Time Over Time")
        plt.xlabel("Time Index")
        plt.ylabel("Waiting Time (mins)")
        plt.grid()

        plt.show()

    def peak_time(self):
        data = self.load_data()
        if data is None:
            return

        max_people = data["People"].max()
        peak_row = data[data["People"] == max_people]

        print("\n🔥 Peak Time Analysis")
        print("Max People:", max_people)
        print("At Time:", peak_row["Timestamp"].values[0])
