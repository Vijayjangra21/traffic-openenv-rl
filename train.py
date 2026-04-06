from tasks import make_env
from agent import RLAgent

env = make_env("medium")
agent = RLAgent()

episodes = 200

for ep in range(episodes):
    state = env.reset()
    total_reward = 0

    for step in range(50):
        action = agent.select_action(state)
        next_state, reward, done, _ = env.step(action)

        agent.train_step(state, action, reward, next_state)

        state = next_state
        total_reward += reward

    print(f"Episode {ep}: Reward = {total_reward}")