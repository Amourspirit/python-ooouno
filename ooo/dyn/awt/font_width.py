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
    from com.sun.star.awt import FontWidth as FontWidth
    if hasattr(FontWidth, '_constants') and isinstance(FontWidth._constants, dict):
        FontWidth._constants['__ooo_ns__'] = 'com.sun.star.awt'
        FontWidth._constants['__ooo_full_ns__'] = 'com.sun.star.awt.FontWidth'
        FontWidth._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global FontWidthEnum
        ls = [f for f in dir(FontWidth) if not callable(getattr(FontWidth, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(FontWidth, name)
        FontWidthEnum = IntEnum('FontWidthEnum', _dict)
    build_enum()
else:
    from ...lo.awt.font_width import FontWidth as FontWidth

    class FontWidthEnum(IntEnum):
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
