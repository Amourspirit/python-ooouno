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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2.data
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.chart2.data.LabelOrigin import (COLUMN, LONG_SIDE, ROW, SHORT_SIDE)

if TYPE_CHECKING or _DYNAMIC is False:


    class LabelOrigin(Enum):
        """
        Enum Class

        

        See Also:
            `API LabelOrigin <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2_1_1data.html#a2afe9ba95ad4b3631057b40391bed0aa>`_
        """
        COLUMN = 'COLUMN'
        """
        Uses the column name for label generation.
        
        A spreadsheet range A1:A6 could, e.g., result in \"Column A\".
        
        If a range consists of more than one column the result of label generation may be empty. Of course, it could also succeed with a string like \"Columns A to B\".
        """
        LONG_SIDE = 'LONG_SIDE'
        """
        This is exactly the opposite of SHORT_SIDE.
        
        I.e., if SHORT_SIDE has the same effect as ROW, LONG_SIDE will have the same effect as COLUMN and the other way round.
        """
        ROW = 'ROW'
        """
        Uses the column name for label generation.
        
        A spreadsheet range A2:D2 could, e.g., result in \"Row 2\".
        
        If a range consists of more than one row the result of label generation may be empty. Of course, it could also succeed with a string like \"Rows 1-3\".
        """
        SHORT_SIDE = 'SHORT_SIDE'
        """
        If a range spans a single row over more than one column, this parameter has the same effect as ROW.
        
        If the range spans a single column over more than one row, this is the same as COLUMN.
        
        In case of a range spanning more than one column and row, the shorter range of both should be used (e.g. a spreadsheet range A1:B10 should treat columns as short side).
        
        In case of a rectangular range, or a range that is composed of more than one contiguous sub-regions, the short side cannot be determined, thus XDataSequence.generateLabel() will return an empty sequence.
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global LabelOrigin
        _dict = {
            "COLUMN": COLUMN,
            "LONG_SIDE": LONG_SIDE,
            "ROW": ROW,
            "SHORT_SIDE": SHORT_SIDE,
        }

        LabelOrigin = type('LabelOrigin', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(LabelOrigin, k, v)

    _dynamic_enum()

__all__ = ['LabelOrigin']

