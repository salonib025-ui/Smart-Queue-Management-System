class QueueAnalyzer:

    def analyze(self, people_count):

        if people_count == 0:
            return "No Queue"
        elif people_count <= 3:
            return "Short"
        elif people_count <= 6:
            return "Moderate"
        else:
            return "Long"