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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.uno.deployment_exception import DeploymentException as DeploymentException
with suppress(ImportError):
    from ...dyn.uno.exception import Exception as Exception
with suppress(ImportError):
    from ...dyn.uno.naming_service import NamingService as NamingService
with suppress(ImportError):
    from ...dyn.uno.runtime_exception import RuntimeException as RuntimeException
with suppress(ImportError):
    from ...dyn.uno.security_exception import SecurityException as SecurityException
with suppress(ImportError):
    from ...dyn.uno.type_class import TypeClass as TypeClass
with suppress(ImportError):
    from ...dyn.uno.uik import Uik as Uik
with suppress(ImportError):
    from ...dyn.uno.x_adapter import XAdapter as XAdapter
with suppress(ImportError):
    from ...dyn.uno.x_aggregation import XAggregation as XAggregation
with suppress(ImportError):
    from ...dyn.uno.x_component_context import XComponentContext as XComponentContext
with suppress(ImportError):
    from ...dyn.uno.x_current_context import XCurrentContext as XCurrentContext
with suppress(ImportError):
    from ...dyn.uno.x_interface import XInterface as XInterface
with suppress(ImportError):
    from ...dyn.uno.x_naming_service import XNamingService as XNamingService
with suppress(ImportError):
    from ...dyn.uno.x_reference import XReference as XReference
with suppress(ImportError):
    from ...dyn.uno.x_unloading_preference import XUnloadingPreference as XUnloadingPreference
with suppress(ImportError):
    from ...dyn.uno.x_weak import XWeak as XWeak
