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
# Namespace: com.sun.star.linguistic2
import uno
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ConversionDictionaryType(metaclass=UnoConstMeta, type_name="com.sun.star.linguistic2.ConversionDictionaryType", name_space="com.sun.star.linguistic2"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.linguistic2.ConversionDictionaryType``"""
        pass

    class ConversionDictionaryTypeEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.linguistic2.ConversionDictionaryType", name_space="com.sun.star.linguistic2"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.linguistic2.ConversionDictionaryType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.linguistic2 import ConversionDictionaryType as ConversionDictionaryType
    else:
        # keep document generators happy
        from ...lo.linguistic2.conversion_dictionary_type import ConversionDictionaryType as ConversionDictionaryType

    class ConversionDictionaryTypeEnum(IntFlag):
        """
        Enum of Const Class ConversionDictionaryType

        specifies the conversion dictionary type to be used with XConversionDictionary.
        
        **since**
        
            OOo 1.1.2
        """
        HANGUL_HANJA = ConversionDictionaryType.HANGUL_HANJA
        """
        Dictionary type for the conversion between Hangul and Hanja.
        """
        SCHINESE_TCHINESE = ConversionDictionaryType.SCHINESE_TCHINESE
        """
        Dictionary type for the conversion between Simplified and Traditional Chinese.
        
        **since**
        
            OOo 2.0
        """

__all__ = ['ConversionDictionaryType', 'ConversionDictionaryTypeEnum']
