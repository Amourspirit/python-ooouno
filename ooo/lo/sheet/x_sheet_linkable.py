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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from com.sun.star.sheet.SheetLinkMode import SheetLinkModeProto  # type: ignore

class XSheetLinkable(XInterface_8f010a43):
    """
    enables a sheet to refer to another sheet in a different document.
    
    To insert a sheet link, the sheet used as linked sheet has to exist already. The method XSheetLinkable.link() creates a SheetLink object in the document's SheetLinks collection and links the sheet to the specified external sheet.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XSheetLinkable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetLinkable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetLinkable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetLinkable'

    @abstractmethod
    def getLinkMode(self) -> SheetLinkModeProto:
        """
        returns the link mode of the spreadsheet.
        
        If the returned value is SheetLinkMode.NORMAL, formulas are copied. With SheetLinkMode.VALUE, only results of formulas are used.
        """
        ...
    @abstractmethod
    def getLinkSheetName(self) -> str:
        """
        returns the sheet name of the sheet in the source document.
        """
        ...
    @abstractmethod
    def getLinkUrl(self) -> str:
        """
        returns the target URL of the link.
        """
        ...
    @abstractmethod
    def link(self, aUrl: str, aSheetName: str, aFilterName: str, aFilterOptions: str, nMode: SheetLinkModeProto) -> None:
        """
        links the sheet to another sheet in another document.
        
        A SheetLink object is created if it does not exist, and the link mode, the URL of the linked document and the linked sheet name are set.
        """
        ...
    @abstractmethod
    def setLinkMode(self, nLinkMode: SheetLinkModeProto) -> None:
        """
        enables the linking of the sheet and controls whether formulas are copied.
        
        If the value is SheetLinkMode.NORMAL, formulas are copied. With SheetLinkMode.VALUE, only results of formulas are used.
        """
        ...
    @abstractmethod
    def setLinkSheetName(self, aLinkSheetName: str) -> None:
        """
        sets the name of the linked sheet in the source document.
        
        This method sets the sheet name in the SheetLink object, it does not modify the sheet name in the source document.
        """
        ...
    @abstractmethod
    def setLinkUrl(self, aLinkUrl: str) -> None:
        """
        sets the target URL of the link.
        
        A SheetLink object with the same file name must exist already or the link will not work.
        """
        ...

__all__ = ['XSheetLinkable']