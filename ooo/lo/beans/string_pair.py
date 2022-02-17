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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.beans
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class StringPair(object):
    """
    Struct Class

    specifies a pair of two strings.

    See Also:
        `API StringPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1StringPair.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.StringPair'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.StringPair'
    """Literal Constant ``com.sun.star.beans.StringPair``"""

    def __init__(self, First: str = '', Second: str = '') -> None:
        """
        Constructor

        Other Arguments:
            ``First`` can be another ``StringPair`` instance,
                in which case other named args are ignored.

        Arguments:
            First (str, optional): First value
            Second (str, optional): Second value
        """
        if isinstance(First, StringPair):
            oth: StringPair = First
            self._first = oth.First
            self._second = oth.Second
            return
        else:
            self._first = First
            self._second = Second



    @property
    def First(self) -> str:
        """
        specifies the first of the two strings.
        """
        return self._first
    
    @First.setter
    def First(self, value: str) -> None:
        self._first = value

    @property
    def Second(self) -> str:
        """
        specifies the second of the two strings.
        """
        return self._second
    
    @Second.setter
    def Second(self, value: str) -> None:
        self._second = value


__all__ = ['StringPair']
