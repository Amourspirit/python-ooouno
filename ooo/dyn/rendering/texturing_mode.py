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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.rendering
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rendering import TexturingMode
else:
    from ...lo.rendering.texturing_mode import TexturingMode as TexturingMode


class TexturingModeEnum(IntEnum):
    """
    Enum of Const Class TexturingMode

    Enumeration of possible values to spread a texture across a primitive.
    
    **since**
    
        OOo 2.0
    """
    NONE = TexturingMode.NONE
    """
    Pixel outside the texture area are fully transparent.
    
    This completely switches off pixel generation outside the texture coordinate range [0,1]. This results in only one instance of the texture generated per textured primitive.
    """
    CLAMP = TexturingMode.CLAMP
    """
    Clamp texture coordinate.
    
    This value clamps the texture coordinates to the range [0,1]. This results in only one instance of the texture generated per textured primitive, with the remaining area filled with the color of the outermost texels
    """
    REPEAT = TexturingMode.REPEAT
    """
    Repeat the texture.
    
    This value repeats the texture over the textured primitive, for the given texture coordinate.
    """

__all__ = ['TexturingMode', 'TexturingModeEnum']
