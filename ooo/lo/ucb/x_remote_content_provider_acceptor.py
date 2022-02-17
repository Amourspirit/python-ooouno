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
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
    from .x_remote_content_provider_done_listener import XRemoteContentProviderDoneListener as XRemoteContentProviderDoneListener_fc7413f8

class XRemoteContentProviderAcceptor(XInterface_8f010a43):
    """
    Accept remote content providers that want to make themselves known to the local process.

    See Also:
        `API XRemoteContentProviderAcceptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XRemoteContentProviderAcceptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XRemoteContentProviderAcceptor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XRemoteContentProviderAcceptor'

    @abstractmethod
    def addRemoteContentProvider(self, Identifier: str, Factory: 'XMultiServiceFactory_191e0eb6', Templates: 'typing.Tuple[str, ...]', DoneListener: 'XRemoteContentProviderDoneListener_fc7413f8') -> bool:
        """
        Add a remote content provider.
        
        To enable connection control, it is recommended that this argument also implements the interface XRemoteContentProviderConnectionControl.
        """
    @abstractmethod
    def removeRemoteContentProvider(self, Identifier: str) -> bool:
        """
        Remove a remote content provider.
        """

__all__ = ['XRemoteContentProviderAcceptor']

