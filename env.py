import random
from tasks import TrafficTask


class TrafficEnv:
    def __init__(self, mode="medium"):
        self.task = TrafficTask(mode)
        self.num_lanes = 4
        self.queue_lengths = [0] * 4
        self.waiting_times = [0] * 4

    def reset(self):
        self.queue_lengths = [0] * 4
        self.waiting_times = [0] * 4
        return self.get_state()

    def get_state(self):
        return {
            "queue_lengths": self.queue_lengths,
            "waiting_times": self.waiting_times
        }

    def step(self, action):
        lane = action["lane"]

        # Safety check (important)
        if lane < 0 or lane >= self.num_lanes:
            raise ValueError("Invalid lane selected")

        # Cars pass in selected lane
        passed = min(3, self.queue_lengths[lane])
        self.queue_lengths[lane] -= passed
        self.waiting_times[lane] = 0

        # Other lanes wait
        for i in range(self.num_lanes):
            if i != lane:
                self.waiting_times[i] += 1

        # New cars arrive (based on task difficulty)
        low, high = self.task.get_arrival_rate()
        for i in range(self.num_lanes):
            self.queue_lengths[i] += random.randint(low, high)

        # Reward (minimize congestion + waiting)
        total_cars = sum(self.queue_lengths)
        total_wait = sum(self.waiting_times)
        reward = - (total_cars + total_wait)

        return self.get_state(), reward, False, {}
    def state(self):
        return self.get_state()