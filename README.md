# Doosan robot for Robosuite
The project contains codes of Doosan robot and works as a supplementary for Robosuite RL environment.

## How to use
1. Our codes depend on Robosuite RL environment. So, in order to use it, Please install robosuite firstly.
```
pip install robosuite
```

2. Then you can use it as below, then the Doosan robot and RG6 gripper will be registered.
```
import robosuite
from doosan_suite import *

# create environment instance
env = suite.make(
    env_name="Lift", # try with other tasks like "Stack" and "Door"
    robots="Doosan",  # try with other robots like "Sawyer" and "Jaco"
    has_renderer=True,
    has_offscreen_renderer=False,
    use_camera_obs=False,
)

# reset the environment
env.reset()

for i in range(1000):
    action = np.random.randn(env.robots[0].dof) # sample random action
    obs, reward, done, info = env.step(action)  # take action in the environment
    env.render()  # render on display
```
  