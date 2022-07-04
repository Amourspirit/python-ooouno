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
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class TextGridMode(metaclass=UnoConstMeta, type_name="com.sun.star.text.TextGridMode", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.TextGridMode``"""
        pass

    class TextGridModeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.TextGridMode", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.TextGridMode`` as Enum values"""
        pass

else:
    from ...lo.text.text_grid_mode import TextGridMode as TextGridMode

    class TextGridModeEnum(IntEnum):
        """
        Enum of Const Class TextGridMode

        this set of constants describes different modes for text grids
        """
        NONE = TextGridMode.NONE
        """
        no text grid
        """
        LINES = TextGridMode.LINES
        """
        line positions will be determined by the grid
        """
        LINES_AND_CHARS = TextGridMode.LINES_AND_CHARS
        """
        character and line positions will be determined by the grid
        """

__all__ = ['TextGridMode', 'TextGridModeEnum']
