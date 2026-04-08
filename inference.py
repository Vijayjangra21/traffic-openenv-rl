from env import TrafficEnv

# -------- BASELINE ACTION --------
def choose_action(state):
    return state["queue_lengths"].index(max(state["queue_lengths"]))


# -------- MAIN INFERENCE --------
def run_inference():
    tasks = ["easy", "medium", "hard"]

    for task in tasks:
        env = TrafficEnv(mode=task)
        state = env.reset()

        print(f"[START] task={task}", flush=True)

        total_reward = 0
        steps = 20

        for step in range(steps):
            action_lane = choose_action(state)

            state, reward, done, _ = env.step({"lane": action_lane})
            total_reward += reward

            print(
                f"[STEP] step={step}, action={action_lane}, reward={reward}",
                flush=True
            )

            if done:
                break

        # normalize score between 0 and 1
        score = max(0, min(1, -total_reward / 100))

        print(
            f"[END] task={task} score={score:.2f} steps={steps}",
            flush=True
        )


# -------- SINGLE ENTRY POINT (CRITICAL) --------
if __name__ == "__main__":
    run_inference()