"""
Gripper for Franka's Panda (has two fingers).
"""
import os
import numpy as np
from robosuite.models.grippers.gripper_model import GripperModel
from ... import assets_root


class Rg6Gripper(GripperModel):
    """
    Modifies PandaGripperBase to only take one action.
    """
    def __init__(self, idn=0):
        full_path = os.path.join(assets_root, "grippers/rg6_gripper.xml")
        super().__init__(full_path, idn=idn)

    def format_action(self, action):
        """
        Maps continuous action into binary output
        -1 => open, 1 => closed

        Args:
            action (np.array): gripper-specific action

        Raises:
            AssertionError: [Invalid action dimension size]
        """
        assert len(action) == self.dof
        self.current_action = np.clip(
            self.current_action + np.array([1.0]) * self.speed * np.sign(action), -0.5, 0.5
        )
        return self.current_action

    @property
    def init_qpos(self):
        return np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    @property
    def _important_geoms(self):
        return {
            "left_finger": ["finger1_outer_knuckle_collision", "finger1_inner_finger_collision"],
            "right_finger": ["finger2_outer_knuckle_collision", "finger2_inner_finger_collision"],
            "left_fingerpad": ["finger1_inner_knuckle_collision vis"],
            "right_fingerpad": ["finger2_inner_knuckle_collision"],
        }

    @property
    def speed(self):
        return 0.003

    @property
    def dof(self):
        return 1
