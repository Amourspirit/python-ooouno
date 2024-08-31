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
from abc import abstractmethod, ABC

class XGlobalSheetSettings(ABC):
    """
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XGlobalSheetSettings <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XGlobalSheetSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XGlobalSheetSettings'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XGlobalSheetSettings'

    @property
    @abstractmethod
    def DoAutoComplete(self) -> bool:
        """
        specifies whether automatic completion of text in a cell is used.
        """
        ...

    @property
    @abstractmethod
    def EnterEdit(self) -> bool:
        """
        specifies whether the enter key can be used to start editing a cell.
        """
        ...

    @property
    @abstractmethod
    def ExpandReferences(self) -> bool:
        """
        specifies whether formula references are extended when cells are inserted below or to the right of them.
        """
        ...

    @property
    @abstractmethod
    def ExtendFormat(self) -> bool:
        """
        specifies whether cell formatting is extended when entering data.
        """
        ...

    @property
    @abstractmethod
    def LinkUpdateMode(self) -> int:
        """
        specifies the update mode for external linked data.
        
        0 = always
        
        1 = never
        
        2 = on demand
        """
        ...

    @property
    @abstractmethod
    def MarkHeader(self) -> bool:
        """
        specifies whether the current selection is highlighted in column and row headers.
        """
        ...

    @property
    @abstractmethod
    def Metric(self) -> int:
        """
        contains the metric for all spreadsheet documents.
        """
        ...

    @property
    @abstractmethod
    def MoveDirection(self) -> int:
        """
        contains the direction the cursor moves after entering cells.
        """
        ...

    @property
    @abstractmethod
    def MoveSelection(self) -> bool:
        """
        specifies whether the cursor is moved after entering into cells.
        """
        ...

    @property
    @abstractmethod
    def PrintAllSheets(self) -> bool:
        """
        specifies whether all sheets or only selected sheets are printed.
        """
        ...

    @property
    @abstractmethod
    def PrintEmptyPages(self) -> bool:
        """
        specifies whether empty pages are printed.
        """
        ...

    @property
    @abstractmethod
    def RangeFinder(self) -> bool:
        """
        specifies whether ranges are highlighted on the sheet when editing a formula.
        """
        ...

    @property
    @abstractmethod
    def ReplaceCellsWarning(self) -> bool:
        """
        specifies whether a warning is shown before replacing cells (i.e.
        
        when pasting from clipboard).
        """
        ...

    @property
    @abstractmethod
    def Scale(self) -> int:
        """
        contains the default scale for new spreadsheet documents (in percent).
        
        There are several special values:
        
        -1 = Optimal width
        
        -2 = Show whole page
        
        -3 = Page width
        """
        ...

    @property
    @abstractmethod
    def StatusBarFunction(self) -> int:
        """
        contains the function that is displayed in the status bar.
        """
        ...

    @property
    @abstractmethod
    def UsePrinterMetrics(self) -> bool:
        """
        specifies whether printer metrics are used for display.
        """
        ...

    @property
    @abstractmethod
    def UseTabCol(self) -> bool:
        """
        specifies whether the enter key moves the cursor to the column it was in before using the tab key to change columns.
        """
        ...

    @property
    @abstractmethod
    def UserLists(self) -> typing.Tuple[str, ...]:
        """
        contains the string lists used for sorting and filling.
        
        Each string contains the members of a list, separated by commas.
        """
        ...


__all__ = ['XGlobalSheetSettings']

