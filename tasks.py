class TrafficTask:
    def __init__(self, mode="medium"):
        self.mode = mode

    def get_arrival_rate(self):
        if self.mode == "easy":
            return (0, 1)
        elif self.mode == "medium":
            return (0, 2)
        elif self.mode == "hard":
            return (1, 3)
        else:
            return (0, 2)