# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.rendering
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class RenderingIntent(metaclass=UnoConstMeta, type_name="com.sun.star.rendering.RenderingIntent", name_space="com.sun.star.rendering"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.rendering.RenderingIntent``"""
        pass

    class RenderingIntentEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.rendering.RenderingIntent", name_space="com.sun.star.rendering"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.rendering.RenderingIntent`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.rendering import RenderingIntent as RenderingIntent
    else:
        # keep document generators happy
        from ...lo.rendering.rendering_intent import RenderingIntent as RenderingIntent

    class RenderingIntentEnum(IntEnum):
        """
        Enum of Const Class RenderingIntent

        The rendering intent for a color space.
        
        The rendering intent for a color space mostly determines how out-of-gamut color is treated. See Wikipedia for a thorough explanation.
        
        **since**
        
            OOo 2.0
        """
        PERCEPTUAL = RenderingIntent.PERCEPTUAL
        """
        Also known as the image intent, this rendering intent aims to preserve the visual relationship between colors in a way that is perceived as natural to the human eye, although the color values themselves may change.
        
        This intent is most suitable for photographic images.
        """
        SATURATION = RenderingIntent.SATURATION
        """
        The rendering intent for business graphics that maintains vivid color at the expense of accurate color.
        
        It scales the source gamut to the destination gamut but preserves relative saturation instead of hue, so when scaling to a smaller gamut, hues may shift. This rendering intent is primarily designed for business graphics, where bright saturated colors are more important than the exact relationship between colors (such as in a photographic image).
        """
        RELATIVE_COLORIMETRIC = RenderingIntent.RELATIVE_COLORIMETRIC
        """
        The rendering intent almost identical to Absolute Colorimetric except for the following difference: Relative Colorimetric compares the white point (extreme highlight) of the source color space to that of the destination color space and shifts all colors accordingly.
        """
        ABSOLUTE_COLORIMETRIC = RenderingIntent.ABSOLUTE_COLORIMETRIC
        """
        The rendering intent that leaves colors that fall inside the destination gamut unchanged.
        
        Out of gamut colors are clipped. No scaling of colors to destination white point is performed. This intent aims to maintain color accuracy at the expense of preserving relationships between colors, and is useful for seeing how output will look on a non-neutral substrate.
        """

__all__ = ['RenderingIntent', 'RenderingIntentEnum']
