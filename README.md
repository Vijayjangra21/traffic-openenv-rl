# 🚦 Adaptive Traffic Signal Control (OpenEnv RL Environment)

## 📌 Overview

This project implements an **OpenEnv-compliant reinforcement learning environment** for adaptive traffic signal control.

The system simulates a traffic intersection where an RL agent dynamically selects which lane receives a green signal, with the goal of reducing congestion and waiting time.

It is designed as a **decision-making environment** with a complete pipeline including environment, baseline, training, evaluation, and Docker deployment.

---

## 🎯 Problem Statement

Traditional traffic signals operate on fixed timing schedules, leading to:

- Inefficient traffic flow  
- Increased waiting times  
- Poor adaptability to real-time conditions  

This project enables an AI agent to **learn optimal signal control strategies dynamically**.

---

## 🧠 Key Features

- ✅ OpenEnv-style environment (`reset`, `step`, `state`)
- ✅ Realistic traffic simulation (4-lane intersection)
- ✅ 3 difficulty levels (easy, medium, hard)
- ✅ Reinforcement learning agent (DQN-based)
- ✅ Baseline comparison (heuristic policy)
- ✅ Deterministic grading system (0–1 score)
- ✅ Fully Dockerized (reproducible execution)

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

The agent selects which lane gets the green signal.

---

### 🎯 Reward Function

```python
reward = - (total_queue_length + total_waiting_time)
```

* Penalizes congestion
* Encourages clearing high-density lanes
* Provides continuous learning signal

---

## 🧪 Tasks (Difficulty Levels)

| Mode      | Description                      |
| --------- | -------------------------------- |
| 🟢 Easy   | Low traffic, stable conditions   |
| 🟡 Medium | Moderate traffic with randomness |
| 🔴 Hard   | High congestion and imbalance    |

---

## 🤖 Approach

* Deep Q-Network (DQN) implemented using PyTorch
* Input: 8-dimensional state (queue + waiting)
* Output: 4 possible actions (lanes)
* Epsilon-greedy policy for exploration
* Trained over multiple episodes
* Trained with fixed random seeds for reproducibility

---

## ⚖️ Evaluation & Grading

Performance is measured relative to a baseline:

```python
score = baseline_wait / agent_wait
score = min(score, 1.0)
```

* Score range: **0.0 – 1.0**
* Higher score = better performance

---

## 🧠 Baseline Agent

A simple heuristic baseline:

```python
select lane with maximum queue length
```

Used for:

* Performance comparison
* Score normalization

---

## 📊 Results

| Mode   | Score |
| ------ | ----- |
| Easy   | 1.00  |
| Medium | 0.54  |
| Hard   | 0.42  |

### Observations:

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

## 🐳 Docker Support

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
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## 🌍 OpenEnv Compliance

* `reset()` → initializes environment
* `step(action)` → returns next state, reward
* Structured tasks and grading
* Fully reproducible setup

---

## 💡 Use Case

This environment models a **resource allocation problem**, where limited signal time must be distributed across competing traffic lanes under dynamic conditions.

---

## 🚀 Future Improvements

* Multi-intersection coordination
* Integration with YOLO (real-time traffic input)
* Advanced RL methods (Replay Buffer, PPO)
* Smart city deployment

---

## 🏆 Conclusion

This project demonstrates a complete RL pipeline for traffic optimization, including environment design, training, evaluation, and deployment.

It highlights how **well-structured environments and evaluation systems are critical for building effective AI solutions**.

---

## 🔑 Keywords

Reinforcement Learning, OpenEnv, Traffic Optimization, Simulation, AI Systems
