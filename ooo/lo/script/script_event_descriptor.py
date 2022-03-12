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
# Namespace: com.sun.star.script
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class ScriptEventDescriptor(object):
    """
    Struct Class

    describes an effect, especially a script to be executed, for a certain event given by the listener type and the name of the event method.

    See Also:
        `API ScriptEventDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1ScriptEventDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.ScriptEventDescriptor'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.ScriptEventDescriptor'
    """Literal Constant ``com.sun.star.script.ScriptEventDescriptor``"""

    def __init__(self, ListenerType: typing.Optional[str] = '', EventMethod: typing.Optional[str] = '', AddListenerParam: typing.Optional[str] = '', ScriptType: typing.Optional[str] = '', ScriptCode: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            ListenerType (str, optional): ListenerType value.
            EventMethod (str, optional): EventMethod value.
            AddListenerParam (str, optional): AddListenerParam value.
            ScriptType (str, optional): ScriptType value.
            ScriptCode (str, optional): ScriptCode value.
        """
        super().__init__()
        kargs = {
            "ListenerType": ListenerType,
            "EventMethod": EventMethod,
            "AddListenerParam": AddListenerParam,
            "ScriptType": ScriptType,
            "ScriptCode": ScriptCode,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._listener_type = kwargs["ListenerType"]
        self._event_method = kwargs["EventMethod"]
        self._add_listener_param = kwargs["AddListenerParam"]
        self._script_type = kwargs["ScriptType"]
        self._script_code = kwargs["ScriptCode"]


    @property
    def ListenerType(self) -> str:
        """
        listener type as string, same as listener-XIdlClass.getName().
        """
        return self._listener_type
    
    @ListenerType.setter
    def ListenerType(self, value: str) -> None:
        self._listener_type = value

    @property
    def EventMethod(self) -> str:
        """
        event method as string.
        """
        return self._event_method
    
    @EventMethod.setter
    def EventMethod(self, value: str) -> None:
        self._event_method = value

    @property
    def AddListenerParam(self) -> str:
        """
        data to be used if the addListener method needs an additional parameter.
        
        If the type of this parameter is different from string, it will be converted, when added.
        """
        return self._add_listener_param
    
    @AddListenerParam.setter
    def AddListenerParam(self, value: str) -> None:
        self._add_listener_param = value

    @property
    def ScriptType(self) -> str:
        """
        type of the script language as string; for example, \"Basic\" or \"StarScript\".
        """
        return self._script_type
    
    @ScriptType.setter
    def ScriptType(self, value: str) -> None:
        self._script_type = value

    @property
    def ScriptCode(self) -> str:
        """
        script code as string (the code has to correspond with the language defined by ScriptType).
        """
        return self._script_code
    
    @ScriptCode.setter
    def ScriptCode(self, value: str) -> None:
        self._script_code = value


__all__ = ['ScriptEventDescriptor']
