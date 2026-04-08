import os
from fastapi import FastAPI
from pydantic import BaseModel
from env import TrafficEnv

# -------- INIT --------
app = FastAPI()
env = TrafficEnv(mode="medium")

# -------- REQUEST MODEL --------
class Action(BaseModel):
    lane: int

# -------- BASELINE ACTION --------
def choose_action(state):
    return state["queue_lengths"].index(max(state["queue_lengths"]))

# -------- REQUIRED FUNCTION --------
def run_inference():
    output = ""

    for mode in ["easy", "medium", "hard"]:
        local_env = TrafficEnv(mode=mode)
        state = local_env.reset()

        output += f"[START] mode={mode}\n"

        total_reward = 0

        for step in range(20):
            action_lane = choose_action(state)

            state, reward, done, _ = local_env.step({"lane": action_lane})
            total_reward += reward

            output += f"[STEP] step={step}, action={action_lane}, reward={reward}\n"

            if done:
                break

        output += f"[END] mode={mode}, total_reward={total_reward}\n\n"

    return output

# -------- API ENDPOINTS --------

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step({"lane": action.lane})

    return {
        "state": state,
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }

# -------- HEALTH CHECK --------
@app.get("/")
def home():
    return {"message": "Traffic RL API running"}

# -------- PRINT FOR VALIDATOR --------
if __name__ == "__main__":
    result = run_inference()
    print(result, flush=True)