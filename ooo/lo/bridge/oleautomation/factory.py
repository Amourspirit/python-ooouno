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
# Namespace: com.sun.star.bridge.oleautomation
from __future__ import annotations
from ...lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6

class Factory(XMultiServiceFactory_191e0eb6):
    """
    Service Class

    makes it possible to create COM objects as UNO objects.
    
    A COM object must have a ProgId since the ProgId is used as argument for com.sun.star.lang.XMultiServiceFactory.createInstance(). The only interfaces which are mapped are IUnknown and IDispatch. The created UNO objects support com.sun.star.script.XInvocation if the original COM objects support IDispatch.
    
    The optional parameters of the method com.sun.star.lang.XMultiServiceFactory.createInstanceWithArguments() are reserved for future use; at this time they are ignored.

    See Also:
        `API Factory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1Factory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge.oleautomation'
    __ooo_full_ns__: str = 'com.sun.star.bridge.oleautomation.Factory'
    __ooo_type_name__: str = 'service'


__all__ = ['Factory']

