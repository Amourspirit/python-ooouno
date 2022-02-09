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
# Namespace: com.sun.star.uno
import typing
from abc import abstractmethod
from .x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.x_multi_component_factory import XMultiComponentFactory as XMultiComponentFactory_381b0f98

class XComponentContext(XInterface_8f010a43):
    """
    Component context to be passed to a component via com.sun.star.lang.XSingleComponentFactory.
    
    Arbitrary values (e.g. deployment values) can be retrieved from the context.

    See Also:
        `API XComponentContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XComponentContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.XComponentContext'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.uno.XComponentContext'

    @abstractmethod
    def getServiceManager(self) -> 'XMultiComponentFactory_381b0f98':
        """
        Gets the service manager instance to be used from key /singletons/com.sun.star.lang.theServiceManager.
        
        This method has been added for convenience, because the service manager is used very often.
        """
    @abstractmethod
    def getValueByName(self, Name: str) -> object:
        """
        Gets a value from the context.
        """


__all__ = ['XComponentContext']

