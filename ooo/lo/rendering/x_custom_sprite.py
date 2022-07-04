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
# Libre Office Version: 7.2
# Namespace: com.sun.star.rendering
import typing
from abc import abstractmethod
from .x_sprite import XSprite as XSprite_b2470b95
if typing.TYPE_CHECKING:
    from .x_canvas import XCanvas as XCanvas_b19b0b7a

class XCustomSprite(XSprite_b2470b95):
    """
    Interface to control a custom sprite object on a XSpriteCanvas.
    
    Every change performed on XCustomSprite objects is only visible after a XSpriteCanvas.updateScreen() call, to facilitate synchronized screen updates.
    
    TODO: Maybe more than alpha has to be overridden from render state. TODO: Provide means to change the output area

    See Also:
        `API XCustomSprite <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XCustomSprite.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XCustomSprite'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XCustomSprite'

    @abstractmethod
    def getContentCanvas(self) -> 'XCanvas_b19b0b7a':
        """
        Query a render canvas for this sprite's content.
        
        Whatever is rendered to this canvas will become visible on the screen only after a XSpriteCanvas.updateScreen() call at the associated sprite canvas. This canvas is not equivalent to the host canvas of the sprite. At the very least, all output happens relative to the sprite's upper left corner, i.e. the origin of the sprite's canvas device coordinate system will move with the sprite across the screen.
        """
        ...

__all__ = ['XCustomSprite']

