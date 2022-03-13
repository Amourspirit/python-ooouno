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
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class PropertyInfo(object):
    """
    Struct Class

    This structure contains all the information related to a property.

    See Also:
        `API PropertyInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1configuration_1_1backend_1_1PropertyInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.PropertyInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.configuration.backend.PropertyInfo'
    """Literal Constant ``com.sun.star.configuration.backend.PropertyInfo``"""

    def __init__(self, Name: typing.Optional[str] = '', Type: typing.Optional[str] = '', Value: typing.Optional[object] = None, Protected: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Type (str, optional): Type value.
            Value (object, optional): Value value.
            Protected (bool, optional): Protected value.
        """
        super().__init__()

        if isinstance(Name, PropertyInfo):
            oth: PropertyInfo = Name
            self.Name = oth.Name
            self.Type = oth.Type
            self.Value = oth.Value
            self.Protected = oth.Protected
            return

        kargs = {
            "Name": Name,
            "Type": Type,
            "Value": Value,
            "Protected": Protected,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._type = kwargs["Type"]
        self._value = kwargs["Value"]
        self._protected = kwargs["Protected"]


    @property
    def Name(self) -> str:
        """
        The full name of the Property for eg.
        
        org.openoffice.Inet/Settings/ooInetHTTPProxyName
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Type(self) -> str:
        """
        The type of the Property.
        """
        return self._type
    
    @Type.setter
    def Type(self, value: str) -> None:
        self._type = value

    @property
    def Value(self) -> object:
        """
        The value of the property.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value

    @property
    def Protected(self) -> bool:
        """
        Is the property protected, if true the property can not be over written in later layer.
        """
        return self._protected
    
    @Protected.setter
    def Protected(self, value: bool) -> None:
        self._protected = value


__all__ = ['PropertyInfo']
