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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from abc import abstractproperty
from ..util.sort_descriptor import SortDescriptor as SortDescriptor_ca680c8d

class TextSortDescriptor(SortDescriptor_ca680c8d):
    """
    Service Class

    describes sort criteria for sorting text.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API TextSortDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextSortDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextSortDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Delimiter(self) -> str:
        """
        contains the character that marks the separation of columns.
        """
    @abstractproperty
    def IsSortAscending0(self) -> bool:
        """
        determines if the sorting in the first search key is done in ascending or descending order.
        """
    @abstractproperty
    def IsSortAscending1(self) -> bool:
        """
        determines if the sorting in the second search key is done in ascending or descending order.
        """
    @abstractproperty
    def IsSortAscending2(self) -> bool:
        """
        determines if the sorting in the third search key is done in ascending or descending order.
        """
    @abstractproperty
    def IsSortInTable(self) -> bool:
        """
        determines if the content of a table is to be sorted.
        """
    @abstractproperty
    def IsSortNumeric0(self) -> bool:
        """
        determines if the sorting in the first search key is done numeric or alphanumeric order.
        """
    @abstractproperty
    def IsSortNumeric1(self) -> bool:
        """
        determines if the sorting in the second search key is done in numeric or alphanumeric order.
        """
    @abstractproperty
    def IsSortNumeric2(self) -> bool:
        """
        determines if the sorting in the third search key is done in numeric or alphanumeric order.
        """
    @abstractproperty
    def SortRowOrColumnNo0(self) -> int:
        """
        contains the row or column index used in the first search key.
        """
    @abstractproperty
    def SortRowOrColumnNo1(self) -> int:
        """
        contains the row or column index used in the second search key.
        """
    @abstractproperty
    def SortRowOrColumnNo2(self) -> int:
        """
        contains the row or column index used in the third search key.
        """

__all__ = ['TextSortDescriptor']

