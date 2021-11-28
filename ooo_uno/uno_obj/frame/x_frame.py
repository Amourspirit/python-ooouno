# coding: utf-8
from abc import abstractmethod
from typing import Optional, Union, TYPE_CHECKING
from ..lang.x_component import XComponent
if TYPE_CHECKING:
    from .x_controller import XController
    from .x_frame_action_listener import XFrameActionListener
    from .x_frames_supplier import XFramesSupplier
    from .frame_action import FrameAction


class XFrame(XComponent):
    """
    a frame object can be considered to be an "anchor" object where a component can be attached to.

    A frame can be (it's not a must!) a part of a frame tree. If not this frame won't be accessible
    by using the API. This mode make sense for previews. The root node of the tree can be a Desktop
    implementation.

    See Also:
        `API Frame <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrame.html>`_
    """

    @abstractmethod
    def activate(self):
        """
        activates this frame and thus the component within.

        At first the frame sets itself as the active frame of its creator by calling
        ``XFramesSupplier.setActiveFrame()``, then it broadcasts a FrameActionEvent with
        ``FrameAction.FRAME_ACTIVATED``. The component within this frame may listen to
        this event to grab the focus on activation; for simple components this can be done
        by the FrameLoader.

        Finally, most frames may grab the focus to one of its windows or forward the
        activation to a sub-frame.
        """

    @abstractmethod
    def addFrameActionListener(self, xListener: 'XFrameActionListener'):
        """
        registers an event listener, which will be called when certain things happen to
        the components within this frame or within sub-frames of this frame.

        E.g., it is possible to determine instantiation/destruction and
        activation/deactivation of components.

        Args:
            xListener (XFrameActionListener): specifies the listener which will be informed
        """

    @abstractmethod
    def contextChanged(self):
        """
        notifies the frame that the context of the controller within this
        frame changed (i.e. the selection).

        According to a call to this interface, the frame calls ``XFrameActionListener.frameAction()``
        with FrameAction::CONTEXT_CHANGED to all listeners which are registered using
        ``XFrame.addFrameActionListener()``. For external controllers this event can be used to
        requery dispatches.
        """

    @abstractmethod
    def deactivate(self):
        """
        is called by the creator frame when another sub-frame gets activated.

        At first the frame deactivates its active sub-frame, if any.
        Then broadcasts a FrameActionEvent with ``FrameAction.FRAME_DEACTIVATING``.
        """

    @abstractmethod
    def findFrame(self, aTargetFrameName: str, nSearchFlags: Optional['FrameAction']) -> 'XFrame':
        """
        searches for a frame with the specified name.

        Frames may contain other frames (e.g., a frameset) and may be contained in other frames.
        This hierarchy is searched with this method. First some special names are taken into account,
        i.e. "", "_self", "_top", "_blank" etc. *SearchFlags* is ignored when comparing these names
        with *TargetFrameName*; further steps are controlled by SearchFlags. If allowed, the name of
        the frame itself is compared with the desired one, and then ( again if allowed ) the method
        is called for all children of the frame. Finally may be called for the siblings and then for
        parent frame (if allowed).

        +-------------+---------------------------------------------------------+
        | ""/"_self"  | address the starting frame itself                       |
        +=============+=========================================================+
        | "_parent"   | address the direct parent frame only                    |
        +-------------+---------------------------------------------------------+
        | "_top"      | address the top frame of this subtree of the frametree  |
        +-------------+---------------------------------------------------------+
        | "_blank"    | creates a new top frame                                 |
        +-------------+---------------------------------------------------------+


        If no frame with the given name is found, a new top frame is created; if this is
        allowed by a special flag ``FrameSearchFlag.CREATE``. The new frame also gets the desired name.

        Args:
            aTargetFrameName (str): identify

                * (a) a special target ("_blank","_self" ...) or
                * (b) any well known frame

                to search it inside the current hierarchy
            nSearchFlags (int, optional): parameter to regulate search if no special target was used for *TargetFrameName*

        Returns:
            XFrame: frame
        """

    @abstractmethod
    def getComponentWindow(self) -> Union[object, None]:
        """
        provides access to the component window

        Note:
            Don't dispose this window - the frame is the owner of it.

        Todo:
            Update return value to be of type com.sun.star.awt.XWindow

        Returns:
            Union[XWindow, None]: the current visible component in this frame or ``None`` if no one currently exist
        """

    @abstractmethod
    def getContainerWindow(self) -> object:
        """
        provides access to the container window of the frame.

        Normally this is used as the parent window of the component window.

        Todo:
            Update return value to be of type com.sun.star.awt.XWindow

        Returns:
            XWindow: the container window of this frame
        """

    @abstractmethod
    def getController(self) -> 'XController':
        """
        provides access to the controller

        Note:
            Don't dispose it - the frame is the owner of it.
            Use ``XController.getFrame()`` to dispose the frame after you the controller
            agreed with a ``XController.suspend()`` call.

        Returns:
            XController: the current controller within this frame or ``None`` if no one currently exist
        """

    @abstractmethod
    def getCreator(self) -> 'XFramesSupplier':
        """
        provides access to the creator (parent) of this frame

        Returns:
            XFramesSupplier: the frame container that created and contains this frame.
        """

    @abstractmethod
    def getName(self) -> str:
        """
        access to the name property of this frame

        Returns:
            str: the programmatic name of this frame.
        """

    @abstractmethod
    def initialize(self, xWindow: object):
        """
        is called to initialize the frame within a window - the container window.

        This window will be used as parent for the component window and to support
        some UI relevant features of the frame service. Note: Re-parenting mustn't
        supported by a real frame implementation! It's designed for
        initializing - not for setting.

        This frame will take over ownership of the window referred from *xWindow*.
        Thus, the previous owner is not allowed to dispose this window anymore.

        Todo:
            Update Arg xWindow to be of type com.sun.star.awt.XWindow
        Args:
            xWindow (XWindow): the new container window
        """

    @abstractmethod
    def isActive(self) -> bool:
        """
        determines if the frame is active.

        Returns:
            bool: ``True`` for active or UI active frames; Otherwise, ``False``.
        """

    @abstractmethod
    def isTop(self) -> bool:
        """
        determines if the frame is a top frame.

        In general a top frame is the frame which is a direct child of a task frame
        or which does not have a parent. Possible frame searches must stop the search
        at such a frame unless the flag ``FrameSearchFlag.TASKS`` is set.

        Returns:
            bool: ``True`` if frame supports top frame specification; Otherwise, ``False``.
        """

    @abstractmethod
    def removeFrameActionListener(self, xListener: 'XFrameActionListener'):
        """
        unregisters an event listener

        Args:
            xListener (XFrameActionListener): specifies the listener which won't be informed any longer
        """

    @abstractmethod
    def setComponent(self, xComponentWindow: object, xController: 'XController') -> bool:
        """
        sets a new component into the frame or release an existing one from a frame.

        Args:
            xComponentWindow (XWindow): the window of the new component or ``None`` for release
                A valid component window should be a child of the frame container window.
            xController (XController): the controller of the new component or ``None`` for release
                Simple components may implement a ``com.sun.star.awt.XWindow`` only.
                In this case no controller must be given here.

        Todo:
            update arg xComponentWindow to be of type com.sun.star.awt.XWindow

        Returns:
            bool: ``True`` if setting of new component or release of an existing one was successfully;
            Otherwise, ``False`` (especially, if an existing controller disagree within this
            ``XController.suspend()`` call)
        """

    @abstractmethod
    def setCreator(self, Creator: 'XFramesSupplier'):
        """
        sets the frame container that created this frame.

        Only the creator is allowed to call this method. But creator doesn't mean the implementation
        which creates this instance ... it means the parent frame of the frame hierarchy.
        Because; normally a frame should be created by using the API and is necessary for searches
        inside the tree (e.g. XFrame.findFrame())

        Args:
            Creator (XFramesSupplier): the creator (parent) of this frame

        """

    @abstractmethod
    def setName(self, aName: str):
        """
        sets the name of the frame.

        Normally the name of the frame is set initially (e.g. by the creator). The name of a
        frame will be used for identifying it if a frame search was started.
        These searches can be forced by:

        * ``XFrame.findFrame()``
        * ``XDispatchProvider.queryDispatch()``
        * ``XComponentLoader.loadComponentFromURL()``

        Note:
            Special targets like "_blank", "_self" etc. are not allowed.
            That's why frame names shouldn't start with a sign "_".

        Args:
            aName (str): the new programmatic name of this frame
        """
