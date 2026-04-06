from tasks import make_env
from baseline import BaselineAgent

env = make_env("medium")
agent = BaselineAgent()

state = env.reset()

for step in range(10):
    action = agent.select_action(state)
    state, reward, done, _ = env.step(action)

    print(f"Step {step}")
    print("Action:", action)
    print("Reward:", reward)
    env.render()