import os
from env import TrafficEnv

# -------- REQUIRED ENV VARIABLES --------
API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

# -------- SAFE OPENAI SETUP --------
USE_API = False
client = None

try:
    from openai import OpenAI

    if HF_TOKEN:
        client = OpenAI(
            api_key=HF_TOKEN,
            base_url=API_BASE_URL if API_BASE_URL else None,
        )
        USE_API = True

except Exception as e:
    print("OpenAI init failed:", e)


# -------- ACTION SELECTION --------
def choose_action(state):
    if USE_API and client:
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

            content = response.choices[0].message.content.strip()
            lane = int(content)

            return max(0, min(3, lane))

        except Exception as e:
            print("API failed, using fallback:", e)

    # ✅ fallback
    return state["queue_lengths"].index(max(state["queue_lengths"]))


# -------- RUN SINGLE TASK --------
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

    print(f"[END] mode={mode}, total_reward={total_reward}")


# -------- MAIN INFERENCE FUNCTION --------
def run_inference():
    for mode in ["easy", "medium", "hard"]:
        run_task(mode)


# -------- ENTRY POINT --------
if __name__ == "__main__":
    run_inference()