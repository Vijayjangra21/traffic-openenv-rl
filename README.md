# 🚦 Adaptive Traffic Signal Control (OpenEnv RL Environment)

👉 **Live Demo:**  
https://huggingface.co/spaces/Vijay212002/traffic-openenv-rl-final

---

## 📌 Overview

This project implements an **OpenEnv-compliant reinforcement learning environment** for adaptive traffic signal control.

The system simulates a traffic intersection where an agent dynamically selects which lane receives a green signal to minimize congestion and waiting time.

Designed for **reproducible evaluation and scalable deployment**, the project includes environment design, baseline, evaluation, inference, and deployment.

---

## 🎯 Problem Statement

Traditional traffic signals operate on fixed timing schedules, leading to:

- Inefficient traffic flow  
- Increased waiting times  
- Poor adaptability to real-time conditions  

This project enables an AI agent to **adaptively manage traffic signals**.

---

## 🧠 Key Features

- ✅ OpenEnv-compliant API (`reset`, `step`)
- ✅ 4-lane traffic simulation
- ✅ 3 difficulty levels (easy, medium, hard)
- ✅ Baseline decision policy
- ✅ Deterministic evaluation
- ✅ Structured inference logs (`[START]`, `[STEP]`, `[END]`)
- ✅ FastAPI backend deployment
- ✅ Docker support

---

## ⚙️ Environment Design

### 📊 State

```python
{
  "queue_lengths": [l1, l2, l3, l4],
  "waiting_times": [w1, w2, w3, w4]
}


---

🎮 Action

{"lane": 0-3}


---

🎯 Reward Function

reward = - (total_queue_length + total_waiting_time)

Penalizes congestion

Encourages efficient traffic flow



---

🧪 Tasks

Mode	Description

Easy	Low traffic
Medium	Moderate traffic
Hard	High congestion



---

🧠 Baseline Strategy

lane = argmax(queue_lengths)


---

⚖️ Evaluation

score = baseline_wait / agent_wait
score = min(score, 1.0)

📌 Scores are normalized relative to baseline.


---

📊 Sample Results

Mode	Score

Easy	1.00
Medium	0.54
Hard	0.42



---

🚀 Inference (OpenEnv Evaluation)

Run:

python -c "from inference import run_inference; print(run_inference())"

Output Format

[START]
[STEP]
[END]


---

🔐 Optional Environment Variables

API_BASE_URL
MODEL_NAME
HF_TOKEN


---

🐳 Docker

docker build -t traffic_env .
docker run traffic_env


---

📁 Project Structure

traffic-openenv-rl/
│── env.py
│── tasks.py
│── baseline.py
│── grader.py
│── agent.py
│── models.py
│── openenv.yaml
│── inference.py
│── app.py
│── server/
│     └── app.py
│── requirements.txt
│── Dockerfile
│── pyproject.toml
│── uv.lock
│── README.md


---

🌍 OpenEnv Compliance

reset() → initialize environment

step(action) → state transition + reward

run_inference() → evaluation entry

Deterministic and reproducible



---

💡 Use Case

Efficient allocation of traffic signals across competing lanes under dynamic conditions.


---

🚀 Future Improvements

Multi-intersection systems

Real-time traffic integration

Advanced RL algorithms



---

🏁 Conclusion

This project demonstrates:

Environment design

Baseline strategy

Evaluation pipeline

Deployment with FastAPI and Docker



---

🔑 Keywords

Reinforcement Learning, OpenEnv, Traffic Control, Simulation