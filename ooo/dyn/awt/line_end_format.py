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
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class LineEndFormat(metaclass=UnoConstMeta, type_name="com.sun.star.awt.LineEndFormat", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.LineEndFormat``"""
        pass

    class LineEndFormatEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.LineEndFormat", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.LineEndFormat`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.awt import LineEndFormat as LineEndFormat
    else:
        # keep document generators happy
        from ...lo.awt.line_end_format import LineEndFormat as LineEndFormat

    class LineEndFormatEnum(IntEnum):
        """
        Enum of Const Class LineEndFormat

        These values are used to specify which line end format should be used in strings.
        """
        CARRIAGE_RETURN = LineEndFormat.CARRIAGE_RETURN
        """
        specifies that line ends are to be represented by a carriage return character (\\\\\r)
        """
        LINE_FEED = LineEndFormat.LINE_FEED
        """
        specifies that line ends are to be represented by a line feed character (\\\\\n)
        """
        CARRIAGE_RETURN_LINE_FEED = LineEndFormat.CARRIAGE_RETURN_LINE_FEED
        """
        specifies that line ends are to be represented by a line feed character (\\\\\n), followed by a carriage return character (\\\\\r).
        """

__all__ = ['LineEndFormat', 'LineEndFormatEnum']
