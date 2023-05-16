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
import warnings
warnings.filterwarnings('module')
warnings.warn('The csslo namespace is deprecated. Use lo instead.', DeprecationWarning, stacklevel=2)
from ....lo.script.provider.language_script_provider import LanguageScriptProvider as LanguageScriptProvider
from ....lo.script.provider.master_script_provider import MasterScriptProvider as MasterScriptProvider
from ....lo.script.provider.master_script_provider_factory import MasterScriptProviderFactory as MasterScriptProviderFactory
from ....lo.script.provider.script_error_raised_exception import ScriptErrorRaisedException as ScriptErrorRaisedException
from ....lo.script.provider.script_exception_raised_exception import ScriptExceptionRaisedException as ScriptExceptionRaisedException
from ....lo.script.provider.script_framework_error_exception import ScriptFrameworkErrorException as ScriptFrameworkErrorException
from ....lo.script.provider.script_framework_error_type import ScriptFrameworkErrorType as ScriptFrameworkErrorType
from ....lo.script.provider.script_provider import ScriptProvider as ScriptProvider
from ....lo.script.provider.script_provider_for_basic import ScriptProviderForBasic as ScriptProviderForBasic
from ....lo.script.provider.script_provider_for_bean_shell import ScriptProviderForBeanShell as ScriptProviderForBeanShell
from ....lo.script.provider.script_provider_for_java import ScriptProviderForJava as ScriptProviderForJava
from ....lo.script.provider.script_provider_for_java_script import ScriptProviderForJavaScript as ScriptProviderForJavaScript
from ....lo.script.provider.script_uri_helper import ScriptURIHelper as ScriptURIHelper
from ....lo.script.provider.x_script import XScript as XScript
from ....lo.script.provider.x_script_context import XScriptContext as XScriptContext
from ....lo.script.provider.x_script_provider import XScriptProvider as XScriptProvider
from ....lo.script.provider.x_script_provider_factory import XScriptProviderFactory as XScriptProviderFactory
from ....lo.script.provider.x_script_provider_supplier import XScriptProviderSupplier as XScriptProviderSupplier
from ....lo.script.provider.x_script_uri_helper import XScriptURIHelper as XScriptURIHelper
from ....lo.script.provider.the_master_script_provider_factory import theMasterScriptProviderFactory as theMasterScriptProviderFactory
