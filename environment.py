import numpy as np

class Patch:
    def __init__(self, initial_reward=10.0, decay=0.9, travel_cost=2.0):
        self.initial_reward = initial_reward
        self.decay = decay
        self.travel_cost = travel_cost
        self.reset()

    def reset(self):
        self.current_reward = self.initial_reward

    def stay(self):
        reward = self.current_reward
        self.current_reward *= self.decay
        return reward

    def leave(self):
        self.reset()
        return -self.travel_cost