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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class HomogenMatrixLine(object):
    """
    Struct Class

    specifies a single line for a HomogenMatrix.

    See Also:
        `API HomogenMatrixLine <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1HomogenMatrixLine.html>`_


    Note:
        | At runtime HomogenMatrixLine will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | HomogenMatrixLine is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Column1: typing.Optional[float] = None, Column2: typing.Optional[float] = None, Column3: typing.Optional[float] = None, Column4: typing.Optional[float] = None):
        self._column1 = Column1
        self._column2 = Column2
        self._column3 = Column3
        self._column4 = Column4

    @property
    def Column1(self) -> float:
        return self._column1
    
    @Column1.setter
    def Column1(self, value: float) -> None:
        self._column1 = value

    @property
    def Column2(self) -> float:
        return self._column2
    
    @Column2.setter
    def Column2(self, value: float) -> None:
        self._column2 = value

    @property
    def Column3(self) -> float:
        return self._column3
    
    @Column3.setter
    def Column3(self, value: float) -> None:
        self._column3 = value

    @property
    def Column4(self) -> float:
        return self._column4
    
    @Column4.setter
    def Column4(self, value: float) -> None:
        self._column4 = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global HomogenMatrixLine
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Column1', 'Column2', 'Column3', 'Column4')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.drawing.HomogenMatrixLine')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        HomogenMatrixLine = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['HomogenMatrixLine']
