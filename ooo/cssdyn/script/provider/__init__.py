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
    from ....dyn.script.provider.language_script_provider import LanguageScriptProvider as LanguageScriptProvider
with suppress(ImportError):
    from ....dyn.script.provider.master_script_provider import MasterScriptProvider as MasterScriptProvider
with suppress(ImportError):
    from ....dyn.script.provider.master_script_provider_factory import MasterScriptProviderFactory as MasterScriptProviderFactory
with suppress(ImportError):
    from ....dyn.script.provider.script_error_raised_exception import ScriptErrorRaisedException as ScriptErrorRaisedException
with suppress(ImportError):
    from ....dyn.script.provider.script_exception_raised_exception import ScriptExceptionRaisedException as ScriptExceptionRaisedException
with suppress(ImportError):
    from ....dyn.script.provider.script_framework_error_exception import ScriptFrameworkErrorException as ScriptFrameworkErrorException
with suppress(ImportError):
    from ....dyn.script.provider.script_framework_error_type import ScriptFrameworkErrorType as ScriptFrameworkErrorType
with suppress(ImportError):
    from ....dyn.script.provider.script_framework_error_type import ScriptFrameworkErrorTypeEnum as ScriptFrameworkErrorTypeEnum
with suppress(ImportError):
    from ....dyn.script.provider.script_provider import ScriptProvider as ScriptProvider
with suppress(ImportError):
    from ....dyn.script.provider.script_provider_for_basic import ScriptProviderForBasic as ScriptProviderForBasic
with suppress(ImportError):
    from ....dyn.script.provider.script_provider_for_bean_shell import ScriptProviderForBeanShell as ScriptProviderForBeanShell
with suppress(ImportError):
    from ....dyn.script.provider.script_provider_for_java import ScriptProviderForJava as ScriptProviderForJava
with suppress(ImportError):
    from ....dyn.script.provider.script_provider_for_java_script import ScriptProviderForJavaScript as ScriptProviderForJavaScript
with suppress(ImportError):
    from ....dyn.script.provider.script_uri_helper import ScriptURIHelper as ScriptURIHelper
with suppress(ImportError):
    from ....dyn.script.provider.x_script import XScript as XScript
with suppress(ImportError):
    from ....dyn.script.provider.x_script_context import XScriptContext as XScriptContext
with suppress(ImportError):
    from ....dyn.script.provider.x_script_provider import XScriptProvider as XScriptProvider
with suppress(ImportError):
    from ....dyn.script.provider.x_script_provider_factory import XScriptProviderFactory as XScriptProviderFactory
with suppress(ImportError):
    from ....dyn.script.provider.x_script_provider_supplier import XScriptProviderSupplier as XScriptProviderSupplier
with suppress(ImportError):
    from ....dyn.script.provider.x_script_uri_helper import XScriptURIHelper as XScriptURIHelper
with suppress(ImportError):
    from ....dyn.script.provider.the_master_script_provider_factory import theMasterScriptProviderFactory as theMasterScriptProviderFactory
