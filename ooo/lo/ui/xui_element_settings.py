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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.ui
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d

class XUIElementSettings(XInterface_8f010a43):
    """
    provides functions to retrieve and change user interface element structure data and to update its visible representation.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUIElementSettings <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XUIElementSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XUIElementSettings'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XUIElementSettings'

    @abstractmethod
    def getSettings(self, bWriteable: bool) -> 'XIndexAccess_f0910d6d':
        """
        provides a UIElementSettings instance that provides access to the structure of user interface element if the user interface element type supports it.
        """
    @abstractmethod
    def setSettings(self, UISettings: 'XIndexAccess_f0910d6d') -> None:
        """
        set changes to the structure of the user interface element.
        
        User interface elements cannot be changed directly. The changed structure data has to be set again. This speeds up the configuration process if many changes have to be made on the structure. The persistence of changes are controlled by the boolean property Persistent.
        """
    @abstractmethod
    def updateSettings(self) -> None:
        """
        forces the user interface element to retrieve new settings from its configuration source.
        
        This is not done automatically as configurable user interface elements are controlled by layout managers. It is more efficient to let the responsible layout manager to control the update process in a single task.
        """


__all__ = ['XUIElementSettings']

