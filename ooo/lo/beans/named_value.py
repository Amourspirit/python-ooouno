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
# Namespace: com.sun.star.beans
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class NamedValue(object):
    """
    Struct Class

    specifies a pair assembled from a name and a value.

    See Also:
        `API NamedValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1NamedValue.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.NamedValue'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.NamedValue'
    """Literal Constant ``com.sun.star.beans.NamedValue``"""

    def __init__(self, Name: typing.Optional[str] = '', Value: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Value (object, optional): Value value.
        """
        super().__init__()

        if isinstance(Name, NamedValue):
            oth: NamedValue = Name
            self.Name = oth.Name
            self.Value = oth.Value
            return

        kargs = {
            "Name": Name,
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._value = kwargs["Value"]


    @property
    def Name(self) -> str:
        """
        specifies the name part of the pair
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Value(self) -> object:
        """
        specifies the value part of the pair.
        """
        return self._value

    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value


__all__ = ['NamedValue']
