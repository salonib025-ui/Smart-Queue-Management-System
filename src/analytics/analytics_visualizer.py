import pandas as pd
import matplotlib.pyplot as plt
plt.ion()


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
        plt.plot(data["People_Count"])
        plt.title("People Count Over Time")
       
        plt.xlabel("Time Index")
        plt.ylabel("Number of People")
        plt.grid()

        plt.show(block=True)

    def plot_waiting_time(self):
        data = self.load_data()
        if data is None:
            return

        plt.figure()
        plt.plot(data["Waiting_Time"])
        plt.title("Waiting Time Over Time")
        plt.xlabel("Time Index")
        plt.ylabel("Waiting Time (mins)")
        plt.grid()

        plt.show(block=True)

    def peak_time(self):
        data = self.load_data()
        if data is None:
            return

        max_people = data["People_Count"].max()
        peak_row = data[data["People_Count"] == max_people]

        print("\n🔥 Peak Time Analysis")
        print("Max People:", max_people)
        print("At Time:", peak_row["Timestamp"].values[0])
