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
# Namespace: com.sun.star.i18n
from enum import IntEnum
from ...lo.i18n.unicode_type import UnicodeType as UnicodeType


class UnicodeTypeEnum(IntEnum):
    """
    Enum of Const Class UnicodeType

    Constants to classify Unicode characters, returned by XCharacterClassification.getType()
    """
    UNASSIGNED = UnicodeType.UNASSIGNED
    UPPERCASE_LETTER = UnicodeType.UPPERCASE_LETTER
    LOWERCASE_LETTER = UnicodeType.LOWERCASE_LETTER
    TITLECASE_LETTER = UnicodeType.TITLECASE_LETTER
    MODIFIER_LETTER = UnicodeType.MODIFIER_LETTER
    OTHER_LETTER = UnicodeType.OTHER_LETTER
    NON_SPACING_MARK = UnicodeType.NON_SPACING_MARK
    ENCLOSING_MARK = UnicodeType.ENCLOSING_MARK
    COMBINING_SPACING_MARK = UnicodeType.COMBINING_SPACING_MARK
    DECIMAL_DIGIT_NUMBER = UnicodeType.DECIMAL_DIGIT_NUMBER
    LETTER_NUMBER = UnicodeType.LETTER_NUMBER
    OTHER_NUMBER = UnicodeType.OTHER_NUMBER
    SPACE_SEPARATOR = UnicodeType.SPACE_SEPARATOR
    LINE_SEPARATOR = UnicodeType.LINE_SEPARATOR
    PARAGRAPH_SEPARATOR = UnicodeType.PARAGRAPH_SEPARATOR
    CONTROL = UnicodeType.CONTROL
    FORMAT = UnicodeType.FORMAT
    PRIVATE_USE = UnicodeType.PRIVATE_USE
    SURROGATE = UnicodeType.SURROGATE
    DASH_PUNCTUATION = UnicodeType.DASH_PUNCTUATION
    INITIAL_PUNCTUATION = UnicodeType.INITIAL_PUNCTUATION
    FINAL_PUNCTUATION = UnicodeType.FINAL_PUNCTUATION
    CONNECTOR_PUNCTUATION = UnicodeType.CONNECTOR_PUNCTUATION
    OTHER_PUNCTUATION = UnicodeType.OTHER_PUNCTUATION
    MATH_SYMBOL = UnicodeType.MATH_SYMBOL
    CURRENCY_SYMBOL = UnicodeType.CURRENCY_SYMBOL
    MODIFIER_SYMBOL = UnicodeType.MODIFIER_SYMBOL
    OTHER_SYMBOL = UnicodeType.OTHER_SYMBOL
    START_PUNCTUATION = UnicodeType.START_PUNCTUATION
    END_PUNCTUATION = UnicodeType.END_PUNCTUATION
    GENERAL_TYPES_COUNT = UnicodeType.GENERAL_TYPES_COUNT

__all__ = ['UnicodeType', 'UnicodeTypeEnum']
