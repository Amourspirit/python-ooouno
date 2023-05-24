# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .xui_element import XUIElement as XUIElement_820509a6

class XUIElementFactory(XInterface_8f010a43):
    """
    specifies a user interface element factory that can create and initialize user interface elements.
    
    User interface element factories must be registered at a UIElementFactoryManager service to provide access to itself.
    
    Currently the following user interface element types are defined:
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUIElementFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XUIElementFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XUIElementFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XUIElementFactory'

    @abstractmethod
    def createUIElement(self, ResourceURL: str, Args: typing.Tuple[PropertyValue_c9610c73, ...]) -> XUIElement_820509a6:
        """
        creates a new instances of a specific user interface element.
        
        An implementation is responsible to initialize every newly created user interface element if the necessary properties are provided. Especially it must connect a configurable user interface element to the correct user interface configuration manager. Without this connection the configurable user interface element cannot retrieve its structure data and changes to the user interface element structure won't be persistent. It is up to the implementation to throw an com.sun.star.lang.IllegalArgumentException if it cannot create a user interface element with the provided arguments.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XUIElementFactory']

