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
    from ...dyn.system.simple_command_mail import SimpleCommandMail as SimpleCommandMail
with suppress(ImportError):
    from ...dyn.system.simple_mail_client_flags import SimpleMailClientFlags as SimpleMailClientFlags
with suppress(ImportError):
    from ...dyn.system.simple_mail_client_flags import SimpleMailClientFlagsEnum as SimpleMailClientFlagsEnum
with suppress(ImportError):
    from ...dyn.system.simple_system_mail import SimpleSystemMail as SimpleSystemMail
with suppress(ImportError):
    from ...dyn.system.system_shell_execute import SystemShellExecute as SystemShellExecute
with suppress(ImportError):
    from ...dyn.system.system_shell_execute_exception import SystemShellExecuteException as SystemShellExecuteException
with suppress(ImportError):
    from ...dyn.system.system_shell_execute_flags import SystemShellExecuteFlags as SystemShellExecuteFlags
with suppress(ImportError):
    from ...dyn.system.system_shell_execute_flags import SystemShellExecuteFlagsEnum as SystemShellExecuteFlagsEnum
with suppress(ImportError):
    from ...dyn.system.x_simple_mail_client import XSimpleMailClient as XSimpleMailClient
with suppress(ImportError):
    from ...dyn.system.x_simple_mail_client_supplier import XSimpleMailClientSupplier as XSimpleMailClientSupplier
with suppress(ImportError):
    from ...dyn.system.x_simple_mail_message import XSimpleMailMessage as XSimpleMailMessage
with suppress(ImportError):
    from ...dyn.system.x_simple_mail_message2 import XSimpleMailMessage2 as XSimpleMailMessage2
with suppress(ImportError):
    from ...dyn.system.x_system_shell_execute import XSystemShellExecute as XSystemShellExecute
