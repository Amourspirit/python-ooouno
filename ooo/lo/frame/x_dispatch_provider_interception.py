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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_dispatch_provider_interceptor import XDispatchProviderInterceptor as XDispatchProviderInterceptor_afda1275

class XDispatchProviderInterception(XInterface_8f010a43):
    """
    makes it possible to register an XDispatchProvider which intercepts all requests of XDispatch to this instance.
    
    Note: Nobody can guarantee order of used interceptor objects if more than ones exist. Later registered ones will be used at first. But it's possible to increase the chance for that by providing the optional interface XInterceptorInfo.

    See Also:
        `API XDispatchProviderInterception <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDispatchProviderInterception.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XDispatchProviderInterception'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XDispatchProviderInterception'

    @abstractmethod
    def registerDispatchProviderInterceptor(self, Interceptor: 'XDispatchProviderInterceptor_afda1275') -> None:
        """
        registers an XDispatchProviderInterceptor, which will become the first interceptor in the chain of registered interceptors.
        """
        ...
    @abstractmethod
    def releaseDispatchProviderInterceptor(self, Interceptor: 'XDispatchProviderInterceptor_afda1275') -> None:
        """
        removes an XDispatchProviderInterceptor which was previously registered
        
        The order of removals is arbitrary. It is not necessary to remove the last registered interceptor first.
        """
        ...

__all__ = ['XDispatchProviderInterception']

