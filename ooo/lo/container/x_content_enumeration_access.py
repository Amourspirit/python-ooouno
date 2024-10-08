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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.container
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_enumeration import XEnumeration as XEnumeration_f2180daa

class XContentEnumerationAccess(XInterface_8f010a43):
    """
    allows access to the collections of all content types within the object.
    
    This example prints the names of all tables:

    See Also:
        `API XContentEnumerationAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XContentEnumerationAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.container'
    __ooo_full_ns__: str = 'com.sun.star.container.XContentEnumerationAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.container.XContentEnumerationAccess'

    @abstractmethod
    def createContentEnumeration(self, aServiceName: str) -> XEnumeration_f2180daa:
        """
        """
        ...
    @abstractmethod
    def getAvailableServiceNames(self) -> typing.Tuple[str, ...]:
        """
        XContentEnumerationAccess.createContentEnumeration() creates an enumeration for all the service names which are listed here. For all others it creates no enumeration.
        """
        ...

__all__ = ['XContentEnumerationAccess']

