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
    from ....dyn.bridge.oleautomation.application_registration import ApplicationRegistration as ApplicationRegistration
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.bridge_supplier import BridgeSupplier as BridgeSupplier
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.currency import Currency as Currency
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.date import Date as Date
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.decimal import Decimal as Decimal
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.factory import Factory as Factory
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.named_argument import NamedArgument as NamedArgument
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.property_put_argument import PropertyPutArgument as PropertyPutArgument
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.s_code import SCode as SCode
except ImportError:
    pass
try:
    from ....dyn.bridge.oleautomation.x_automation_object import XAutomationObject as XAutomationObject
except ImportError:
    pass
