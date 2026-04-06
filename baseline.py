import numpy as np


class BaselineAgent:
    def select_action(self, state):
        queue_lengths = state[:4]

        # pick lane with max queue
        action = np.argmax(queue_lengths)

        return action