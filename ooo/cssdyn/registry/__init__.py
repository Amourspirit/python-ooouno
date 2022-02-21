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
    from ...dyn.registry.cannot_register_implementation_exception import CannotRegisterImplementationException as CannotRegisterImplementationException
except ImportError:
    pass
try:
    from ...dyn.registry.default_registry import DefaultRegistry as DefaultRegistry
except ImportError:
    pass
try:
    from ...dyn.registry.implementation_registration import ImplementationRegistration as ImplementationRegistration
except ImportError:
    pass
try:
    from ...dyn.registry.invalid_registry_exception import InvalidRegistryException as InvalidRegistryException
except ImportError:
    pass
try:
    from ...dyn.registry.invalid_value_exception import InvalidValueException as InvalidValueException
except ImportError:
    pass
try:
    from ...dyn.registry.merge_conflict_exception import MergeConflictException as MergeConflictException
except ImportError:
    pass
try:
    from ...dyn.registry.nested_registry import NestedRegistry as NestedRegistry
except ImportError:
    pass
try:
    from ...dyn.registry.registry_key_type import RegistryKeyType as RegistryKeyType
except ImportError:
    pass
try:
    from ...dyn.registry.registry_value_type import RegistryValueType as RegistryValueType
except ImportError:
    pass
try:
    from ...dyn.registry.simple_registry import SimpleRegistry as SimpleRegistry
except ImportError:
    pass
try:
    from ...dyn.registry.x_implementation_registration import XImplementationRegistration as XImplementationRegistration
except ImportError:
    pass
try:
    from ...dyn.registry.x_implementation_registration2 import XImplementationRegistration2 as XImplementationRegistration2
except ImportError:
    pass
try:
    from ...dyn.registry.x_registry_key import XRegistryKey as XRegistryKey
except ImportError:
    pass
try:
    from ...dyn.registry.x_simple_registry import XSimpleRegistry as XSimpleRegistry
except ImportError:
    pass
