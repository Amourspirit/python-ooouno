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
    from ...dyn.registry.cannot_register_implementation_exception import CannotRegisterImplementationException as CannotRegisterImplementationException
with suppress(ImportError):
    from ...dyn.registry.default_registry import DefaultRegistry as DefaultRegistry
with suppress(ImportError):
    from ...dyn.registry.implementation_registration import ImplementationRegistration as ImplementationRegistration
with suppress(ImportError):
    from ...dyn.registry.invalid_registry_exception import InvalidRegistryException as InvalidRegistryException
with suppress(ImportError):
    from ...dyn.registry.invalid_value_exception import InvalidValueException as InvalidValueException
with suppress(ImportError):
    from ...dyn.registry.merge_conflict_exception import MergeConflictException as MergeConflictException
with suppress(ImportError):
    from ...dyn.registry.nested_registry import NestedRegistry as NestedRegistry
with suppress(ImportError):
    from ...dyn.registry.registry_key_type import RegistryKeyType as RegistryKeyType
with suppress(ImportError):
    from ...dyn.registry.registry_value_type import RegistryValueType as RegistryValueType
with suppress(ImportError):
    from ...dyn.registry.simple_registry import SimpleRegistry as SimpleRegistry
with suppress(ImportError):
    from ...dyn.registry.x_implementation_registration import XImplementationRegistration as XImplementationRegistration
with suppress(ImportError):
    from ...dyn.registry.x_implementation_registration2 import XImplementationRegistration2 as XImplementationRegistration2
with suppress(ImportError):
    from ...dyn.registry.x_registry_key import XRegistryKey as XRegistryKey
with suppress(ImportError):
    from ...dyn.registry.x_simple_registry import XSimpleRegistry as XSimpleRegistry
