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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .solver_constraint_operator import SolverConstraintOperator as SolverConstraintOperator_6e4a110d
from ..table.cell_address import CellAddress as CellAddress_ae5f0b56


class SolverConstraint(object):
    """
    Struct Class

    is used to specify a constraint for a solver model.

    See Also:
        `API SolverConstraint <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1SolverConstraint.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SolverConstraint'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.SolverConstraint'
    """Literal Constant ``com.sun.star.sheet.SolverConstraint``"""

    def __init__(self, Left: typing.Optional[CellAddress_ae5f0b56] = UNO_NONE, Operator: typing.Optional[SolverConstraintOperator_6e4a110d] = SolverConstraintOperator_6e4a110d.LESS_EQUAL, Right: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Left (CellAddress, optional): Left value.
            Operator (SolverConstraintOperator, optional): Operator value.
            Right (object, optional): Right value.
        """
        super().__init__()

        if isinstance(Left, SolverConstraint):
            oth: SolverConstraint = Left
            self.Left = oth.Left
            self.Operator = oth.Operator
            self.Right = oth.Right
            return

        kargs = {
            "Left": Left,
            "Operator": Operator,
            "Right": Right,
        }
        if kargs["Left"] is UNO_NONE:
            kargs["Left"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._left = kwargs["Left"]
        self._operator = kwargs["Operator"]
        self._right = kwargs["Right"]


    @property
    def Left(self) -> CellAddress_ae5f0b56:
        """
        The address of the cell that is constrained.
        """
        return self._left

    @Left.setter
    def Left(self, value: CellAddress_ae5f0b56) -> None:
        self._left = value

    @property
    def Operator(self) -> SolverConstraintOperator_6e4a110d:
        """
        The type of the constraint.
        """
        return self._operator

    @Operator.setter
    def Operator(self, value: SolverConstraintOperator_6e4a110d) -> None:
        self._operator = value

    @property
    def Right(self) -> object:
        """
        The comparison value, of type double or com.sun.star.table.CellAddress.
        """
        return self._right

    @Right.setter
    def Right(self, value: object) -> None:
        self._right = value


__all__ = ['SolverConstraint']
