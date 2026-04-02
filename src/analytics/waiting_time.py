class WaitingTimeEstimator:

    def __init__(self, service_rate=0.5):
        self.service_rate = service_rate

    def estimate(self, people_count):
        if people_count == 0:
            return 0
        return round(people_count / self.service_rate, 2)