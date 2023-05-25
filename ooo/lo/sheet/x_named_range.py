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
from __future__ import annotations
import typing
from abc import abstractmethod
from ..container.x_named import XNamed as XNamed_a6520b08
if typing.TYPE_CHECKING:
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56

class XNamedRange(XNamed_a6520b08):
    """
    provides access to the settings of a named range in a spreadsheet document.

    See Also:
        `API XNamedRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XNamedRange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XNamedRange'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XNamedRange'

    @abstractmethod
    def getContent(self) -> str:
        """
        returns the content of the named range.
        
        The content can be a reference to a cell or cell range or any formula expression.
        """
        ...
    @abstractmethod
    def getReferencePosition(self) -> CellAddress_ae5f0b56:
        """
        returns the position in the document which is used as a base for relative references in the content.
        """
        ...
    @abstractmethod
    def getType(self) -> int:
        """
        returns the type of the named range.
        
        This is a combination of flags as defined in NamedRangeFlag.
        """
        ...
    @abstractmethod
    def setContent(self, aContent: str) -> None:
        """
        sets the content of the named range.
        
        The content can be a reference to a cell or cell range or any formula expression.
        """
        ...
    @abstractmethod
    def setReferencePosition(self, aReferencePosition: CellAddress_ae5f0b56) -> None:
        """
        sets the position in the document which is used as a base for relative references in the content.
        """
        ...
    @abstractmethod
    def setType(self, nType: int) -> None:
        """
        sets the type of the named range.
        """
        ...

__all__ = ['XNamedRange']


