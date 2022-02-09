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
import typing
if typing.TYPE_CHECKING:
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


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``SolverConstraint`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``SolverConstraint``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Left (CellAddress, optional): Left value
            Operator (SolverConstraintOperator, optional): Operator value
            Right (object, optional): Right value
        """
        self._left = None
        self._operator = None
        self._right = None

        key_order = ('Left', 'Operator', 'Right')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], SolverConstraint):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("SolverConstraint.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Left(self) -> 'CellAddress_ae5f0b56':
        """
        The address of the cell that is constrained.
        """
        return self._left
    
    @Left.setter
    def Left(self, value: 'CellAddress_ae5f0b56') -> None:
        self._left = value

    @property
    def Operator(self) -> 'SolverConstraintOperator_6e4a110d':
        """
        The type of the constraint.
        """
        return self._operator
    
    @Operator.setter
    def Operator(self, value: 'SolverConstraintOperator_6e4a110d') -> None:
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
