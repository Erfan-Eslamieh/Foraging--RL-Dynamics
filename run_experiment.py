from environment import Patch
from agent_dynamics import DynamicalAgent

def run_episode(steps=100):
    patch = Patch(initial_reward=10, decay=0.85, travel_cost=2)
    agent = DynamicalAgent(tau=0.25, threshold=3)

    rewards = []
    states = []
    actions = []

    for t in range(steps):
        action = agent.decide()

        if action == "stay":
            r = patch.stay()
        else:
            r = patch.leave()

        agent.update(r)

        rewards.append(r)
        states.append(agent.x)
        actions.append(action)

    return rewards, states, actions


if __name__ == "__main__":
    rewards, states, actions = run_episode()
    print("Simulation finished.")