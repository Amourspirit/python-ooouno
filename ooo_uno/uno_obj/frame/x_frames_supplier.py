# coding: utf-8
from abc import abstractmethod
from typing import TYPE_CHECKING
from .x_frame import XFrame
if TYPE_CHECKING:
    from .x_frames import XFrames


class XFramesSupplier(XFrame):
    """
    provides access to sub frames of current one

    See Also:
        `API XFramesSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFramesSupplier.html>`_
    """

    @abstractmethod
    def getActiveFrame(self) -> XFrame:
        """
        gets the current active frame of this container (not of any other available supplier)

        This may be the frame itself. The active frame is defined as the frame which contains
        (recursively) the window with the focus. If no window within the frame contains the focus,
        this method returns the last frame which had the focus. If no containing window ever had
        the focus, the first frame within this frame is returned.

        Returns:
            XFrame: the Frame which is active within this frame.
        """

    @abstractmethod
    def getFrames(self) -> 'XFrames':
        """
        provides access to this container and to all other ``XFramesSupplier`` which are available
        from this node of frame tree

        Returns:
            XFrames: the collection of frames which is represented by a ``FramesContainer``.
        """

    @abstractmethod
    def setActiveFrame(self, Frame: XFrame):
        """
        is called on activation of a direct sub-frame.

        This method is only allowed to be called by a sub-frame according to ``XFrame.activate()``
        or ``XFramesSupplier.setActiveFrame()``. After this call ``XFramesSupplier.getActiveFrame()``
        will return the frame specified by Frame.

        In general this method first calls the method ``XFramesSupplier.setActiveFrame()`` at the
        creator frame with this as the current argument. Then it broadcasts the FrameActionEvent
        ``FrameAction.FRAME_ACTIVATED``.

        Note:
            Given parameter Frame must already exist inside the container 
            e.g., inserted by using XFrames.append())

        Args:
            Frame (XFrame): the new active child frame inside this container
        """
