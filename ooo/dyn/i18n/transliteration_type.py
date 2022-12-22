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

    class TransliterationType(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.TransliterationType", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.TransliterationType``"""
        pass

    class TransliterationTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.TransliterationType", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.TransliterationType`` as Enum values"""
        pass

else:
    from ...lo.i18n.transliteration_type import TransliterationType as TransliterationType

    class TransliterationTypeEnum(IntEnum):
        """
        Enum of Const Class TransliterationType

        Bitmask transliteration types used with XTransliteration.getType() and XTransliteration.getAvailableModules() methods.
        
        Non-IGNORE type modules provide XTransliteration.transliterate(). IGNORE type modules provide XTransliteration.equals() and XTransliteration.transliterateRange().
        """
        NONE = TransliterationType.NONE
        ONE_TO_ONE = TransliterationType.ONE_TO_ONE
        """
        A transliteration module is ONE_TO_ONE if and only if it's mapping between characters is one to one like a-z to A-Z.
        
        Transliteration modules of this type can be used as choice in regular expressions based search/replace.
        """
        NUMERIC = TransliterationType.NUMERIC
        """
        A transliteration module can have attribute NUMERIC if it transliterates numbers in different languages like Chinese numbers to Arabic numbers and vice versa.
        
        This mapping need not be one to one, it should be primarily used by number formatting and parsing methods.
        """
        ONE_TO_ONE_NUMERIC = TransliterationType.ONE_TO_ONE_NUMERIC
        """
        A transliteration module is ONE_TO_ONE_NUMERIC if it offers both one to one mapping and handles number also.
        """
        IGNORE = TransliterationType.IGNORE
        """
        With a transliteration IGNORE case, the regular expression A-Z can be transformed to a-z, for example.
        """
        CASCADE = TransliterationType.CASCADE
        """
        If the transliteration is cascaded (uses more than one algorithm).
        """

__all__ = ['TransliterationType', 'TransliterationTypeEnum']
