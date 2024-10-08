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
    from ...dyn.java.invalid_java_settings_exception import InvalidJavaSettingsException as InvalidJavaSettingsException
with suppress(ImportError):
    from ...dyn.java.java_disabled_exception import JavaDisabledException as JavaDisabledException
with suppress(ImportError):
    from ...dyn.java.java_initialization_exception import JavaInitializationException as JavaInitializationException
with suppress(ImportError):
    from ...dyn.java.java_not_configured_exception import JavaNotConfiguredException as JavaNotConfiguredException
with suppress(ImportError):
    from ...dyn.java.java_not_found_exception import JavaNotFoundException as JavaNotFoundException
with suppress(ImportError):
    from ...dyn.java.java_vm_creation_failure_exception import JavaVMCreationFailureException as JavaVMCreationFailureException
with suppress(ImportError):
    from ...dyn.java.java_virtual_machine import JavaVirtualMachine as JavaVirtualMachine
with suppress(ImportError):
    from ...dyn.java.missing_java_runtime_exception import MissingJavaRuntimeException as MissingJavaRuntimeException
with suppress(ImportError):
    from ...dyn.java.restart_required_exception import RestartRequiredException as RestartRequiredException
with suppress(ImportError):
    from ...dyn.java.wrong_java_version_exception import WrongJavaVersionException as WrongJavaVersionException
with suppress(ImportError):
    from ...dyn.java.x_java_thread_register_11 import XJavaThreadRegister_11 as XJavaThreadRegister_11
with suppress(ImportError):
    from ...dyn.java.x_java_vm import XJavaVM as XJavaVM
