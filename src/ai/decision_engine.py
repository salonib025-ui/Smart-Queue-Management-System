class DecisionEngine:

    def __init__(self):
        print("AI Decision Engine Initialized")

    def make_decision(self, people_count, queue_status, waiting_time):

        if people_count == 0:
            return "Idle"

        elif queue_status == "Short Queue":
            return "Normal Operations"

        elif queue_status == "Moderate Queue":
            return "Prepare Extra Counter"

        elif queue_status == "Long Queue":
            return "Open New Counter"

        if waiting_time > 10:
            return "High Waiting Time Alert"

        return "Monitoring"