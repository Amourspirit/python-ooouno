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


class FormulaToken(object):
    """
    Struct Class

    contains a single token within a formula.

    See Also:
        `API FormulaToken <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1FormulaToken.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FormulaToken'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.FormulaToken'
    """Literal Constant ``com.sun.star.sheet.FormulaToken``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``FormulaToken`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``FormulaToken``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            OpCode (int, optional): OpCode value
            Data (object, optional): Data value
        """
        self._op_code = None
        self._data = None

        key_order = ('OpCode', 'Data')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], FormulaToken):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("FormulaToken.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def OpCode(self) -> int:
        """
        is the OpCode of the token.
        """
        return self._op_code
    
    @OpCode.setter
    def OpCode(self, value: int) -> None:
        self._op_code = value

    @property
    def Data(self) -> object:
        """
        is additional data in the token, depending on the OpCode.
        """
        return self._data
    
    @Data.setter
    def Data(self, value: object) -> None:
        self._data = value


__all__ = ['FormulaToken']
