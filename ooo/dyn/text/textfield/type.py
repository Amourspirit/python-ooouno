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
# Namespace: com.sun.star.text.textfield
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

    class Type(metaclass=UnoConstMeta, type_name="com.sun.star.text.textfield.Type", name_space="com.sun.star.text.textfield"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.textfield.Type``"""
        pass

    class TypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.textfield.Type", name_space="com.sun.star.text.textfield"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.textfield.Type`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.text.textfield import Type as Type
    else:
        # keep document generators happy
        from ....lo.text.textfield.type import Type as Type

    class TypeEnum(IntEnum):
        """
        Enum of Const Class Type

        Text field types.
        
        Right now this only contains the types that are supported by the edit engine, but it should eventually contain all field types that are used across all engines.
        
        **since**
        
            LibreOffice 3.6
        """
        UNSPECIFIED = Type.UNSPECIFIED
        DATE = Type.DATE
        URL = Type.URL
        PAGE = Type.PAGE
        PAGES = Type.PAGES
        TIME = Type.TIME
        TABLE = Type.TABLE
        EXTENDED_TIME = Type.EXTENDED_TIME
        EXTENDED_FILE = Type.EXTENDED_FILE
        AUTHOR = Type.AUTHOR
        MEASURE = Type.MEASURE
        DOCINFO_TITLE = Type.DOCINFO_TITLE
        PRESENTATION_HEADER = Type.PRESENTATION_HEADER
        PRESENTATION_FOOTER = Type.PRESENTATION_FOOTER
        PRESENTATION_DATE_TIME = Type.PRESENTATION_DATE_TIME
        PAGE_NAME = Type.PAGE_NAME
        DOCINFO_CUSTOM = Type.DOCINFO_CUSTOM

__all__ = ['Type', 'TypeEnum']
