import numpy as np


class TrafficEnv:
    def __init__(self, arrival_rate=0.3, max_queue=50):
        self.arrival_rate = arrival_rate
        self.max_queue = max_queue
        self.num_lanes = 4
        self.reset()

    def reset(self):
        self.queue_lengths = np.zeros(self.num_lanes, dtype=int)
        self.waiting_times = np.zeros(self.num_lanes, dtype=int)
        self.time_step = 0
        return self.get_state()

    def step(self, action):
        assert 0 <= action < self.num_lanes

        self.time_step += 1

        # 🚦 Serve cars
        cars_passed = min(5, self.queue_lengths[action])
        self.queue_lengths[action] -= cars_passed

        # ⏳ Update waiting
        for i in range(self.num_lanes):
            if i == action:
                self.waiting_times[i] = 0
            else:
                if self.queue_lengths[i] > 0:
                    self.waiting_times[i] += 1

        # 🚗 New cars arrive
        for i in range(self.num_lanes):
            if np.random.rand() < self.arrival_rate:
                self.queue_lengths[i] = min(
                    self.queue_lengths[i] + 1, self.max_queue
                )

        # 🎯 Reward
        reward = -np.sum(self.waiting_times)

        return self.get_state(), reward, False, {}

    def get_state(self):
        return np.concatenate([self.queue_lengths, self.waiting_times])

    def render(self):
        print("Queues:", self.queue_lengths)
        print("Waiting:", self.waiting_times)
        print("-" * 30)