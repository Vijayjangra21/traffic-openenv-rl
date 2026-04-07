import os
from env import TrafficEnv

# Try importing OpenAI (optional)
try:
    from openai import OpenAI
    client = OpenAI(
        api_key=os.getenv("HF_TOKEN"),
        base_url=os.getenv("API_BASE_URL"),
    )
    MODEL_NAME = os.getenv("MODEL_NAME") or "gpt-4o-mini"
    USE_API = True
except:
    USE_API = False


def choose_action(state):
    # Try OpenAI (if key exists)
    if USE_API and os.getenv("HF_TOKEN"):
        try:
            prompt = f"""
State:
queue_lengths: {state['queue_lengths']}
waiting_times: {state['waiting_times']}

Choose best lane (0-3). Return only number.
"""

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
            )

            content = response.choices[0].message.content
            if content:
                lane = int(content.strip())
                return max(0, min(3, lane))
        except:
            pass

    # ✅ FREE fallback (baseline logic)
    return state["queue_lengths"].index(max(state["queue_lengths"]))


def run_task(mode):
    env = TrafficEnv(mode=mode)
    state = env.reset()

    print(f"[START] mode={mode}")

    total_reward = 0

    for step in range(20):
        action_lane = choose_action(state)
        action = {"lane": action_lane}

        state, reward, done, _ = env.step(action)
        total_reward += reward

        print(f"[STEP] step={step}, action={action_lane}, reward={reward}")

        if done:
            break

    print(f"[END] mode={mode}, total_reward={total_reward}\n")


if __name__ == "__main__":
    for mode in ["easy", "medium", "hard"]:
        run_task(mode)