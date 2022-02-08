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
# Namespace: com.sun.star.awt
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import ImageDrawMode
else:
    from ...lo.awt.image_draw_mode import ImageDrawMode as ImageDrawMode


class ImageDrawModeEnum(IntFlag):
    """
    Enum of Const Class ImageDrawMode

    defines modes how an image is drawn onto a device
    
    **since**
    
        LibreOffice 4.1
    """
    NONE = ImageDrawMode.NONE
    """
    the image is drawn as is, without any color transformation.
    """
    DISABLE = ImageDrawMode.DISABLE
    """
    the image is drawn as if it represented a feature whose state is disabled.
    """
    HIGHLIGHT = ImageDrawMode.HIGHLIGHT
    """
    the image is drawn as being highlighted.
    
    See com.sun.star.awt.XStyleSettings.HighlightColor.
    """
    DEACTIVE = ImageDrawMode.DEACTIVE
    """
    the image is drawn as being deactivated.
    
    See com.sun.star.awt.XStyleSettings.DeactiveColor.
    """
    SEMITRANSPARENT = ImageDrawMode.SEMITRANSPARENT
    """
    the image is drawn semi-transparent.
    """

__all__ = ['ImageDrawMode', 'ImageDrawModeEnum']
