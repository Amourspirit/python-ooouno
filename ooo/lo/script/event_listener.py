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
# Namespace: com.sun.star.script
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .x_all_listener import XAllListener as XAllListener_c91b0c54


class EventListener(object):
    """
    Struct Class


    See Also:
        `API EventListener <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1EventListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.EventListener'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.EventListener'
    """Literal Constant ``com.sun.star.script.EventListener``"""

    def __init__(self, AllListener: typing.Optional[XAllListener_c91b0c54] = None, Helper: typing.Optional[object] = None, ListenerType: typing.Optional[str] = '', AddListenerParam: typing.Optional[str] = '', EventMethod: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            AllListener (XAllListener, optional): AllListener value.
            Helper (object, optional): Helper value.
            ListenerType (str, optional): ListenerType value.
            AddListenerParam (str, optional): AddListenerParam value.
            EventMethod (str, optional): EventMethod value.
        """
        super().__init__()

        if isinstance(AllListener, EventListener):
            oth: EventListener = AllListener
            self.AllListener = oth.AllListener
            self.Helper = oth.Helper
            self.ListenerType = oth.ListenerType
            self.AddListenerParam = oth.AddListenerParam
            self.EventMethod = oth.EventMethod
            return

        kargs = {
            "AllListener": AllListener,
            "Helper": Helper,
            "ListenerType": ListenerType,
            "AddListenerParam": AddListenerParam,
            "EventMethod": EventMethod,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._all_listener = kwargs["AllListener"]
        self._helper = kwargs["Helper"]
        self._listener_type = kwargs["ListenerType"]
        self._add_listener_param = kwargs["AddListenerParam"]
        self._event_method = kwargs["EventMethod"]


    @property
    def AllListener(self) -> XAllListener_c91b0c54:
        return self._all_listener

    @AllListener.setter
    def AllListener(self, value: XAllListener_c91b0c54) -> None:
        self._all_listener = value

    @property
    def Helper(self) -> object:
        return self._helper

    @Helper.setter
    def Helper(self, value: object) -> None:
        self._helper = value

    @property
    def ListenerType(self) -> str:
        return self._listener_type

    @ListenerType.setter
    def ListenerType(self, value: str) -> None:
        self._listener_type = value

    @property
    def AddListenerParam(self) -> str:
        return self._add_listener_param

    @AddListenerParam.setter
    def AddListenerParam(self, value: str) -> None:
        self._add_listener_param = value

    @property
    def EventMethod(self) -> str:
        return self._event_method

    @EventMethod.setter
    def EventMethod(self, value: str) -> None:
        self._event_method = value


__all__ = ['EventListener']
