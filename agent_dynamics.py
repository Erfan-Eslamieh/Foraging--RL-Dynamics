class DynamicalAgent:
    def __init__(self, tau=0.3, threshold=3.0):
        self.tau = tau
        self.threshold = threshold
        self.x = 0.0  # internal state

    def update(self, reward):
        # Dynamical update rule
        self.x += self.tau * (reward - self.x)

    def decide(self):
        if self.x < self.threshold:
            return "leave"
        return "stay"