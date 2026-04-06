import numpy as np
from tasks import make_env
from baseline import BaselineAgent


class RandomAgent:
    def select_action(self, state):
        return np.random.randint(0, 4)


def run_episode(env, agent, steps=50):
    state = env.reset()
    total_wait = 0

    for _ in range(steps):
        action = agent.select_action(state)
        state, reward, done, _ = env.step(action)

        # waiting is negative reward
        total_wait += -reward

    return total_wait


def evaluate():
    tasks = ["easy", "medium", "hard"]

    baseline_agent = BaselineAgent()
    random_agent = RandomAgent()

    for task in tasks:
        env = make_env(task)

        baseline_wait = run_episode(env, baseline_agent)
        random_wait = run_episode(env, random_agent)

        score = random_wait / baseline_wait if baseline_wait > 0 else 1.0
        score = min(score, 1.0)

        print(f"\nTask: {task}")
        print(f"Baseline Wait: {baseline_wait}")
        print(f"Random Wait: {random_wait}")
        print(f"Score: {score:.2f}")