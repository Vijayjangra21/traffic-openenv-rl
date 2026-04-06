from env import TrafficEnv
from agent import Agent
from grader import grade
import random
import numpy as np
import torch

random.seed(42)
np.random.seed(42)
torch.manual_seed(42)

def train():
    env = TrafficEnv(mode="medium")
    agent = Agent()

    episodes = 600

    print("Starting training...\n")

    for episode in range(episodes):
        state = env.reset()
        total_reward = 0

        for step in range(50):
            action = agent.select_action(state)
            next_state, reward, done, _ = env.step(action)

            agent.train_step(state, action, reward, next_state)

            state = next_state
            total_reward += reward

        if episode % 20 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward:.2f}")

    print("\nTraining completed!")

    # 🔥 Evaluate trained agent
    print("\nEvaluating trained agent...")

    for mode in ["easy", "medium", "hard"]:
        score = grade(agent.select_action, mode=mode)
        print(f"Mode: {mode}, Agent Score: {score:.3f}")


if __name__ == "__main__":
    train()