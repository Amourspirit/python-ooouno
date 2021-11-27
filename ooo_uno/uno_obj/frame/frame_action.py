# coding: utf-8
from abc import ABC, abstractproperty


class IFrameAction(ABC):
    """
    these are the events which can happen to the components in frames of the desktop

    Interest listener can get information about loaded/reloaded or unloaded components into a ``Frame``.
    
    See Also:
        `API FrameAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame.html#a793fdb3e5cab69d63a9c89b5e4f83dfd>`_
    """

    @abstractproperty
    def COMPONENT_ATTACHED(self) -> int:
        """
        an event of this kind is broadcast whenever a component is attached to a frame

        This is almost the same as the instantiation of the component within that frame.
        The component is attached to the frame immediately before this event is broadcast.
        """

    @abstractproperty
    def COMPONENT_DETACHING(self) -> int:
        """
        an event of this kind is broadcast whenever a component is detaching from a frame

        This is quite the same as the destruction of the component which was in that frame.
        At the moment when the event is broadcast the component is still attached to the
        frame but in the next moment it won't.
        """

    @abstractproperty
    def COMPONENT_REATTACHED(self) -> int:
        """
        an event of this kind is broadcast whenever a component is attached to a new model.

        In this case the component remains the same but operates on a new model component.
        """

    @abstractproperty
    def FRAME_ACTIVATED(self) -> int:
        """
        an event of this kind is broadcast whenever a component gets activated

        Activations are broadcast from the top component which was not active before,
        down to the inner most component.
        """

    @abstractproperty
    def FRAME_DEACTIVATING(self) -> int:
        """
        an event of this kind is broadcasted immediately before the component is deactivated

        Deactivations are broadcast from the innermost component which does not stay active
        up to the outer most component which does not stay active.
        """

    @abstractproperty
    def CONTEXT_CHANGED(self) -> int:
        """
        an event of this kind is broadcast whenever a component changes its
        internal context (i.e., the selection).

        If the activation status within a frame changes,
        this counts as a context change too.
        """

    @abstractproperty
    def FRAME_UI_ACTIVATED(self) -> int:
        """
        an event of this kind is broadcast by an active frame when it is getting
        UI control (tool control).
        """

    @abstractproperty
    def FRAME_UI_DEACTIVATING(self) -> int:
        """
        an event of this kind is broadcast by an active frame when it is losing
        UI control (tool control).
        """
