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
# Namespace: com.sun.star.ui
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..container.container_event import ContainerEvent as ContainerEvent_ea50e70
import typing


class ConfigurationEvent(ContainerEvent_ea50e70):
    """
    Struct Class

    this event is broadcasted by a configuration manager whenever the state of user interface element has changed.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ConfigurationEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1ConfigurationEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.ConfigurationEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ui.ConfigurationEvent'
    """Literal Constant ``com.sun.star.ui.ConfigurationEvent``"""

    def __init__(self, ResourceURL: str = '', aInfo: object = None, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``ResourceURL`` can be another ``ConfigurationEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            ResourceURL (str, optional): ResourceURL value
            aInfo (object, optional): aInfo value
        """
        super().__init__(**kwargs)
        if isinstance(ResourceURL, ConfigurationEvent):
            oth: ConfigurationEvent = ResourceURL
            self._resource_url = oth.ResourceURL
            self._a_info = oth.aInfo
            return
        else:
            self._resource_url = ResourceURL
            self._a_info = aInfo



    @property
    def ResourceURL(self) -> str:
        """
        contains the resource URL of the user interface element or a configuration manager, which has been changed, inserted or replaced.
        """
        return self._resource_url
    
    @ResourceURL.setter
    def ResourceURL(self, value: str) -> None:
        self._resource_url = value

    @property
    def aInfo(self) -> object:
        """
        contains additional information about this configuration event.
        
        The type depends on the specific implementation.
        """
        return self._a_info
    
    @aInfo.setter
    def aInfo(self, value: object) -> None:
        self._a_info = value


__all__ = ['ConfigurationEvent']