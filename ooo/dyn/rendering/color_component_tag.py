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
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ColorComponentTag(metaclass=UnoConstMeta, type_name="com.sun.star.rendering.ColorComponentTag", name_space="com.sun.star.rendering"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.rendering.ColorComponentTag``"""
        pass

    class ColorComponentTagEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.rendering.ColorComponentTag", name_space="com.sun.star.rendering"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.rendering.ColorComponentTag`` as Enum values"""
        pass

else:
    from ...lo.rendering.color_component_tag import ColorComponentTag as ColorComponentTag

    class ColorComponentTagEnum(IntEnum):
        """
        Enum of Const Class ColorComponentTag

        A collection of tags for the individual components of a color.
        
        Color components usually correspond to physical attributes like the amount of red colorant contained in an output color. This constant field enumerates the most common ones.
        
        **since**
        
            OOo 2.3
        """
        DEVICE = ColorComponentTag.DEVICE
        """
        Unspecified device color value.
        """
        RGB_RED = ColorComponentTag.RGB_RED
        """
        Red colorant from RGB color space.
        """
        RGB_GREEN = ColorComponentTag.RGB_GREEN
        """
        Green colorant from RGB color space.
        """
        RGB_BLUE = ColorComponentTag.RGB_BLUE
        """
        Blue colorant from RGB color space.
        """
        CMYK_CYAN = ColorComponentTag.CMYK_CYAN
        """
        Cyan colorant from CMYK color space.
        """
        CMYK_MAGENTA = ColorComponentTag.CMYK_MAGENTA
        """
        Magenta colorant from CMYK color space.
        """
        CMYK_YELLOW = ColorComponentTag.CMYK_YELLOW
        """
        Yellow colorant from CMYK color space.
        """
        CMYK_BLACK = ColorComponentTag.CMYK_BLACK
        """
        Black colorant from CMYK color space.
        """
        CMYKOG_ORANGE = ColorComponentTag.CMYKOG_ORANGE
        """
        Orange colorant from hexachrome color space.
        """
        CMYKOG_GREEN = ColorComponentTag.CMYKOG_GREEN
        """
        Green colorant from hexachrome color space.
        """
        SPOT = ColorComponentTag.SPOT
        """
        Arbitrary extra spot color, e.g. Pantone.
        """
        INDEX = ColorComponentTag.INDEX
        """
        Index into palette.
        """
        ALPHA = ColorComponentTag.ALPHA
        """
        Alpha channel.
        """
        GREY = ColorComponentTag.GREY
        """
        Grey value. Used for monochrome color spaces.
        """
        PREMULTIPLIED_ALPHA = ColorComponentTag.PREMULTIPLIED_ALPHA
        """
        Premultiplied alpha channel.
        
        Note that this alpha format actually influences the other color components, in that their values are pre-multiplied with the alpha value.
        """
        CIEXYZ_X = ColorComponentTag.CIEXYZ_X
        """
        CieXYZ X value.
        """
        CIEXYZ_Y = ColorComponentTag.CIEXYZ_Y
        """
        CieXYZ Y value.
        """
        CIEXYZ_Z = ColorComponentTag.CIEXYZ_Z
        """
        CieXYZ Z value.
        """
        CIELAB_L = ColorComponentTag.CIELAB_L
        """
        CieLab L value.
        """
        CIELAB_A = ColorComponentTag.CIELAB_A
        """
        CieLab a value.
        """
        CIELAB_B = ColorComponentTag.CIELAB_B
        """
        CieLab b value.
        """
        HSV_H = ColorComponentTag.HSV_H
        """
        HSV H value.
        """
        HSV_S = ColorComponentTag.HSV_S
        """
        HSV S value.
        """
        HSV_V = ColorComponentTag.HSV_V
        """
        HSV V value.
        """
        HSL_H = ColorComponentTag.HSL_H
        """
        HSL H value.
        """
        HSL_S = ColorComponentTag.HSL_S
        """
        HSL S value.
        """
        HSL_L = ColorComponentTag.HSL_L
        """
        HSL L value.
        """
        YCBCR_Y = ColorComponentTag.YCBCR_Y
        """
        YCbCr Y value.
        """
        YCBCR_CB = ColorComponentTag.YCBCR_CB
        """
        YCbCr Cb value.
        """
        YCBCR_CR = ColorComponentTag.YCBCR_CR
        """
        YCbCr Cr value.
        """

__all__ = ['ColorComponentTag', 'ColorComponentTagEnum']
