import robosuite.robots as robots
from robosuite.robots.single_arm import SingleArm
from robosuite.robots.bimanual import Bimanual

robots.ROBOT_CLASS_MAPPING["UR5"] = SingleArm
robots.ROBOT_CLASS_MAPPING["Doosan"] = SingleArm

robots.BIMANUAL_ROBOTS = {k.lower() for k, v in robots.ROBOT_CLASS_MAPPING.items() if v == Bimanual}

