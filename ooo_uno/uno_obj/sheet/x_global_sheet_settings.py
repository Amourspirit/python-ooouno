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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty, ABC

class XGlobalSheetSettings(ABC):
    """
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XGlobalSheetSettings <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XGlobalSheetSettings.html>`_
    """

    @abstractproperty
    def DoAutoComplete(self) -> bool:
        """
        specifies whether automatic completion of text in a cell is used.
        """
    @abstractproperty
    def EnterEdit(self) -> bool:
        """
        specifies whether the enter key can be used to start editing a cell.
        """
    @abstractproperty
    def ExpandReferences(self) -> bool:
        """
        specifies whether formula references are extended when cells are inserted below or to the right of them.
        """
    @abstractproperty
    def ExtendFormat(self) -> bool:
        """
        specifies whether cell formatting is extended when entering data.
        """
    @abstractproperty
    def LinkUpdateMode(self) -> int:
        """
        specifies the update mode for external linked data.
        
        0 = always
        
        1 = never
        
        2 = on demand
        """
    @abstractproperty
    def MarkHeader(self) -> bool:
        """
        specifies whether the current selection is highlighted in column and row headers.
        """
    @abstractproperty
    def Metric(self) -> int:
        """
        contains the metric for all spreadsheet documents.
        """
    @abstractproperty
    def MoveDirection(self) -> int:
        """
        contains the direction the cursor moves after entering cells.
        """
    @abstractproperty
    def MoveSelection(self) -> bool:
        """
        specifies whether the cursor is moved after entering into cells.
        """
    @abstractproperty
    def PrintAllSheets(self) -> bool:
        """
        specifies whether all sheets or only selected sheets are printed.
        """
    @abstractproperty
    def PrintEmptyPages(self) -> bool:
        """
        specifies whether empty pages are printed.
        """
    @abstractproperty
    def RangeFinder(self) -> bool:
        """
        specifies whether ranges are highlighted on the sheet when editing a formula.
        """
    @abstractproperty
    def ReplaceCellsWarning(self) -> bool:
        """
        specifies whether a warning is shown before replacing cells (i.e.
        
        when pasting from clipboard).
        """
    @abstractproperty
    def Scale(self) -> int:
        """
        contains the default scale for new spreadsheet documents (in percent).
        
        There are several special values:
        
        -1 = Optimal width
        
        -2 = Show whole page
        
        -3 = Page width
        """
    @abstractproperty
    def StatusBarFunction(self) -> int:
        """
        contains the function that is displayed in the status bar.
        """
    @abstractproperty
    def UsePrinterMetrics(self) -> bool:
        """
        specifies whether printer metrics are used for display.
        """
    @abstractproperty
    def UseTabCol(self) -> bool:
        """
        specifies whether the enter key moves the cursor to the column it was in before using the tab key to change columns.
        """
    @abstractproperty
    def UserLists(self) -> 'typing.List[str]':
        """
        contains the string lists used for sorting and filling.
        
        Each string contains the members of a list, separated by commas.
        """

__all__ = ['XGlobalSheetSettings']

