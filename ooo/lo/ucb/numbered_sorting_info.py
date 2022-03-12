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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class NumberedSortingInfo(object):
    """
    Struct Class

    contains information for sorting a ContentResultSet.
    
    In contrast to the struct SortingInfo this struct is used to be on the safe side, that no one asks for sorting by a property which is not contained in a ContentResultSet.

    See Also:
        `API NumberedSortingInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1NumberedSortingInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.NumberedSortingInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.NumberedSortingInfo'
    """Literal Constant ``com.sun.star.ucb.NumberedSortingInfo``"""

    def __init__(self, ColumnIndex: typing.Optional[int] = 0, Ascending: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            ColumnIndex (int, optional): ColumnIndex value.
            Ascending (bool, optional): Ascending value.
        """
        super().__init__()
        kargs = {
            "ColumnIndex": ColumnIndex,
            "Ascending": Ascending,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._column_index = kwargs["ColumnIndex"]
        self._ascending = kwargs["Ascending"]


    @property
    def ColumnIndex(self) -> int:
        """
        sort the result set by this column.
        
        Index starts with 1.
        """
        return self._column_index
    
    @ColumnIndex.setter
    def ColumnIndex(self, value: int) -> None:
        self._column_index = value

    @property
    def Ascending(self) -> bool:
        """
        contains a flag indicating the sort mode (ascending or descending).
        """
        return self._ascending
    
    @Ascending.setter
    def Ascending(self, value: bool) -> None:
        self._ascending = value


__all__ = ['NumberedSortingInfo']
