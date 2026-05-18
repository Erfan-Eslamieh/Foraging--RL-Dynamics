import numpy as np
import random

class QLearningAgent:
    def __init__(self):
        self.q = {"stay": 0.0, "leave": 0.0}
        self.lr = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def decide(self):
        if random.random() < self.epsilon:
            return random.choice(["stay", "leave"])
        return max(self.q, key=self.q.get)

    def update(self, action, reward):
        self.q[action] += self.lr * (reward + self.gamma * max(self.q.values()) - self.q[action])