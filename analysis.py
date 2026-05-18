import matplotlib.pyplot as plt
from run_experiment import run_episode

rewards, states, actions = run_episode()

plt.figure(figsize=(10,5))
plt.plot(rewards, label="Reward")
plt.plot(states, label="Internal State x")
plt.legend()
plt.title("Foraging with Dynamical Decision Agent")
plt.show()