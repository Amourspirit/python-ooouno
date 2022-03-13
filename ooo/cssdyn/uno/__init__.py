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
    from ...dyn.uno.deployment_exception import DeploymentException as DeploymentException
except ImportError:
    pass
try:
    from ...dyn.uno.exception import Exception as Exception
except ImportError:
    pass
try:
    from ...dyn.uno.naming_service import NamingService as NamingService
except ImportError:
    pass
try:
    from ...dyn.uno.runtime_exception import RuntimeException as RuntimeException
except ImportError:
    pass
try:
    from ...dyn.uno.security_exception import SecurityException as SecurityException
except ImportError:
    pass
try:
    from ...dyn.uno.type_class import TypeClass as TypeClass
except ImportError:
    pass
try:
    from ...dyn.uno.uik import Uik as Uik
except ImportError:
    pass
try:
    from ...dyn.uno.x_adapter import XAdapter as XAdapter
except ImportError:
    pass
try:
    from ...dyn.uno.x_aggregation import XAggregation as XAggregation
except ImportError:
    pass
try:
    from ...dyn.uno.x_component_context import XComponentContext as XComponentContext
except ImportError:
    pass
try:
    from ...dyn.uno.x_current_context import XCurrentContext as XCurrentContext
except ImportError:
    pass
try:
    from ...dyn.uno.x_interface import XInterface as XInterface
except ImportError:
    pass
try:
    from ...dyn.uno.x_naming_service import XNamingService as XNamingService
except ImportError:
    pass
try:
    from ...dyn.uno.x_reference import XReference as XReference
except ImportError:
    pass
try:
    from ...dyn.uno.x_unloading_preference import XUnloadingPreference as XUnloadingPreference
except ImportError:
    pass
try:
    from ...dyn.uno.x_weak import XWeak as XWeak
except ImportError:
    pass
