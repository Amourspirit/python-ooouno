# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56

class XAreaLinks(XIndexAccess_f0910d6d):
    """
    provides access via index to a collection of area links and inserting and removing area links.

    See Also:
        `API XAreaLinks <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XAreaLinks.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XAreaLinks'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XAreaLinks'

    @abstractmethod
    def insertAtPosition(self, aDestPos: 'CellAddress_ae5f0b56', aFileName: str, aSourceArea: str, aFilter: str, aFilterOptions: str) -> None:
        """
        creates an area link and adds it to the collection.
        
        This can be the address of a cell or range in the form \"Sheet1.A1:C5\", or the name of a named range or database range.
        """
        ...
    @abstractmethod
    def removeByIndex(self, nIndex: int) -> None:
        """
        removes an area link from the collection.
        """
        ...

__all__ = ['XAreaLinks']

