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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.bridge.oleautomation
from __future__ import annotations
from ..x_bridge_supplier2 import XBridgeSupplier2 as XBridgeSupplier2_fb800da0

class BridgeSupplier(XBridgeSupplier2_fb800da0):
    """
    Service Class

    maps UNO types to oleautomation types and vice versa.
    
    The function com.sun.star.bridge.XBridgeSupplier2.createBridge() maps a value of a UNO or Automation type to the desired target type. If a UNO interface was mapped to IDispatch, then all objects (interfaces, structs) and other types which are obtained from that Automation object are automatically mapped to the corresponding Automation types. Hence, if one provides an initial object which forms the root of all other objects, such as a service manager, then only that object needs to be explicitly mapped by a call to com.sun.star.bridge.XBridgeSupplier2.createBridge(). The same holds true if an automation object is mapped to a UNO interface.
    
    For Automation objects to be mapped they have to implement IDispatch interface. Other COM interfaces, except for IUnknown, are not supported. UNO interfaces and structs are mapped to IDispatch.
    
    The service implements the com.sun.star.bridge.XBridgeSupplier2 interface and handles the model types com.sun.star.bridge.ModelDependent.UNO and com.sun.star.bridge.ModelDependent.OLE. The service does not specify any requirements for registering OLE objects and class factories.

    See Also:
        `API BridgeSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1BridgeSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge.oleautomation'
    __ooo_full_ns__: str = 'com.sun.star.bridge.oleautomation.BridgeSupplier'
    __ooo_type_name__: str = 'service'


__all__ = ['BridgeSupplier']

