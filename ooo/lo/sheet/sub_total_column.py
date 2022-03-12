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
from .general_function import GeneralFunction as GeneralFunction_e2280d25


class SubTotalColumn(object):
    """
    Struct Class

    describes how a single data column is treated when creating subtotals.

    See Also:
        `API SubTotalColumn <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1SubTotalColumn.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SubTotalColumn'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.SubTotalColumn'
    """Literal Constant ``com.sun.star.sheet.SubTotalColumn``"""

    def __init__(self, Column: typing.Optional[int] = 0, Function: typing.Optional[GeneralFunction_e2280d25] = GeneralFunction_e2280d25.NONE) -> None:
        """
        Constructor

        Arguments:
            Column (int, optional): Column value.
            Function (GeneralFunction, optional): Function value.
        """
        super().__init__()
        kargs = {
            "Column": Column,
            "Function": Function,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._column = kwargs["Column"]
        self._function = kwargs["Function"]


    @property
    def Column(self) -> int:
        """
        the index of the column inside the source data area.
        """
        return self._column
    
    @Column.setter
    def Column(self, value: int) -> None:
        self._column = value

    @property
    def Function(self) -> GeneralFunction_e2280d25:
        """
        specifies what kind of subtotals are calculated.
        """
        return self._function
    
    @Function.setter
    def Function(self, value: GeneralFunction_e2280d25) -> None:
        self._function = value


__all__ = ['SubTotalColumn']
