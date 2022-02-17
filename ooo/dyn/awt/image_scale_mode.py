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
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import ImageScaleMode as ImageScaleMode
else:
    from ...lo.awt.image_scale_mode import ImageScaleMode as ImageScaleMode


class ImageScaleModeEnum(IntEnum):
    """
    Enum of Const Class ImageScaleMode

    defines modes how an image displayed in a given area should be scaled to fit this area
    """
    NONE = ImageScaleMode.NONE
    """
    specifies that no scaling should happen at all
    """
    ISOTROPIC = ImageScaleMode.ISOTROPIC
    """
    specifies that the image should be scaled up or down to the size of the surrounding area isotropically, i.e.
    
    by keeping its aspect ratio.
    """
    ANISOTROPIC = ImageScaleMode.ANISOTROPIC
    """
    specifies that the image should be scaled up or down to the size of the surrounding area anisotropically.
    
    The image will finally cover all of the surrounding area, but its dimensions might be distorted.
    """

__all__ = ['ImageScaleMode', 'ImageScaleModeEnum']