# coding: utf-8
from abc import abstractmethod
from typing import TYPE_CHECKING
from ..lang.x_event_listener import XEventListener
if TYPE_CHECKING:
    from .frame_action_event import IFrameActionEvent

class XFrameActionListener(XEventListener):
    """
    has to be provided if an object wants to receive events when several
    things happen to components within frames of the desktop frame tree.

    See Also:
        `API XFrameActionListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrameActionListener.html>`_
    """

    @abstractmethod
    def frameAction(self, Action: 'IFrameActionEvent'):
        """
        is called whenever any action occurs to a component within a frame.


        Args:
            Action (IFrameActionEvent): describes the detected frame action for which the listener can react
        """
