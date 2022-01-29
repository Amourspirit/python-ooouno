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
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class PropertyInfo(object):
    """
    Struct Class

    This structure contains all the information related to a property.

    See Also:
        `API PropertyInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1configuration_1_1backend_1_1PropertyInfo.html>`_


    Note:
        | At runtime PropertyInfo will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | PropertyInfo is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Name: typing.Optional[str] = None, Protected: typing.Optional[bool] = None, Type: typing.Optional[str] = None, Value: typing.Optional[object] = None):
        self._name = Name
        self._protected = Protected
        self._type = Type
        self._value = Value

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
    def Protected(self) -> bool:
        """
        Is the property protected, if true the property can not be over written in later layer.
        """
        return self._protected
    
    @Protected.setter
    def Protected(self, value: bool) -> None:
        self._protected = value

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

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global PropertyInfo
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Name', 'Protected', 'Type', 'Value')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.configuration.backend.PropertyInfo')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        PropertyInfo = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['PropertyInfo']
