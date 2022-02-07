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

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``FormulaOpCodeMapEntry`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``FormulaOpCodeMapEntry``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Name (str, optional): Name value
            Token (FormulaToken, optional): Token value
        """
        self._name = None
        self._token = None

        key_order = ('Name', 'Token')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], FormulaOpCodeMapEntry):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("FormulaOpCodeMapEntry.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


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
    def Token(self) -> 'FormulaToken_bd1c0bf8':
        """
        The corresponding mapping.
        """
        return self._token
    
    @Token.setter
    def Token(self, value: 'FormulaToken_bd1c0bf8') -> None:
        self._token = value


__all__ = ['FormulaOpCodeMapEntry']
