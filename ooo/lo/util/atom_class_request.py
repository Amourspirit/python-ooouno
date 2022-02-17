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


class AtomClassRequest(object):
    """
    Struct Class

    is used to describe which atoms the user wants to know about.

    See Also:
        `API AtomClassRequest <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1AtomClassRequest.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.AtomClassRequest'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.AtomClassRequest'
    """Literal Constant ``com.sun.star.util.AtomClassRequest``"""

    def __init__(self, atoms: typing.Tuple[int, ...] = UNO_NONE, atomClass: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``atoms`` can be another ``AtomClassRequest`` instance,
                in which case other named args are ignored.

        Arguments:
            atoms (Tuple[int, ...], optional): atoms value
            atomClass (int, optional): atomClass value
        """
        if isinstance(atoms, AtomClassRequest):
            oth: AtomClassRequest = atoms
            self._atoms = oth.atoms
            self._atom_class = oth.atomClass
            return
        else:
            if atoms is UNO_NONE:
                self._atoms = None
            else:
                self._atoms = atoms
            self._atom_class = atomClass



    @property
    def atoms(self) -> typing.Tuple[int, ...]:
        """
        the atoms requested from class AtomClassRequest.atomClass().
        """
        return self._atoms
    
    @atoms.setter
    def atoms(self, value: typing.Tuple[int, ...]) -> None:
        self._atoms = value

    @property
    def atomClass(self) -> int:
        """
        the class of the atoms described in member AtomClassRequest.atoms().
        """
        return self._atom_class
    
    @atomClass.setter
    def atomClass(self, value: int) -> None:
        self._atom_class = value


__all__ = ['AtomClassRequest']