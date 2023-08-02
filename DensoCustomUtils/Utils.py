from .FigCalc import *


class MoveInterpolation(Enum):
    LINEAR = 'Linear'
    POINT_TO_POINT = 'PointToPoint'
    JOINT = 'Joint'
    NONE = ''


@dataclass
class Pose:
    pose: np.array
    fig: int

    def to_dict(self):
        return {'Pose': self.pose.tolist(), 'Fig': self.fig}


class RobotMotion:
    def __init__(self, frame, tool, pose, joints, move_interpolation=MoveInterpolation.NONE, **kwargs):
        self.frame = frame
        self.tool = tool
        self.pose = pose
        self.joints = joints
        self.move_interpolation = move_interpolation
        self.meta = kwargs

    def to_dict(self):
        return {'Frame': self.frame, 'Tool': self.tool, 'Pose': self.pose.to_dict(), 'Meta': self.meta}


class SystemStateHolder:
    def __init__(self):
        self.frames = dict()
        self.tools = dict()
        self.active_frame = ''
        self.active_tool = ''

    def set_frame(self, frame_name: str, pose: np.array):
        if frame_name is None:
            raise Exception("Invalid empty frame name received")
        self.frames[frame_name] = list(pose)
        self.active_frame = frame_name

    def set_tool(self, tool_name: str, pose: np.array):
        if tool_name is None:
            raise Exception("Invalid empty tool name received")
        self.tools[tool_name] = list(pose)
        self.active_tool = tool_name


_DENSO_MHD = mhd = np.array([
    [0.0000000, -1.5707963, 0.0000000, -1.5707963, 1.5707963, -1.5707963],
    [0.0000000, 180.0000000, 520.0000000, 100.0000000, 0.0000000, 0.0000000],
    [0.0000000, -1.5707963, -1.5707963, 0.0000000, 0.0000000, 3.1415927],
    [475.0000000, 0.0000000, 0.0000000, 590.0000000, 0.0000000, 90.0000000]
]).T
_fig_calculator = FigCalculator.from_parameters(_DENSO_MHD)


def get_fig(joints):
    return _fig_calculator.calc_fig(np.deg2rad(joints))
