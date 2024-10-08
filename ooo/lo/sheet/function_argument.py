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


class FunctionArgument(object):
    """
    Struct Class

    contains the description of a single argument within a spreadsheet function.

    See Also:
        `API FunctionArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1FunctionArgument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FunctionArgument'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.FunctionArgument'
    """Literal Constant ``com.sun.star.sheet.FunctionArgument``"""

    def __init__(self, Name: typing.Optional[str] = '', Description: typing.Optional[str] = '', IsOptional: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Description (str, optional): Description value.
            IsOptional (bool, optional): IsOptional value.
        """
        super().__init__()

        if isinstance(Name, FunctionArgument):
            oth: FunctionArgument = Name
            self.Name = oth.Name
            self.Description = oth.Description
            self.IsOptional = oth.IsOptional
            return

        kargs = {
            "Name": Name,
            "Description": Description,
            "IsOptional": IsOptional,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._description = kwargs["Description"]
        self._is_optional = kwargs["IsOptional"]


    @property
    def Name(self) -> str:
        """
        the name of the argument.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Description(self) -> str:
        """
        a description of the argument.
        """
        return self._description

    @Description.setter
    def Description(self, value: str) -> None:
        self._description = value

    @property
    def IsOptional(self) -> bool:
        """
        determines whether the argument is optional.
        """
        return self._is_optional

    @IsOptional.setter
    def IsOptional(self, value: bool) -> None:
        self._is_optional = value


__all__ = ['FunctionArgument']
