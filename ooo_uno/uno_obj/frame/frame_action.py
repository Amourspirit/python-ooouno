# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.frame.FrameAction import (COMPONENT_ATTACHED, COMPONENT_DETACHING, COMPONENT_REATTACHED, CONTEXT_CHANGED, FRAME_ACTIVATED, FRAME_DEACTIVATING, FRAME_UI_ACTIVATED, FRAME_UI_DEACTIVATING)


class FrameAction(Enum):
    """
    

    See Also:
        `API FrameAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame.html#a793fdb3e5cab69d63a9c89b5e4f83dfd>`_
    """
    COMPONENT_ATTACHED = 'COMPONENT_ATTACHED'
    """
    an event of this kind is broadcast whenever a component is attached to a frame
    
    This is almost the same as the instantiation of the component within that frame. The component is attached to the frame immediately before this event is broadcast.
    """
    COMPONENT_DETACHING = 'COMPONENT_DETACHING'
    """
    an event of this kind is broadcast whenever a component is detaching from a frame
    
    This is quite the same as the destruction of the component which was in that frame. At the moment when the event is broadcast the component is still attached to the frame but in the next moment it won't.
    """
    COMPONENT_REATTACHED = 'COMPONENT_REATTACHED'
    """
    an event of this kind is broadcast whenever a component is attached to a new model.
    
    In this case the component remains the same but operates on a new model component.
    """
    CONTEXT_CHANGED = 'CONTEXT_CHANGED'
    """
    an event of this kind is broadcast whenever a component changes its internal context (i.e., the selection).
    
    If the activation status within a frame changes, this counts as a context change too.
    """
    FRAME_ACTIVATED = 'FRAME_ACTIVATED'
    """
    an event of this kind is broadcast whenever a component gets activated
    
    Activations are broadcast from the top component which was not active before, down to the inner most component.
    """
    FRAME_DEACTIVATING = 'FRAME_DEACTIVATING'
    """
    an event of this kind is broadcasted immediately before the component is deactivated
    
    Deactivations are broadcast from the innermost component which does not stay active up to the outer most component which does not stay active.
    """
    FRAME_UI_ACTIVATED = 'FRAME_UI_ACTIVATED'
    """
    an event of this kind is broadcast by an active frame when it is getting UI control (tool control).
    """
    FRAME_UI_DEACTIVATING = 'FRAME_UI_DEACTIVATING'
    """
    an event of this kind is broadcast by an active frame when it is losing UI control (tool control).
    """

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global FrameAction
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "COMPONENT_ATTACHED": COMPONENT_ATTACHED,
            "COMPONENT_DETACHING": COMPONENT_DETACHING,
            "COMPONENT_REATTACHED": COMPONENT_REATTACHED,
            "CONTEXT_CHANGED": CONTEXT_CHANGED,
            "FRAME_ACTIVATED": FRAME_ACTIVATED,
            "FRAME_DEACTIVATING": FRAME_DEACTIVATING,
            "FRAME_UI_ACTIVATED": FRAME_UI_ACTIVATED,
            "FRAME_UI_DEACTIVATING": FRAME_UI_DEACTIVATING,
        }
        FrameAction = type('FrameAction', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(FrameAction, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['FrameAction']

