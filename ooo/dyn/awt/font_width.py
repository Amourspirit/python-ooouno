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
# Namespace: com.sun.star.awt
import uno
from enum import Enum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FontWidth(metaclass=UnoConstMeta, type_name="com.sun.star.awt.FontWidth", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.FontWidth``"""
        pass

    class FontWidthEnum(Enum, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.FontWidth", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.FontWidth`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.awt import FontWidth as FontWidth
    else:
        # keep document generators happy
        from ...lo.awt.font_width import FontWidth as FontWidth

    class FontWidthEnum(Enum):
        """
        Enum of Const Class FontWidth

        These values are used to specify the width of the characters of a font.
        
        They may be expanded in future versions.
        """
        DONTKNOW = FontWidth.DONTKNOW
        """
        The width of the font is not specified/known.
        """
        ULTRACONDENSED = FontWidth.ULTRACONDENSED
        """
        The width of the font is condensed to 50%.
        """
        EXTRACONDENSED = FontWidth.EXTRACONDENSED
        """
        The width of the font is condensed to 60%.
        """
        CONDENSED = FontWidth.CONDENSED
        """
        The width of the font is condensed to 75%.
        """
        SEMICONDENSED = FontWidth.SEMICONDENSED
        """
        The width of the font is condensed to 90%.
        """
        NORMAL = FontWidth.NORMAL
        """
        The width of the font is normal.
        """
        SEMIEXPANDED = FontWidth.SEMIEXPANDED
        """
        The width of the font is expanded to 110%.
        """
        EXPANDED = FontWidth.EXPANDED
        """
        The width of the font is expanded to 150%.
        """
        EXTRAEXPANDED = FontWidth.EXTRAEXPANDED
        """
        The width of the font is expanded to 175%.
        """
        ULTRAEXPANDED = FontWidth.ULTRAEXPANDED
        """
        The width of the font is expanded to 200%.
        """

__all__ = ['FontWidth', 'FontWidthEnum']
