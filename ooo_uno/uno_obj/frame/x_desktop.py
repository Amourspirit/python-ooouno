# coding: utf-8
from abc import abstractmethod
from typing import TYPE_CHECKING
from ..uno.x_interface import XInterface
if TYPE_CHECKING:
    from .x_terminate_listener import XTerminateListener
    from ..container.x_enumeration_access import XEnumerationAccess
    from ..lang.x_component import XComponent
    from .x_frame import XFrame


class XDesktop(XInterface):
    """
    This is the main interface of a desktop service.

    A desktop is an environment for components which can be viewed in frames.
    Frames are like frames in HTML framesets. This does not imply that a desktop can handle framesets; the frames may be top frames only.

    See Also:
        `API XDesktop <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDesktop.html>`_
    """

    @abstractmethod
    def addTerminateListener(self, Listener: 'XTerminateListener'):
        """
        registers an event listener to the desktop, which is called when the desktop is
        queried to terminate, and when it really terminates.

        Args:
            Listener (XTerminateListener): listener for termination events

        """

    @abstractmethod
    def getComponents(self) -> 'XEnumerationAccess':
        """
        provides read access to collection of all currently loaded components inside the frame tree

        The component is, by definition, the model of the control which is loaded into a frame,
        or if no model exists, into the control itself. The service Components
        which is available from this method is a collection of all components of the
        desktop which are open within a frame of the desktop.

        Returns:
            XEnumerationAccess: the collection of all components
        """

    @abstractmethod
    def getCurrentComponent(self) -> 'XComponent':
        """
        provides read access to the component inside the tree which has the UI focus

        Normally, the component is the model part of the active component.
        If no model exists it is the active controller (view) itself.

        Returns:
            XComponent: the component within the desktop environment which has the UI focus.
        """

    @abstractmethod
    def getCurrentFrame(self) -> 'XFrame':
        """
        provides read access to the frame which contains the current component

        Returns:
            XFrame: the frame of the component which has the UI focus within this desktop environment
        """

    @abstractmethod
    def removeTerminateListener(self, Listener: 'XTerminateListener'):
        """
        unregisters an event listener for termination events.

        Args:
            Listener (XTerminateListener): listener which wishes to be deregistered
        """

    @abstractmethod
    def terminate(self) -> bool:
        """
        tries to terminate the desktop.

        First, every terminate listener is called by his XTerminateListener::queryTermination() method.
        Throwing of a TerminationVetoException can break the termination process and the listener
        how has done that will be the new "controller" of the desktop lifetime. He should try to terminate
        it by himself after his own processes will be finished. If nobody disagree with the termination
        request, every listener will be called by his ``XTerminateListener.notifyTermination()`` method.

        Returns:
            bool: ``True`` If all listeners agree with this request; Otherwise, ``False``.
        """
