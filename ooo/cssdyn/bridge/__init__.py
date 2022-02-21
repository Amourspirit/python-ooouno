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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ...dyn.bridge.bridge import Bridge as Bridge
except ImportError:
    pass
try:
    from ...dyn.bridge.bridge_exists_exception import BridgeExistsException as BridgeExistsException
except ImportError:
    pass
try:
    from ...dyn.bridge.bridge_factory import BridgeFactory as BridgeFactory
except ImportError:
    pass
try:
    from ...dyn.bridge.iiop_bridge import IiopBridge as IiopBridge
except ImportError:
    pass
try:
    from ...dyn.bridge.invalid_protocol_change_exception import InvalidProtocolChangeException as InvalidProtocolChangeException
except ImportError:
    pass
try:
    from ...dyn.bridge.model_dependent import ModelDependent as ModelDependent
except ImportError:
    pass
try:
    from ...dyn.bridge.model_dependent import ModelDependentEnum as ModelDependentEnum
except ImportError:
    pass
try:
    from ...dyn.bridge.ole_application_registration import OleApplicationRegistration as OleApplicationRegistration
except ImportError:
    pass
try:
    from ...dyn.bridge.ole_bridge_supplier import OleBridgeSupplier as OleBridgeSupplier
except ImportError:
    pass
try:
    from ...dyn.bridge.ole_bridge_supplier2 import OleBridgeSupplier2 as OleBridgeSupplier2
except ImportError:
    pass
try:
    from ...dyn.bridge.ole_bridge_supplier_var1 import OleBridgeSupplierVar1 as OleBridgeSupplierVar1
except ImportError:
    pass
try:
    from ...dyn.bridge.ole_object_factory import OleObjectFactory as OleObjectFactory
except ImportError:
    pass
try:
    from ...dyn.bridge.protocol_property import ProtocolProperty as ProtocolProperty
except ImportError:
    pass
try:
    from ...dyn.bridge.uno_url_resolver import UnoUrlResolver as UnoUrlResolver
except ImportError:
    pass
try:
    from ...dyn.bridge.urp_bridge import UrpBridge as UrpBridge
except ImportError:
    pass
try:
    from ...dyn.bridge.x_bridge import XBridge as XBridge
except ImportError:
    pass
try:
    from ...dyn.bridge.x_bridge_factory import XBridgeFactory as XBridgeFactory
except ImportError:
    pass
try:
    from ...dyn.bridge.x_bridge_factory2 import XBridgeFactory2 as XBridgeFactory2
except ImportError:
    pass
try:
    from ...dyn.bridge.x_bridge_supplier import XBridgeSupplier as XBridgeSupplier
except ImportError:
    pass
try:
    from ...dyn.bridge.x_bridge_supplier2 import XBridgeSupplier2 as XBridgeSupplier2
except ImportError:
    pass
try:
    from ...dyn.bridge.x_instance_provider import XInstanceProvider as XInstanceProvider
except ImportError:
    pass
try:
    from ...dyn.bridge.x_protocol_properties import XProtocolProperties as XProtocolProperties
except ImportError:
    pass
try:
    from ...dyn.bridge.x_uno_url_resolver import XUnoUrlResolver as XUnoUrlResolver
except ImportError:
    pass
