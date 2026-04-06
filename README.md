# 🚦 Adaptive Traffic Signal Control (OpenEnv RL Environment)

## 📌 Overview

This project implements an **OpenEnv-compliant reinforcement learning environment** for adaptive traffic signal control. The environment simulates a real-world traffic intersection where an agent learns to dynamically manage signal timing to reduce congestion.

The system is designed as a **decision-making environment** where an AI agent interacts through `reset()`, `step()`, and `state()` APIs and improves performance through reward feedback.

---

## 🎯 Problem Statement

Traditional traffic signals operate on fixed timing, leading to:

- Inefficient traffic flow  
- Increased waiting times  
- Poor adaptability to changing conditions  

This project addresses the problem by enabling an AI agent to **learn optimal signal control strategies dynamically**.

---

## 🧠 Key Features

- ✅ OpenEnv-style environment (`reset`, `step`, `state`)
- ✅ Real-world simulation (traffic intersection)
- ✅ 3 Tasks: Easy, Medium, Hard
- ✅ Deterministic grading system (0.0 – 1.0 score)
- ✅ Baseline comparison (heuristic policy)
- ✅ Reinforcement learning agent support
- ✅ Docker-ready for deployment

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

Agent selects which lane receives the green signal.

---

### 🎯 Reward Function

```python
reward = - total_wait_time - 0.5 * max_wait_time
```

* Penalizes congestion
* Encourages fairness
* Provides continuous learning signal

---

## 🧪 Tasks (Difficulty Levels)

### 🟢 Easy

* Low, uniform traffic
* Stable conditions

### 🟡 Medium

* Random traffic spikes
* Uneven lane distribution

### 🔴 Hard

* High congestion
* Extreme imbalance

---

## ⚖️ Evaluation & Grading

Performance is measured using a deterministic scoring system:

```python
score = baseline_wait_time / agent_wait_time
score = min(score, 1.0)
```

* Score range: **0.0 – 1.0**
* Higher score = better performance

---

## 🤖 Baseline Agent

A simple heuristic baseline is used:

```python
select lane with maximum queue
```

Used for:

* Performance comparison
* Score normalization

---

## 🚀 How to Run

### 🔧 Install dependencies

```bash
pip install -r requirements.txt
```

---

### ▶️ Run baseline evaluation

```bash
python run_baseline.py
```

---

### ▶️ Train RL agent (after adding agent)

```bash
python train.py
```

---

## 📁 Project Structure

```text
traffic-openenv-rl/
│── env.py
│── tasks.py
│── grader.py
│── run_baseline.py
│── agent.py
│── train.py
│── openenv.yaml
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## 🐳 Docker Support

```bash
docker build -t traffic_env .
docker run traffic_env
```

---

## 🌍 OpenEnv Compliance

This project follows OpenEnv standards:

* `reset()` → returns initial state
* `step(action)` → returns next state, reward
* `state()` → returns current state
* Structured tasks and grading
* Reproducible evaluation

---

## 💡 Use Case

This environment models a **real-world resource allocation problem**, where limited green signal time must be optimally distributed across competing lanes under dynamic conditions.

---

## 🚀 Future Improvements

* Multi-intersection coordination
* Real-time video (YOLO integration)
* Advanced RL algorithms (DQN, PPO)
* Smart city deployment

---

## 🏆 Conclusion

This project demonstrates how reinforcement learning can be applied to real-world traffic optimization problems. The environment provides a structured and scalable platform for training intelligent agents in dynamic decision-making scenarios.

---

## 🔑 Keywords

Reinforcement Learning, OpenEnv, Traffic Control, Simulation, AI Systems, Optimization

```

