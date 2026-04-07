# 🚦 Adaptive Traffic Signal Control (OpenEnv RL Environment)

## 📌 Overview

This project implements an **OpenEnv-compliant reinforcement learning environment** for adaptive traffic signal control.

The system simulates a traffic intersection where an RL agent dynamically selects which lane receives a green signal, with the goal of reducing congestion and waiting time.

It provides a **complete pipeline** including environment design, baseline, training, evaluation, inference, and Docker deployment.

---

## 🎯 Problem Statement

Traditional traffic signals operate on fixed timing schedules, leading to:

- Inefficient traffic flow  
- Increased waiting times  
- Poor adaptability to real-time conditions  

This project enables an AI agent to **learn optimal signal control strategies dynamically**.

---

## 🧠 Key Features

- ✅ OpenEnv-compliant API (`reset`, `step`, `state`)
- ✅ Realistic 4-lane traffic simulation
- ✅ 3 difficulty levels (easy, medium, hard)
- ✅ DQN-based RL agent
- ✅ Baseline comparison
- ✅ Deterministic grading system (0–1 score)
- ✅ Fully Dockerized (reproducible execution)
- ✅ Inference script with structured logs

---

## ⚙️ Environment Design

### 📊 State (Observation)

```python
{
  "queue_lengths": [l1, l2, l3, l4],
  "waiting_times": [w1, w2, w3, w4]
}
````

---

### 🎮 Action

```python
{"lane": 0-3}
```

---

### 🎯 Reward Function

```python
reward = - (total_queue_length + total_waiting_time)
```

* Penalizes congestion
* Encourages efficient traffic flow
* Provides continuous learning signal

---

## 🧪 Tasks

| Mode   | Description                      |
| ------ | -------------------------------- |
| Easy   | Low traffic, stable conditions   |
| Medium | Moderate traffic with randomness |
| Hard   | High congestion and imbalance    |

---

## 🤖 Approach

* Deep Q-Network (DQN) using PyTorch
* Input: 8-dimensional state
* Output: 4 actions (lanes)
* Epsilon-greedy exploration
* Trained with fixed seeds for reproducibility

---

## ⚖️ Evaluation

```python
score = baseline_wait / agent_wait
score = min(score, 1.0)
```

---

## 🧠 Baseline

```python
select lane with maximum queue length
```

---

## 📊 Results

| Mode   | Score |
| ------ | ----- |
| Easy   | 1.00  |
| Medium | 0.54  |
| Hard   | 0.42  |

### Observations

* Agent learns to prioritize congested lanes
* Outperforms baseline in medium and hard scenarios
* Demonstrates adaptive decision-making
* Performance improves significantly over baseline in non-trivial scenarios

---

## 🚀 How to Run

### 🔧 Install dependencies

```bash
pip install -r requirements.txt
```

---

### ▶️ Train the agent

```bash
python train.py
```

---

### ▶️ Run baseline evaluation

```bash
python run_baseline.py
```

---

## 🚀 Inference (OpenEnv Evaluation)

```bash
python inference.py
```

### Output format

```
[START]
[STEP]
[END]
```

---

## 🔐 Environment Variables

Set before running inference:

```bash
API_BASE_URL
MODEL_NAME
HF_TOKEN
```

---

## 🐳 Docker

```bash
docker build -t traffic_env .
docker run traffic_env
```

---

## 📁 Project Structure

```
traffic-openenv-rl/
│── env.py
│── tasks.py
│── baseline.py
│── grader.py
│── agent.py
│── train.py
│── run_baseline.py
│── models.py
│── openenv.yaml
│── inference.py
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## 🌍 OpenEnv Compliance

* `reset()` → initialize environment
* `step(action)` → returns next state and reward
* `state()` → returns current state
* Tasks with deterministic graders
* Reproducible evaluation

---

## 💡 Use Case

This environment models a **real-world resource allocation problem**, where limited signal time must be distributed across competing traffic lanes under dynamic conditions.

---

## 🚀 Future Improvements

* Multi-intersection coordination
* YOLO-based real-time traffic input
* Advanced RL methods (Replay Buffer, PPO)

---

## 🏆 Conclusion

This project demonstrates a complete RL system for traffic optimization, including environment design, training, evaluation, and deployment.

It highlights how **well-structured environments and evaluation pipelines are critical for building effective AI systems**.

---

## 🔑 Keywords

Reinforcement Learning, OpenEnv, Traffic Optimization, Simulation, AI Systems
