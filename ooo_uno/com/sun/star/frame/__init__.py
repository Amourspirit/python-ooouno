# coding: utf-8
from typing_extensions import TypeAlias
from .....uno_obj.frame.x_controller import XController
from .....uno_obj.frame.x_desktop import XDesktop
from .....uno_obj.frame.x_terminate_listener import XTerminateListener
from .....uno_obj.frame.x_frame_action_listener import XFrameActionListener
from .....uno_obj.frame.x_frame import XFrame
from .....uno_obj.frame.x_frames import XFrames
from .....uno_obj.frame.frame_action import FrameAction
from .....uno_obj.frame.frame_action_event import IFrameActionEvent
from .....uno_obj.frame.x_frames_supplier import XFramesSupplier
from .....uno_obj.frame.frame_search_flag import IFrameSearchFlag
FrameActionEvent: TypeAlias = IFrameActionEvent
FrameSearchFlag: TypeAlias = IFrameSearchFlag
