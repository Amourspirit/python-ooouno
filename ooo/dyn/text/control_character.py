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
# Namespace: com.sun.star.text
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

    class ControlCharacter(metaclass=UnoConstMeta, type_name="com.sun.star.text.ControlCharacter", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.ControlCharacter``"""
        pass

    class ControlCharacterEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.ControlCharacter", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.ControlCharacter`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.text import ControlCharacter as ControlCharacter
    else:
        # keep document generators happy
        from ...lo.text.control_character import ControlCharacter as ControlCharacter

    class ControlCharacterEnum(IntEnum):
        """
        Enum of Const Class ControlCharacter

        These constants are the codes for inserting control characters using XSimpleText.insertControlCharacter() interface.
        """
        PARAGRAPH_BREAK = ControlCharacter.PARAGRAPH_BREAK
        """
        This control character starts a new paragraph.
        """
        LINE_BREAK = ControlCharacter.LINE_BREAK
        """
        This control character starts a new line in a paragraph.
        """
        HARD_HYPHEN = ControlCharacter.HARD_HYPHEN
        """
        This control character equals a dash but prevents this position from being hyphenated.
        """
        SOFT_HYPHEN = ControlCharacter.SOFT_HYPHEN
        """
        This control character defines a special position as a hyphenation point.
        
        If a word containing a soft hyphen must be split at the end of a line, then this position is preferred.
        """
        HARD_SPACE = ControlCharacter.HARD_SPACE
        """
        This control character is used to link two words and prevents this concatenation from being hyphenated.
        
        It is printed as a space.
        """
        APPEND_PARAGRAPH = ControlCharacter.APPEND_PARAGRAPH
        """
        This control character appends a new paragraph.
        """

__all__ = ['ControlCharacter', 'ControlCharacterEnum']
