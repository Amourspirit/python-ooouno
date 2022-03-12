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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class DataResult(object):
    """
    Struct Class

    contains the result of one element in the data pilot data array.

    See Also:
        `API DataResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DataResult'
    """Literal Constant ``com.sun.star.sheet.DataResult``"""

    def __init__(self, Flags: typing.Optional[int] = 0, Value: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            Flags (int, optional): Flags value.
            Value (float, optional): Value value.
        """
        super().__init__()
        kargs = {
            "Flags": Flags,
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._flags = kwargs["Flags"]
        self._value = kwargs["Value"]


    @property
    def Flags(self) -> int:
        """
        contains boolean flags describing the result.
        """
        return self._flags
    
    @Flags.setter
    def Flags(self, value: int) -> None:
        self._flags = value

    @property
    def Value(self) -> float:
        """
        contains the result value.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: float) -> None:
        self._value = value


__all__ = ['DataResult']
