from tasks import make_env
from baseline import BaselineAgent

tasks = ["easy", "medium", "hard"]

for task in tasks:
    env = make_env(task)
    agent = BaselineAgent()

    state = env.reset()
    total_reward = 0

    for _ in range(50):
        action = agent.select_action(state)
        state, reward, done, _ = env.step(action)
        total_reward += reward

    print(f"{task} → Total Reward: {total_reward}")