# coding: utf-8
from abc import abstractmethod
from typing import Iterable

from ..frame.x_frame import XFrame
from ..container.x_index_access import XIndexAccess
from .frame_search import IFrameSearch


class XFrames(XIndexAccess):
    """
    manages and creates frames.

    Frames may contain other frames (by implementing an XFrames
    interface) and may be contained in other frames.
    """

    @abstractmethod
    def append(self, xFrame: XFrame):
        """
        appends the specified Frame to the list of sub-frames.

        Args:
            xFrame (XFame): new frame for inserting into this container
        """

    @abstractmethod
    def queryFrames(self, nSearchFlags: IFrameSearch) -> Iterable[XFrame]:
        """
        provides access to the list of all currently existing frames inside this container and her sub frames

        Args:
            nSearchFlags (FrameSearchFlag): specifies which frames should be found

        Returns:
            Iterable[XFrame]: all frames of this container and all available frames of the
            whole frame tree which match search parameter *SearchFlags*
        """

    @abstractmethod
    def remove(self, xFrame: XFrame):
        """
        removes the frame from its container.


        Args:
            xFrame (XFrame): frame which should be removed from this container

        Note:

            * The method XComponent::dispose() is not called implicitly by this method.
            * The creator attribute of the frame must be reset by the caller of this method.
        """
