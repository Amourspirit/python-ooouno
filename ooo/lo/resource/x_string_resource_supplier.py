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
# Namespace: com.sun.star.resource
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_string_resource_resolver import XStringResourceResolver as XStringResourceResolver_92cb11d9

class XStringResourceSupplier(XInterface_8f010a43):
    """
    Provides access to a string resource represented by a com.sun.star.resource.XStringResourceResolver.

    See Also:
        `API XStringResourceSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1resource_1_1XStringResourceSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.resource'
    __ooo_full_ns__: str = 'com.sun.star.resource.XStringResourceSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.resource.XStringResourceSupplier'

    @abstractmethod
    def getStringResource(self) -> 'XStringResourceResolver_92cb11d9':
        """
        Provides access to a string resource.
        
        Depending on the context the returned object may also support com.sun.star.resource.XStringResourceManager or com.sun.star.resource.XStringResourcePersistence or com.sun.star.resource.XStringResourceWithStorage
        """

__all__ = ['XStringResourceSupplier']

