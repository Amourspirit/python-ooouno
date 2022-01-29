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
import os
import typing
if typing.TYPE_CHECKING:
    from .general_function import GeneralFunction as GeneralFunction_e2280d25
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class SubTotalColumn(object):
    """
    Struct Class

    describes how a single data column is treated when creating subtotals.

    See Also:
        `API SubTotalColumn <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1SubTotalColumn.html>`_


    Note:
        | At runtime SubTotalColumn will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | SubTotalColumn is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Column: typing.Optional[int] = None, Function: 'typing.Optional[GeneralFunction_e2280d25]' = None):
        self._column = Column
        self._function = Function

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
    def Function(self) -> 'GeneralFunction_e2280d25':
        """
        specifies what kind of subtotals are calculated.
        """
        return self._function
    
    @Function.setter
    def Function(self, value: 'GeneralFunction_e2280d25') -> None:
        self._function = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global SubTotalColumn
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Column', 'Function')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.sheet.SubTotalColumn')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        SubTotalColumn = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['SubTotalColumn']
