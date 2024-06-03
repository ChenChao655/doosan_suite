import robosuite.models.grippers as grippers
from .rg6_gripper import Rg6Gripper


grippers.GRIPPER_MAPPING["Rg6Gripper"] = Rg6Gripper

grippers.ALL_GRIPPERS = grippers.GRIPPER_MAPPING.keys()


