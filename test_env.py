from env import TrafficEnv
from baseline import baseline

env = TrafficEnv(mode="hard")
state = env.reset()

for step in range(10):
    action = baseline(state)
    state, reward, done, _ = env.step(action)

    print(f"Step {step}")
    print("Action:", action)
    print("State:", state)
    print("Reward:", reward)
    print("-" * 30)