# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.style
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

    class LineSpacingMode(metaclass=UnoConstMeta, type_name="com.sun.star.style.LineSpacingMode", name_space="com.sun.star.style"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.style.LineSpacingMode``"""
        pass

    class LineSpacingModeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.style.LineSpacingMode", name_space="com.sun.star.style"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.style.LineSpacingMode`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.style import LineSpacingMode as LineSpacingMode
    else:
        # keep document generators happy
        from ...lo.style.line_spacing_mode import LineSpacingMode as LineSpacingMode

    class LineSpacingModeEnum(IntEnum):
        """
        Enum of Const Class LineSpacingMode

        These constants specify the interpretation of LineHeight.
        """
        PROP = LineSpacingMode.PROP
        """
        This constant specifies the height value as a proportional value.
        """
        MINIMUM = LineSpacingMode.MINIMUM
        """
        This constant specifies the height as the minimum line height.
        """
        LEADING = LineSpacingMode.LEADING
        """
        This constant specifies the height value as the distance to the previous line.
        """
        FIX = LineSpacingMode.FIX
        """
        This constant specifies the height value as a fixed line height.
        """

__all__ = ['LineSpacingMode', 'LineSpacingModeEnum']
