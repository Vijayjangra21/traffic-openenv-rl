import torch
import torch.nn as nn
import torch.optim as optim
import random


class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(8, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 4)
        )

    def forward(self, x):
        return self.model(x)


class Agent:
    def __init__(self):
        self.model = DQN()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.loss_fn = nn.MSELoss()

        self.epsilon = 1.0
        self.epsilon_decay = 0.98
        self.epsilon_min = 0.01

    def state_to_tensor(self, state):
        data = state["queue_lengths"] + state["waiting_times"]
        return torch.tensor(data, dtype=torch.float32)

    def select_action(self, state):
        if random.random() < self.epsilon:
            return {"lane": random.randint(0, 3)}

        state_tensor = self.state_to_tensor(state)
        q_values = self.model(state_tensor)
        action = torch.argmax(q_values).item()

        return {"lane": action}

    def train_step(self, state, action, reward, next_state):
        state_tensor = self.state_to_tensor(state)
        next_state_tensor = self.state_to_tensor(next_state)

        q_values = self.model(state_tensor)
        next_q_values = self.model(next_state_tensor)

        target = q_values.clone().detach()
        action_idx = action["lane"]

        target[action_idx] = reward + 0.9 * torch.max(next_q_values)

        loss = self.loss_fn(q_values, target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # decay epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

if __name__ == "__main__":
    agent = Agent()
    dummy_state = {
        "queue_lengths": [1, 2, 3, 4],
        "waiting_times": [0, 1, 2, 3]
    }

    action = agent.select_action(dummy_state)
    print("Action:", action)