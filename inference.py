import os
from env import TrafficEnv
from openai import OpenAI

# -------- INIT LLM CLIENT --------
client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY"),
)

# -------- BASELINE FALLBACK --------
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

            # -------- LLM CALL --------
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a traffic signal controller. Return ONLY a number between 0 and 3."
                        },
                        {
                            "role": "user",
                            "content": f"Queue lengths: {state['queue_lengths']}"
                        }
                    ],
                )

                action_lane = int(response.choices[0].message.content.strip())

                if action_lane not in [0, 1, 2, 3]:
                    action_lane = choose_action(state)

            except Exception:
                # fallback if API fails
                action_lane = choose_action(state)

            # -------- STEP --------
            state, reward, done, _ = env.step({"lane": action_lane})
            total_reward += reward

            print(
                f"[STEP] step={step}, action={action_lane}, reward={reward}",
                flush=True
            )

            if done:
                break

        # normalize score
        score = max(0, min(1, -total_reward / 100))

        print(
            f"[END] task={task} score={score:.2f} steps={steps}",
            flush=True
        )


# -------- ENTRY POINT --------
if __name__ == "__main__":
    run_inference()