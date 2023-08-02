from pybotics.robot import Robot
import numpy as np
from enum import Enum
from dataclasses import dataclass


class RightyLeftyMode(Enum):
    RIGHTY = 0
    LEFTY = 1


class AboveBelowMode(Enum):
    ABOVE = 0
    BELOW = 2


class FlipNonFlipMode(Enum):
    FLIP = 0
    NON_FLIP = 4


class J6SingleDoubleTripleMode(Enum):
    SINGLE = 0
    DOUBLE = 8


class J4SingleDoubleMode(Enum):
    SINGLE = 0
    DOUBLE = 16


@dataclass
class FigDescriptor:
    righty_lefty_mode: RightyLeftyMode = RightyLeftyMode.RIGHTY
    above_below_mode: AboveBelowMode = AboveBelowMode.ABOVE
    flip_non_flip_mode: FlipNonFlipMode = FlipNonFlipMode.FLIP
    J4_single_double_mode: J4SingleDoubleMode = J4SingleDoubleMode.SINGLE
    J6_single_double_mode: J6SingleDoubleTripleMode = J6SingleDoubleTripleMode.SINGLE

    def get_fig_value(self):
        return self.righty_lefty_mode.value + self.above_below_mode.value + \
            self.flip_non_flip_mode.value + self.J6_single_double_mode.value + self.J4_single_double_mode.value


class FigCalculator(Robot):
    def __init__(self, *args, **kwargs):
        self.fig_descriptor = FigDescriptor()
        super().__init__(*args, **kwargs)

    def calc_fig(self, joints):
        if joints is None:
            raise Exception("Joints not set, call set_joints with the joint values first!")
        self._calc_righty_lefty(joints)
        self._calc_above_below(joints)
        self._calc_flip_non_flip(joints)
        self._calc_j4_sd(joints)
        self._calc_j6_sd(joints)
        return self.fig_descriptor.get_fig_value()

    def _calc_righty_lefty(self, joints):
        pose = self._get_transforms(range(2, 5), joints)
        self.fig_descriptor.righty_lefty_mode = RightyLeftyMode.LEFTY if pose[0, 3] > 0 else RightyLeftyMode.RIGHTY

    def _calc_above_below(self, joints):
        pose = self._get_transforms(range(3, 5), joints)
        is_above = pose[1, 3] > 0
        is_above = is_above if self.fig_descriptor.righty_lefty_mode == RightyLeftyMode.LEFTY else not is_above
        self.fig_descriptor.above_below_mode = AboveBelowMode.ABOVE if is_above else AboveBelowMode.BELOW

    def _calc_flip_non_flip(self, joints):
        pose = self._get_transforms(range(5, 7), joints)
        is_flip = pose[0, 3] > 0
        is_flip = is_flip if self.fig_descriptor.righty_lefty_mode == RightyLeftyMode.LEFTY else not is_flip
        self.fig_descriptor.flip_non_flip_mode = FlipNonFlipMode.FLIP if is_flip else FlipNonFlipMode.NON_FLIP

    def _calc_j4_sd(self, joints):
        self.fig_descriptor.J4_single_double_mode = FigCalculator._calc_sd_fig(joints[3], np.pi, J4SingleDoubleMode)

    def _calc_j6_sd(self, joints):
        self.fig_descriptor.J6_single_double_mode = FigCalculator._calc_sd_fig(joints[5], np.pi,
                                                                               J6SingleDoubleTripleMode)

    @staticmethod
    def _calc_sd_fig(joint, threshold, options):
        return options.SINGLE if -threshold < joint <= threshold else options.DOUBLE

    def _get_transforms(self, joint_range, joints):
        transforms = [np.eye(4)]
        transforms.extend(self.kinematic_chain.transforms(joints))
        pose = np.eye(4, dtype=float)
        poses = []
        for i in joint_range:
            t = transforms[i]
            pose = np.dot(pose, t)
            poses.append(pose.copy())
        return pose
