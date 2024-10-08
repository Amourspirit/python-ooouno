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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.script.vba
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class VBAEventId(metaclass=UnoConstMeta, type_name="com.sun.star.script.vba.VBAEventId", name_space="com.sun.star.script.vba"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.script.vba.VBAEventId``"""
        pass

    class VBAEventIdEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.script.vba.VBAEventId", name_space="com.sun.star.script.vba"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.script.vba.VBAEventId`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.script.vba import VBAEventId as VBAEventId
    else:
        # keep document generators happy
        from ....lo.script.vba.vba_event_id import VBAEventId as VBAEventId

    class VBAEventIdEnum(IntEnum):
        """
        Enum of Const Class VBAEventId

        Constants used to identify VBA document events.
        
        If one of these events is fired, a specific VBA macro in a specific document code module will be executed.
        
        Each event expects some specific arguments to be passed to XVBAEventProcessor.processVbaEvent().
        """
        NO_EVENT = VBAEventId.NO_EVENT
        """
        An identifier not corresponding to any VBA document event.
        """
        AUTO_NEW = VBAEventId.AUTO_NEW
        """
        New document opened from template.
        
        No arguments.
        """
        AUTO_OPEN = VBAEventId.AUTO_OPEN
        """
        Document opened (loaded).
        
        No arguments.
        """
        AUTO_CLOSE = VBAEventId.AUTO_CLOSE
        """
        Document about to be closed.
        
        No arguments.
        """
        AUTO_EXEC = VBAEventId.AUTO_EXEC
        """
        Application start.
        
        No arguments.
        """
        AUTO_EXIT = VBAEventId.AUTO_EXIT
        """
        Application exit.
        
        No arguments.
        """
        DOCUMENT_NEW = VBAEventId.DOCUMENT_NEW
        """
        New text document opened from template.
        
        No arguments.
        """
        DOCUMENT_OPEN = VBAEventId.DOCUMENT_OPEN
        """
        Text document opened (loaded).
        
        No arguments.
        """
        DOCUMENT_CLOSE = VBAEventId.DOCUMENT_CLOSE
        """
        Document about to be closed.
        
        No arguments.
        """
        WORKBOOK_ACTIVATE = VBAEventId.WORKBOOK_ACTIVATE
        """
        Document activated.
        
        No arguments.
        """
        WORKBOOK_DEACTIVATE = VBAEventId.WORKBOOK_DEACTIVATE
        """
        Document deactivated.
        
        No arguments.
        """
        WORKBOOK_OPEN = VBAEventId.WORKBOOK_OPEN
        """
        Document opened (loaded).
        
        No arguments.
        """
        WORKBOOK_BEFORECLOSE = VBAEventId.WORKBOOK_BEFORECLOSE
        """
        Document about to be closed.
        
        Arguments: [out] boolean bCancel.
        """
        WORKBOOK_BEFOREPRINT = VBAEventId.WORKBOOK_BEFOREPRINT
        """
        Document about to be printed.
        
        Arguments: [out] boolean bCancel.
        """
        WORKBOOK_BEFORESAVE = VBAEventId.WORKBOOK_BEFORESAVE
        """
        Document about to be saved.
        
        Arguments: boolean bSaveAs, [out] boolean bCancel.
        """
        WORKBOOK_AFTERSAVE = VBAEventId.WORKBOOK_AFTERSAVE
        """
        Document has been saved.
        
        Arguments: boolean bSuccess.
        """
        WORKBOOK_NEWSHEET = VBAEventId.WORKBOOK_NEWSHEET
        """
        New sheet inserted.
        
        Arguments: short nSheet.
        """
        WORKBOOK_WINDOWACTIVATE = VBAEventId.WORKBOOK_WINDOWACTIVATE
        """
        Document window has been activated.
        
        Arguments: XController aController.
        """
        WORKBOOK_WINDOWDEACTIVATE = VBAEventId.WORKBOOK_WINDOWDEACTIVATE
        """
        Document window has been deactivated.
        
        Arguments: XController aController.
        """
        WORKBOOK_WINDOWRESIZE = VBAEventId.WORKBOOK_WINDOWRESIZE
        """
        Document window has been resized.
        
        Arguments: XController aController.
        """
        WORKSHEET_ACTIVATE = VBAEventId.WORKSHEET_ACTIVATE
        """
        Worksheet has been activated (made visible).
        
        Arguments: short nSheet.
        """
        WORKSHEET_DEACTIVATE = VBAEventId.WORKSHEET_DEACTIVATE
        """
        Worksheet has been deactivated (made not visible).
        
        Arguments: short nSheet.
        """
        WORKSHEET_BEFOREDOUBLECLICK = VBAEventId.WORKSHEET_BEFOREDOUBLECLICK
        """
        Double click in the sheet.
        
        Arguments: XRange/XSheetCellRangeContainer aRange, [out] boolean bCancel.
        """
        WORKSHEET_BEFORERIGHTCLICK = VBAEventId.WORKSHEET_BEFORERIGHTCLICK
        """
        Right click in the sheet.
        
        Arguments: XRange/XSheetCellRangeContainer aRange, [out] boolean bCancel.
        """
        WORKSHEET_CALCULATE = VBAEventId.WORKSHEET_CALCULATE
        """
        Cells in sheet have been recalculated.
        
        Arguments: short nSheet.
        """
        WORKSHEET_CHANGE = VBAEventId.WORKSHEET_CHANGE
        """
        Cells in sheet have been changed.
        
        Arguments: XRange/XSheetCellRangeContainer aRange.
        """
        WORKSHEET_SELECTIONCHANGE = VBAEventId.WORKSHEET_SELECTIONCHANGE
        """
        Selection in sheet has been changed.
        
        Arguments: XRange/XSheetCellRangeContainer aRange.
        """
        WORKSHEET_FOLLOWHYPERLINK = VBAEventId.WORKSHEET_FOLLOWHYPERLINK
        """
        Hyperlink has been clicked.
        
        Arguments: XCell aCell.
        """
        USERDEFINED_START = VBAEventId.USERDEFINED_START
        """
        Implementations are allowed to use identifiers above this value for any internal purpose.
        """

__all__ = ['VBAEventId', 'VBAEventIdEnum']
