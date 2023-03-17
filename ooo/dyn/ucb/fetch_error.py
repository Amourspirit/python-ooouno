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
# Libre Office Version: 7.4
# Namespace: com.sun.star.ucb
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FetchError(metaclass=UnoConstMeta, type_name="com.sun.star.ucb.FetchError", name_space="com.sun.star.ucb"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.ucb.FetchError``"""
        pass

    class FetchErrorEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.ucb.FetchError", name_space="com.sun.star.ucb"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.ucb.FetchError`` as Enum values"""
        pass

else:
    from ...lo.ucb.fetch_error import FetchError as FetchError

    class FetchErrorEnum(IntEnum):
        """
        Enum of Const Class FetchError

        These values are used to specify whether and which error has occurred while fetching data of some ContentResultSet rows.
        """
        SUCCESS = FetchError.SUCCESS
        """
        indicates that fetching of data was successful.
        """
        ENDOFDATA = FetchError.ENDOFDATA
        """
        indicates that during fetching we went beyond the last or first row.
        
        Therefore the FetchResult does not contain the full count of demanded rows, but the maximum possible count must be contained.
        """
        EXCEPTION = FetchError.EXCEPTION
        """
        indicates that during fetching we got an exception.
        
        The row, that causes the exception, and all following ( \"following\" in read order! ) rows are not contained in the FetchResult. Therefore the FetchResult does not contain the full count of demanded rows. But all properly read rows so far must be contained.
        """

__all__ = ['FetchError', 'FetchErrorEnum']
