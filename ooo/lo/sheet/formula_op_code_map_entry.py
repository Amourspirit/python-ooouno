# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .formula_token import FormulaToken as FormulaToken_bd1c0bf8


class FormulaOpCodeMapEntry(object):
    """
    Struct Class

    contains a mapping from a formula name (function name, operator, ...) to the OpCode used by the formula compiler.

    See Also:
        `API FormulaOpCodeMapEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1FormulaOpCodeMapEntry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FormulaOpCodeMapEntry'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.FormulaOpCodeMapEntry'
    """Literal Constant ``com.sun.star.sheet.FormulaOpCodeMapEntry``"""

    def __init__(self, Name: typing.Optional[str] = '', Token: typing.Optional[FormulaToken_bd1c0bf8] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Token (FormulaToken, optional): Token value.
        """
        super().__init__()

        if isinstance(Name, FormulaOpCodeMapEntry):
            oth: FormulaOpCodeMapEntry = Name
            self.Name = oth.Name
            self.Token = oth.Token
            return

        kargs = {
            "Name": Name,
            "Token": Token,
        }
        if kargs["Token"] is UNO_NONE:
            kargs["Token"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._token = kwargs["Token"]


    @property
    def Name(self) -> str:
        """
        The function name, or operator.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Token(self) -> FormulaToken_bd1c0bf8:
        """
        The corresponding mapping.
        """
        return self._token

    @Token.setter
    def Token(self, value: FormulaToken_bd1c0bf8) -> None:
        self._token = value


__all__ = ['FormulaOpCodeMapEntry']
