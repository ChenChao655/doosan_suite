import os
import numpy as np
from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from envs.suite.models import assets_root


class Doosan(ManipulatorModel):
    """
    Panda is a sensitive single-arm robot designed by Franka.

    Args:
        idn (int or str): Number or some other unique identification string for this robot instance
    """
    def __init__(self, idn=0):
        full_path = os.path.join(assets_root, "robots/doosan/robot.xml")
        super().__init__(full_path, idn=idn)

    @property
    def default_mount(self):
        return "RethinkMount"

    @property
    def default_gripper(self):
        return "Rg6Gripper"

    @property
    def default_controller_config(self):
        return "osc_position"

    @property
    def init_qpos(self):
        return np.array([3.18982335, -0.5955753,  -1.24131643,  0.01710542, -1.30926468, -1.51545488])

    @property
    def base_xpos_offset(self):
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.16 - table_length / 2, 0.0, 0.0),
        }

    @property
    def top_offset(self):
        return np.array((0, 0, 2.0))

    @property
    def _horizontal_radius(self):
        return 0.5

    @property
    def arm_type(self):
        return "single"
