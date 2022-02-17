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
from ooo.oenv import UNO_NONE
import typing


class HomogenMatrixLine3(object):
    """
    Struct Class

    specifies a single line for a HomogenMatrix3.

    See Also:
        `API HomogenMatrixLine3 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1HomogenMatrixLine3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.HomogenMatrixLine3'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.HomogenMatrixLine3'
    """Literal Constant ``com.sun.star.drawing.HomogenMatrixLine3``"""

    def __init__(self, Column1: float = 0.0, Column2: float = 0.0, Column3: float = 0.0) -> None:
        """
        Constructor

        Other Arguments:
            ``Column1`` can be another ``HomogenMatrixLine3`` instance,
                in which case other named args are ignored.

        Arguments:
            Column1 (float, optional): Column1 value
            Column2 (float, optional): Column2 value
            Column3 (float, optional): Column3 value
        """
        if isinstance(Column1, HomogenMatrixLine3):
            oth: HomogenMatrixLine3 = Column1
            self._column1 = oth.Column1
            self._column2 = oth.Column2
            self._column3 = oth.Column3
            return
        else:
            self._column1 = Column1
            self._column2 = Column2
            self._column3 = Column3



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


__all__ = ['HomogenMatrixLine3']