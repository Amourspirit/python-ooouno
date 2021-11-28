# coding: utf-8
from enum import Enum
from typing import TYPE_CHECKING
from ...env import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    # PushButtonType is string enum
    from com.sun.star.frame.FrameAction import (
        COMPONENT_ATTACHED, COMPONENT_DETACHING, COMPONENT_REATTACHED, FRAME_ACTIVATED,
        FRAME_DEACTIVATING, CONTEXT_CHANGED, FRAME_UI_ACTIVATED, FRAME_UI_DEACTIVATING)

class FrameAction(str, Enum):
    """
    these are the events which can happen to the components in frames of the desktop

    Interest listener can get information about loaded/reloaded or unloaded components into a ``Frame``.
    
    See Also:
        `API FrameAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame.html#a793fdb3e5cab69d63a9c89b5e4f83dfd>`_
    """
    COMPONENT_ATTACHED = 'COMPONENT_ATTACHED'
    """
    an event of this kind is broadcast whenever a component is attached to a frame

    This is almost the same as the instantiation of the component within that frame.
    The component is attached to the frame immediately before this event is broadcast.
    """
    COMPONENT_DETACHING = 'COMPONENT_DETACHING'
    """
    an event of this kind is broadcast whenever a component is detaching from a frame

    This is quite the same as the destruction of the component which was in that frame.
    At the moment when the event is broadcast the component is still attached to the
    frame but in the next moment it won't.
    """
    COMPONENT_REATTACHED = 'COMPONENT_REATTACHED'
    """
    an event of this kind is broadcast whenever a component is attached to a new model.

    In this case the component remains the same but operates on a new model component.
    """
    FRAME_ACTIVATED = 'FRAME_ACTIVATED'
    """
    an event of this kind is broadcast whenever a component gets activated

    Activations are broadcast from the top component which was not active before,
    down to the inner most component.
    """
    FRAME_DEACTIVATING = 'FRAME_DEACTIVATING'
    """
    an event of this kind is broadcasted immediately before the component is deactivated

    Deactivations are broadcast from the innermost component which does not stay active
    up to the outer most component which does not stay active.
    """
    CONTEXT_CHANGED = 'CONTEXT_CHANGED'
    """
    an event of this kind is broadcast whenever a component changes its
    internal context (i.e., the selection).

    If the activation status within a frame changes,
    this counts as a context change too.
    """
    FRAME_UI_ACTIVATED = 'FRAME_UI_ACTIVATED'
    """
    an event of this kind is broadcast by an active frame when it is getting
    UI control (tool control).
    """
    FRAME_UI_DEACTIVATING = 'FRAME_UI_DEACTIVATING'
    

def _dynamic_enum():
    '''
    Dynamically add Enum names and value for enum
    
    It is possible that enum values could change, therefore dynamically create enum
    '''
    global FrameAction
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
        FrameAction = Enum('FrameAction', {
            "COMPONENT_ATTACHED": COMPONENT_ATTACHED.value,
            "COMPONENT_DETACHING": COMPONENT_DETACHING.value,
            "COMPONENT_REATTACHED": COMPONENT_REATTACHED.value,
            "FRAME_ACTIVATED": FRAME_ACTIVATED.value,
            "FRAME_DEACTIVATING": FRAME_DEACTIVATING.value,
            "CONTEXT_CHANGED": CONTEXT_CHANGED.value,
            "FRAME_UI_ACTIVATED": FRAME_UI_ACTIVATED.value,
            "FRAME_UI_DEACTIVATING": FRAME_UI_DEACTIVATING.value
        })
        FrameAction.__str__ = lambda self: self._value_


if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['FrameAction']
