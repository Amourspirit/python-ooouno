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
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class KCharacterType(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.KCharacterType", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.KCharacterType``"""
        pass

    class KCharacterTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.KCharacterType", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.KCharacterType`` as Enum values"""
        pass

else:
    from ...lo.i18n.k_character_type import KCharacterType as KCharacterType

    class KCharacterTypeEnum(IntEnum):
        """
        Enum of Const Class KCharacterType

        Constants to identify the character type.
        
        Returned by XCharacterClassification.getCharacterType() and XCharacterClassification.getStringType()
        """
        DIGIT = KCharacterType.DIGIT
        """
        digit
        """
        UPPER = KCharacterType.UPPER
        """
        upper case alpha letter
        """
        LOWER = KCharacterType.LOWER
        """
        lower case alpha letter
        """
        TITLE_CASE = KCharacterType.TITLE_CASE
        """
        title case alpha letter
        """
        ALPHA = KCharacterType.ALPHA
        """
        any alpha, ALPHA = UPPER | LOWER | TITLE_CASE
        """
        CONTROL = KCharacterType.CONTROL
        """
        control character
        """
        PRINTABLE = KCharacterType.PRINTABLE
        """
        printable character
        """
        BASE_FORM = KCharacterType.BASE_FORM
        """
        base form
        """
        LETTER = KCharacterType.LETTER
        """
        any UnicodeType...._LETTER.
        
        Note that a LETTER must not necessarily be ALPHA
        """

__all__ = ['KCharacterType', 'KCharacterTypeEnum']
