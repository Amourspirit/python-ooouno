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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .condition_operator import ConditionOperator as ConditionOperator_fec90e14
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56

class XSheetCondition(XInterface_8f010a43):
    """
    provides methods to access the settings of a condition in a conditional format or data validation.

    See Also:
        `API XSheetCondition <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetCondition.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetCondition'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetCondition'

    @abstractmethod
    def getFormula1(self) -> str:
        """
        returns either the comparison value, which is used in the condition, or the first value if two values are needed for the operator.
        """
        ...
    @abstractmethod
    def getFormula2(self) -> str:
        """
        if two values are needed for the operator, this method returns the second one.
        """
        ...
    @abstractmethod
    def getOperator(self) -> 'ConditionOperator_fec90e14':
        """
        returns the operator in the condition.
        """
        ...
    @abstractmethod
    def getSourcePosition(self) -> 'CellAddress_ae5f0b56':
        """
        returns the position in the document which is used as a base for relative references in the formulas.
        """
        ...
    @abstractmethod
    def setFormula1(self, aFormula1: str) -> None:
        """
        sets either the comparison value, which is used in the condition, or the first value if two values are needed for the operator.
        """
        ...
    @abstractmethod
    def setFormula2(self, aFormula2: str) -> None:
        """
        if two values are needed for the operator, this method sets the second one.
        """
        ...
    @abstractmethod
    def setOperator(self, nOperator: 'ConditionOperator_fec90e14') -> None:
        """
        sets the operator in the condition.
        """
        ...
    @abstractmethod
    def setSourcePosition(self, aSourcePosition: 'CellAddress_ae5f0b56') -> None:
        """
        sets the position in the document which is used as a base for relative references in the formulas.
        """
        ...

__all__ = ['XSheetCondition']

