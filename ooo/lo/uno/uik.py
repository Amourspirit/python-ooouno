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
# Namespace: com.sun.star.uno
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class Uik(object):
    """
    Struct Class

    Specifies a universal interface key (globally unique).
    
    This struct is deprecated. Uiks are not used anymore.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API Uik <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1uno_1_1Uik.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.Uik'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.uno.Uik'
    """Literal Constant ``com.sun.star.uno.Uik``"""

    def __init__(self, Data1: int = 0, Data2: int = 0, Data3: int = 0, Data4: int = 0, Data5: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``Data1`` can be another ``Uik`` instance,
                in which case other named args are ignored.

        Arguments:
            Data1 (int, optional): Data1 value
            Data2 (int, optional): Data2 value
            Data3 (int, optional): Data3 value
            Data4 (int, optional): Data4 value
            Data5 (int, optional): Data5 value
        """
        if isinstance(Data1, Uik):
            oth: Uik = Data1
            self._data1 = oth.Data1
            self._data2 = oth.Data2
            self._data3 = oth.Data3
            self._data4 = oth.Data4
            self._data5 = oth.Data5
            return
        else:
            self._data1 = Data1
            self._data2 = Data2
            self._data3 = Data3
            self._data4 = Data4
            self._data5 = Data5



    @property
    def Data1(self) -> int:
        """
        specifies a 4 byte data block.
        """
        return self._data1
    
    @Data1.setter
    def Data1(self, value: int) -> None:
        self._data1 = value

    @property
    def Data2(self) -> int:
        """
        specifies a 2 byte data block.
        """
        return self._data2
    
    @Data2.setter
    def Data2(self, value: int) -> None:
        self._data2 = value

    @property
    def Data3(self) -> int:
        """
        specifies a 2 byte data block.
        """
        return self._data3
    
    @Data3.setter
    def Data3(self, value: int) -> None:
        self._data3 = value

    @property
    def Data4(self) -> int:
        """
        specifies a 4 byte data block.
        """
        return self._data4
    
    @Data4.setter
    def Data4(self, value: int) -> None:
        self._data4 = value

    @property
    def Data5(self) -> int:
        """
        specifies a 4 byte data block.
        """
        return self._data5
    
    @Data5.setter
    def Data5(self, value: int) -> None:
        self._data5 = value


__all__ = ['Uik']
