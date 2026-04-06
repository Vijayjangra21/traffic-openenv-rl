from env import TrafficEnv
from baseline import baseline
from agent import Agent

def run_episode(policy, mode="medium", steps=50):
    env = TrafficEnv(mode=mode)
    state = env.reset()

    total_wait = 0

    for _ in range(steps):
        action = policy(state)
        state, reward, done, _ = env.step(action)

        total_wait += sum(state["waiting_times"])

    return total_wait


def grade(agent_policy, mode="medium"):
    baseline_wait = run_episode(baseline, mode)
    agent_wait = run_episode(agent_policy, mode)

    # avoid division error
    if agent_wait == 0:
        return 1.0

    score = baseline_wait / agent_wait
    score = min(score, 1.0)

    return score

if __name__ == "__main__":
    from baseline import baseline

    score = grade(baseline, mode="medium")
    print("Baseline score:", score)