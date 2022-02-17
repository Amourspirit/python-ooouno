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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class CellProtection(object):
    """
    Struct Class

    describes the kind of protection for a protectable cell.

    See Also:
        `API CellProtection <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1CellProtection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.CellProtection'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.CellProtection'
    """Literal Constant ``com.sun.star.util.CellProtection``"""

    def __init__(self, IsLocked: bool = False, IsFormulaHidden: bool = False, IsHidden: bool = False, IsPrintHidden: bool = False) -> None:
        """
        Constructor

        Other Arguments:
            ``IsLocked`` can be another ``CellProtection`` instance,
                in which case other named args are ignored.

        Arguments:
            IsLocked (bool, optional): IsLocked value
            IsFormulaHidden (bool, optional): IsFormulaHidden value
            IsHidden (bool, optional): IsHidden value
            IsPrintHidden (bool, optional): IsPrintHidden value
        """
        if isinstance(IsLocked, CellProtection):
            oth: CellProtection = IsLocked
            self._is_locked = oth.IsLocked
            self._is_formula_hidden = oth.IsFormulaHidden
            self._is_hidden = oth.IsHidden
            self._is_print_hidden = oth.IsPrintHidden
            return
        else:
            self._is_locked = IsLocked
            self._is_formula_hidden = IsFormulaHidden
            self._is_hidden = IsHidden
            self._is_print_hidden = IsPrintHidden



    @property
    def IsLocked(self) -> bool:
        """
        specifies if the cell is locked from modifications by the user.
        """
        return self._is_locked
    
    @IsLocked.setter
    def IsLocked(self, value: bool) -> None:
        self._is_locked = value

    @property
    def IsFormulaHidden(self) -> bool:
        """
        specifies if the formula is hidden from the user.
        """
        return self._is_formula_hidden
    
    @IsFormulaHidden.setter
    def IsFormulaHidden(self, value: bool) -> None:
        self._is_formula_hidden = value

    @property
    def IsHidden(self) -> bool:
        """
        specifies if the cell is hidden from the user.
        """
        return self._is_hidden
    
    @IsHidden.setter
    def IsHidden(self, value: bool) -> None:
        self._is_hidden = value

    @property
    def IsPrintHidden(self) -> bool:
        """
        specifies if the cell is hidden on printouts.
        """
        return self._is_print_hidden
    
    @IsPrintHidden.setter
    def IsPrintHidden(self, value: bool) -> None:
        self._is_print_hidden = value


__all__ = ['CellProtection']
