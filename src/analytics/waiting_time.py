class WaitingTimeEstimator:

    def __init__(self, service_rate=0.5):
        self.service_rate = service_rate

    def estimate(self, people_count):

<<<<<<< HEAD
        return people_count * 2
=======
        if people_count == 0:
            return 0

        return round(people_count / self.service_rate, 2)
>>>>>>> 4ad1d51ca5fc7882d79953ababdad8a15a44ef2e
