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


class TablePageBreakData(object):
    """
    Struct Class

    describes a page break in a spreadsheet.

    See Also:
        `API TablePageBreakData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1TablePageBreakData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.TablePageBreakData'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.TablePageBreakData'
    """Literal Constant ``com.sun.star.sheet.TablePageBreakData``"""

    def __init__(self, Position: typing.Optional[int] = 0, ManualBreak: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Position (int, optional): Position value.
            ManualBreak (bool, optional): ManualBreak value.
        """
        super().__init__()
        kargs = {
            "Position": Position,
            "ManualBreak": ManualBreak,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._position = kwargs["Position"]
        self._manual_break = kwargs["ManualBreak"]


    @property
    def Position(self) -> int:
        """
        the position (column or row index) of the page break.
        """
        return self._position
    
    @Position.setter
    def Position(self, value: int) -> None:
        self._position = value

    @property
    def ManualBreak(self) -> bool:
        """
        is TRUE for a manual page break, FALSE for an automatic one.
        """
        return self._manual_break
    
    @ManualBreak.setter
    def ManualBreak(self, value: bool) -> None:
        self._manual_break = value


__all__ = ['TablePageBreakData']
