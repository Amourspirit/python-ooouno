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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.animations
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .x_animation_node import XAnimationNode as XAnimationNode_1cf10eb9

class XAnimationListener(XEventListener_c7230c4a):
    """
    makes it possible to register listeners, which are called whenever an animation event occurs.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XAnimationListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XAnimationListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.XAnimationListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.animations.XAnimationListener'

    @abstractmethod
    def beginEvent(self, Node: 'XAnimationNode_1cf10eb9') -> None:
        """
        This event is raised when the element local timeline begins to play.
        
        It will be raised each time the element begins the active duration (i.e. when it restarts, but not when it repeats).
        
        It may be raised both in the course of normal (i.e. scheduled or interactive) timeline play, as well as in the case that the element was begun with an interface method.
        """
        ...
    @abstractmethod
    def endEvent(self, Node: 'XAnimationNode_1cf10eb9') -> None:
        """
        This event is raised at the active end of the element.
        
        Note that this event is not raised at the simple end of each repeat.
        
        This event may be raised both in the course of normal (i.e. scheduled or interactive) timeline play, as well as in the case that the element was ended with a DOM method.
        """
        ...
    @abstractmethod
    def repeat(self, Node: 'XAnimationNode_1cf10eb9', Repeat: int) -> None:
        """
        This event is raised when the element local timeline repeats.
        
        It will be raised each time the element repeats, after the first iteration.
        
        Associated with the repeat event is an integer that indicates which repeat iteration is beginning.
        """
        ...

__all__ = ['XAnimationListener']

