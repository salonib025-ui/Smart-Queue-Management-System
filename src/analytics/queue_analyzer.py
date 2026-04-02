class QueueAnalyzer:

    def __init__(self):
        self.history = []

    def update(self, people_count):

        # Store recent counts
        self.history.append(people_count)

        # Keep only last 30 values
        if len(self.history) > 30:
            self.history.pop(0)

        return self.analyze_queue()

    def analyze_queue(self):

        if len(self.history) < 5:
            return "Analyzing..."

        avg = sum(self.history) / len(self.history)

        if avg <= 3:
            return "Short Queue"

        elif avg <= 7:
            return "Moderate Queue"

        else:
            return "Long Queue"
