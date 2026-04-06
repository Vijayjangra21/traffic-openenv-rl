import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(8, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 4)
        )

    def forward(self, x):
        return self.net(x)


class RLAgent:
    def __init__(self, lr=0.001, epsilon=0.2):
        self.model = DQN()
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.loss_fn = nn.MSELoss()
        self.epsilon = epsilon

    def select_action(self, state):
        # epsilon-greedy
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, 4)

        state_tensor = torch.FloatTensor(state)
        q_values = self.model(state_tensor)

        return torch.argmax(q_values).item()

    def train_step(self, state, action, reward, next_state):
        state = torch.FloatTensor(state)
        next_state = torch.FloatTensor(next_state)

        q_values = self.model(state)
        next_q_values = self.model(next_state)

        target = q_values.clone().detach()
        target[action] = reward + 0.9 * torch.max(next_q_values)

        loss = self.loss_fn(q_values, target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()