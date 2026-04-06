from env import TrafficEnv

env = TrafficEnv()

state = env.reset()

for step in range(10):
    action = step % 4  # simple rotation

    state, reward, done, _ = env.step(action)

    print(f"Step {step}")
    print("State:", state)
    print("Reward:", reward)
    env.render()