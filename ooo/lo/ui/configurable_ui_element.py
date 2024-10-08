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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ui
from __future__ import annotations
import typing
from abc import abstractmethod
from .ui_element import UIElement as UIElement_78af094e
from .xui_element_settings import XUIElementSettings as XUIElementSettings_ddbb0cf7
if typing.TYPE_CHECKING:
    from .xui_configuration_manager import XUIConfigurationManager as XUIConfigurationManager_24e20eef

class ConfigurableUIElement(UIElement_78af094e, XUIElementSettings_ddbb0cf7):
    """
    Service Class

    specifies a configurable user interface element that supports persistence.
    
    Configurable user interface elements are:
    
    **since**
    
        OOo 2.0

    See Also:
        `API ConfigurableUIElement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1ConfigurableUIElement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.ConfigurableUIElement'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def ConfigurationSource(self) -> XUIConfigurationManager_24e20eef:
        """
        specifies the configuration source of this user interface element.
        
        If the property Persistent is TRUE changes on the structure of the user interface element are written back to configuration source. When this property is changed, afterwards XUIElementSettings.updateSettings() must be called so the user interface element tries to retrieve its settings from the new user interface configuration manager.
        """
        ...

    @property
    @abstractmethod
    def Persistent(self) -> bool:
        """
        specifies if the user interface element stores changes of its structure to its creator source defined by the property ConfigurationSource.
        """
        ...


__all__ = ['ConfigurableUIElement']

