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
# Namespace: com.sun.star.text
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FontEmphasis(metaclass=UnoConstMeta, type_name="com.sun.star.text.FontEmphasis", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.FontEmphasis``"""
        pass

    class FontEmphasisEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.FontEmphasis", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.FontEmphasis`` as Enum values"""
        pass

else:
    from ...lo.text.font_emphasis import FontEmphasis as FontEmphasis

    class FontEmphasisEnum(IntEnum):
        """
        Enum of Const Class FontEmphasis

        Determines the type and position of an emphasis mark in Asian texts.
        """
        NONE = FontEmphasis.NONE
        """
        no emphasis mark is used.
        """
        DOT_ABOVE = FontEmphasis.DOT_ABOVE
        """
        a dot is set above (or right from vertical text) the text.
        """
        CIRCLE_ABOVE = FontEmphasis.CIRCLE_ABOVE
        """
        a circle is set above (or right from vertical text) the text.
        """
        DISK_ABOVE = FontEmphasis.DISK_ABOVE
        """
        a disc is set above (or right from vertical text) the text.
        """
        ACCENT_ABOVE = FontEmphasis.ACCENT_ABOVE
        """
        an accent is set above (or right from vertical text) the text.
        """
        DOT_BELOW = FontEmphasis.DOT_BELOW
        """
        a dot is set below (or left from vertical text) the text.
        """
        CIRCLE_BELOW = FontEmphasis.CIRCLE_BELOW
        """
        a circle is set below (or left from vertical text) the text.
        """
        DISK_BELOW = FontEmphasis.DISK_BELOW
        """
        a disk is set below (or left from vertical text) the text.
        """
        ACCENT_BELOW = FontEmphasis.ACCENT_BELOW
        """
        an accent is set below (or left from vertical text) the text.
        """

__all__ = ['FontEmphasis', 'FontEmphasisEnum']
