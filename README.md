# Foraging-RL-Dynamics

Multi-Timescale Exploration–Exploitation in Non-Stationary Foraging

A Dynamical Systems Approach to Decision Making

## 🧠 Scientific Scenario

In natural environments, animals constantly face a fundamental decision problem while foraging:

Should they stay and exploit a currently available food source, or leave and explore for a potentially better one?

This is known as the exploration–exploitation trade-off, but in real ecological settings the problem is more complex:

- Food sources (patches) deplete over time

- Moving to a new location has a travel cost

- The environment is non-stationary

- Decisions depend on the history of experienced rewards, not only the current reward

Behavioral studies across species (e.g., worms, fish, rodents, humans) show that animals do not make these decisions using instantaneous reward maximization. Instead, their decisions appear to arise from internal dynamic states that integrate reward history over time.

This project builds a computational model to demonstrate how:

A simple internal dynamical state can generate realistic patch-leaving decisions similar to those observed in animal foraging behavior.

### The model combines:

- A depleting foraging environment

- A decision agent with an internal dynamical variable

- A comparison with a simple Reinforcement Learning baseline

This approach is inspired by computational neuroscience models of natural decision making.

## 📁 Project Structure

```
foraging_rl_dynamics/
│
├── environment.py
├── agent_dynamics.py
├── agent_rl.py
├── run_experiment.py
├── analysis.py
└── requirements.txt
```

## 🔹 environment.py — Modeling a Depleting Food Patch

### Scientific Idea

This file models a foraging patch:

- Each time the agent stays, it receives a reward

- The reward decays over time (resource depletion)

- If the agent leaves, the patch resets

- Leaving incurs a travel cost

This recreates the exact structure used in animal foraging experiments.

### Key Mechanisms in Code

- self.current_reward *= self.decay
→ Models gradual depletion of the resource.

- leave() resets the patch and returns a negative reward
→ Introduces a realistic trade-off between staying and exploring.

This environment forces the agent into a genuine exploration–exploitation dilemma.

## 🔹 agent_dynamics.py — The Core Neuroscience Model

### Scientific Idea

Instead of choosing actions based only on current reward, the agent has an internal state:

x(t) 

This variable represents the agent’s motivation to remain in the patch and evolves over time depending on reward history.

Dynamical Update Rule

x \leftarrow x + \tau (r - x) 

#### This means:

- When rewards are high → internal state increases → agent stays

When rewards decline → internal state decreases → agent becomes likely to leave

This is similar to dynamical models used in computational neuroscience to describe decision variables in the brain.

### Decision Rule

- When the internal state drops below a threshold, the agent leaves the patch.

- The decision emerges from dynamics, not from a hard-coded rule.

This is the key contribution of the project.

## 🔹 run_experiment.py — Agent–Environment Interaction

### Scientific Idea

This file runs the full simulation loop:

1- The agent decides whether to stay or leave

2- The environment returns a reward

3- The agent updates its internal state

During the simulation, we record:

- Rewards over time

- Internal state evolution

- Agent decisions

These variables allow behavioral analysis of the decision process.

## 🔹 analysis.py — Behavioral Analysis

### Scientific Idea

In foraging studies, the main interest is not only total reward, but behavioral patterns such as:

- How long the agent stays in a patch

- How internal state evolves before leaving

- How reward history shapes decisions

This file plots:

- Reward over time

- Internal decision state over time

The plots reveal how patch-leaving behavior naturally emerges from the dynamical system.

## 🔹 agent_rl.py — Reinforcement Learning Baseline

### Scientific Idea

This file implements a very simple Q-learning agent.

Its purpose is not performance, but comparison:

A standard RL agent tries to maximize reward directly,
while the dynamical agent produces more natural, history-dependent behavior.

This highlights the importance of internal dynamics for modeling natural decisions.

## 🎯 Key Takeaway

This project demonstrates that:

- Patch-leaving decisions can arise from a simple internal dynamical variable

- Exploration–exploitation behavior can be modeled without complex RL

- Multi-timescale decisions emerge from reward integration over time

- The model resembles behavioral patterns observed in animal foraging studies

This aligns closely with computational neuroscience approaches to natural decision making.

---

## ▶️ How to Run the Project

1) Clone the repository

```
git clone <your-repo-url>
cd foraging_rl_dynamics
```

2) Create a virtual environment (recommended)

Linux / macOS

```
python3 -m venv venv
source venv/bin/activate

```

Windows

```
python -m venv venv
venv\Scripts\activate

```

3) Install dependencies

```
pip install -r requirements.txt

```

4) Run the simulation and see the behavioral plots

```
python analysis.py

```

This will:

Run a full foraging simulation

Execute the dynamical decision agent

Plot reward and internal state over time


The plot shows how the agent naturally decides when to leave the patch as rewards deplete.


---

(Optional) Run the raw simulation without plots

```
python run_experiment.py

```

This only runs the environment–agent interaction loop.
