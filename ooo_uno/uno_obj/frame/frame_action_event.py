# coding: utf-8
from abc import abstractproperty
from ..lang.event_object import IEventObject
from .x_frame import XFrame
from .frame_action import IFrameAction


class IFrameActionEvent(IEventObject):
    """
    this event interface is broadcast for actions which can happen to components within frames
    
    See Also:
        `API FrameActionEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1FrameActionEvent.html>`_
    """

    @abstractproperty
    def Action(self) -> IFrameAction:
        """
        specifies the concrete event

        Returns:
            FrameAction: enum
        """

    @abstractproperty
    def Frame(self) -> XFrame:
        """
        contains the frame in which the event occurred

        Returns:
            XFrame: frame
        """
