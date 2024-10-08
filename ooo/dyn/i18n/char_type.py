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
# Namespace: com.sun.star.i18n
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

    class CharType(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.CharType", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.CharType``"""
        pass

    class CharTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.CharType", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.CharType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.i18n import CharType as CharType
    else:
        # keep document generators happy
        from ...lo.i18n.char_type import CharType as CharType

    class CharTypeEnum(IntEnum):
        """
        Enum of Const Class CharType

        Constants to specify the character type that starts a character block.
        
        Character type is Unicode type defined in UnicodeType
        
        Used with XBreakIterator.beginOfCharBlock(), XBreakIterator.endOfCharBlock(), XBreakIterator.nextCharBlock(), XBreakIterator.previousCharBlock()
        """
        ANY_CHAR = CharType.ANY_CHAR
        """
        all alpha characters allowed
        """
        UPPERCASE_LETTER = CharType.UPPERCASE_LETTER
        LOWERCASE_LETTER = CharType.LOWERCASE_LETTER
        TITLECASE_LETTER = CharType.TITLECASE_LETTER
        MODIFIER_LETTER = CharType.MODIFIER_LETTER
        OTHER_LETTER = CharType.OTHER_LETTER
        NON_SPACING_MARK = CharType.NON_SPACING_MARK
        ENCLOSING_MARK = CharType.ENCLOSING_MARK
        COMBINING_SPACING_MARK = CharType.COMBINING_SPACING_MARK
        DECIMAL_DIGIT_NUMBER = CharType.DECIMAL_DIGIT_NUMBER
        LETTER_NUMBER = CharType.LETTER_NUMBER
        OTHER_NUMBER = CharType.OTHER_NUMBER
        SPACE_SEPARATOR = CharType.SPACE_SEPARATOR
        LINE_SEPARATOR = CharType.LINE_SEPARATOR
        PARAGRAPH_SEPARATOR = CharType.PARAGRAPH_SEPARATOR
        CONTROL = CharType.CONTROL
        FORMAT = CharType.FORMAT
        PRIVATE_USE = CharType.PRIVATE_USE
        SURROGATE = CharType.SURROGATE
        DASH_PUNCTUATION = CharType.DASH_PUNCTUATION
        START_PUNCTUATION = CharType.START_PUNCTUATION
        END_PUNCTUATION = CharType.END_PUNCTUATION
        CONNECTOR_PUNCTUATION = CharType.CONNECTOR_PUNCTUATION
        OTHER_PUNCTUATION = CharType.OTHER_PUNCTUATION
        MATH_SYMBOL = CharType.MATH_SYMBOL
        CURRENCY_SYMBOL = CharType.CURRENCY_SYMBOL
        MODIFIER_SYMBOL = CharType.MODIFIER_SYMBOL
        OTHER_SYMBOL = CharType.OTHER_SYMBOL
        INITIAL_PUNCTUATION = CharType.INITIAL_PUNCTUATION
        FINAL_PUNCTUATION = CharType.FINAL_PUNCTUATION
        GENERAL_TYPES_COUNT = CharType.GENERAL_TYPES_COUNT

__all__ = ['CharType', 'CharTypeEnum']
