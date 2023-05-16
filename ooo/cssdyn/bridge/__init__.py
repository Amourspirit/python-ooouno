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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.bridge.bridge import Bridge as Bridge
with suppress(ImportError):
    from ...dyn.bridge.bridge_exists_exception import BridgeExistsException as BridgeExistsException
with suppress(ImportError):
    from ...dyn.bridge.bridge_factory import BridgeFactory as BridgeFactory
with suppress(ImportError):
    from ...dyn.bridge.iiop_bridge import IiopBridge as IiopBridge
with suppress(ImportError):
    from ...dyn.bridge.invalid_protocol_change_exception import InvalidProtocolChangeException as InvalidProtocolChangeException
with suppress(ImportError):
    from ...dyn.bridge.model_dependent import ModelDependent as ModelDependent
with suppress(ImportError):
    from ...dyn.bridge.model_dependent import ModelDependentEnum as ModelDependentEnum
with suppress(ImportError):
    from ...dyn.bridge.ole_application_registration import OleApplicationRegistration as OleApplicationRegistration
with suppress(ImportError):
    from ...dyn.bridge.ole_bridge_supplier import OleBridgeSupplier as OleBridgeSupplier
with suppress(ImportError):
    from ...dyn.bridge.ole_bridge_supplier2 import OleBridgeSupplier2 as OleBridgeSupplier2
with suppress(ImportError):
    from ...dyn.bridge.ole_bridge_supplier_var1 import OleBridgeSupplierVar1 as OleBridgeSupplierVar1
with suppress(ImportError):
    from ...dyn.bridge.ole_object_factory import OleObjectFactory as OleObjectFactory
with suppress(ImportError):
    from ...dyn.bridge.protocol_property import ProtocolProperty as ProtocolProperty
with suppress(ImportError):
    from ...dyn.bridge.uno_url_resolver import UnoUrlResolver as UnoUrlResolver
with suppress(ImportError):
    from ...dyn.bridge.urp_bridge import UrpBridge as UrpBridge
with suppress(ImportError):
    from ...dyn.bridge.x_bridge import XBridge as XBridge
with suppress(ImportError):
    from ...dyn.bridge.x_bridge_factory import XBridgeFactory as XBridgeFactory
with suppress(ImportError):
    from ...dyn.bridge.x_bridge_factory2 import XBridgeFactory2 as XBridgeFactory2
with suppress(ImportError):
    from ...dyn.bridge.x_bridge_supplier import XBridgeSupplier as XBridgeSupplier
with suppress(ImportError):
    from ...dyn.bridge.x_bridge_supplier2 import XBridgeSupplier2 as XBridgeSupplier2
with suppress(ImportError):
    from ...dyn.bridge.x_instance_provider import XInstanceProvider as XInstanceProvider
with suppress(ImportError):
    from ...dyn.bridge.x_protocol_properties import XProtocolProperties as XProtocolProperties
with suppress(ImportError):
    from ...dyn.bridge.x_uno_url_resolver import XUnoUrlResolver as XUnoUrlResolver
