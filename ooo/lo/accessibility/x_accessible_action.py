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
# Namespace: com.sun.star.accessibility
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_accessible_key_binding import XAccessibleKeyBinding as XAccessibleKeyBinding_c493129a

class XAccessibleAction(XInterface_8f010a43):
    """
    Implement this interface to give access to actions that can be executed for accessible objects.
    
    Every accessible object that can be manipulated beyond its methods exported over the accessibility API should support this interface to expose all actions that it can perform. Each action can be performed or be queried for a description or associated key bindings.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleAction <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleAction.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleAction'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleAction'

    @abstractmethod
    def doAccessibleAction(self, nIndex: int) -> bool:
        """
        Perform the specified Action on the object.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getAccessibleActionCount(self) -> int:
        """
        Returns the number of accessible actions available in this object.
        
        If there are more than one, the first one is considered the \"default\" action of the object.
        """
    @abstractmethod
    def getAccessibleActionDescription(self, nIndex: int) -> str:
        """
        Returns a description of the specified action of the object.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getAccessibleActionKeyBinding(self, nIndex: int) -> 'XAccessibleKeyBinding_c493129a':
        """
        Returns a key binding object, if there is one, associated with the specified action.
        
        Note that there can be several alternative key bindings for an action. See XAccessibleKeyBinding for more information about how key bindings are represented.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """


__all__ = ['XAccessibleAction']

