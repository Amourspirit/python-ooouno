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
    from ....dyn.script.vba.vba_event_id import VBAEventId as VBAEventId
with suppress(ImportError):
    from ....dyn.script.vba.vba_event_id import VBAEventIdEnum as VBAEventIdEnum
with suppress(ImportError):
    from ....dyn.script.vba.vba_event_processor import VBAEventProcessor as VBAEventProcessor
with suppress(ImportError):
    from ....dyn.script.vba.vba_macro_resolver import VBAMacroResolver as VBAMacroResolver
with suppress(ImportError):
    from ....dyn.script.vba.vba_script_event import VBAScriptEvent as VBAScriptEvent
with suppress(ImportError):
    from ....dyn.script.vba.vba_script_event_id import VBAScriptEventId as VBAScriptEventId
with suppress(ImportError):
    from ....dyn.script.vba.vba_script_event_id import VBAScriptEventIdEnum as VBAScriptEventIdEnum
with suppress(ImportError):
    from ....dyn.script.vba.vba_spreadsheet_event_processor import VBASpreadsheetEventProcessor as VBASpreadsheetEventProcessor
with suppress(ImportError):
    from ....dyn.script.vba.vba_text_event_processor import VBATextEventProcessor as VBATextEventProcessor
with suppress(ImportError):
    from ....dyn.script.vba.xvba_compatibility import XVBACompatibility as XVBACompatibility
with suppress(ImportError):
    from ....dyn.script.vba.xvba_event_processor import XVBAEventProcessor as XVBAEventProcessor
with suppress(ImportError):
    from ....dyn.script.vba.xvba_macro_resolver import XVBAMacroResolver as XVBAMacroResolver
with suppress(ImportError):
    from ....dyn.script.vba.xvba_module_info import XVBAModuleInfo as XVBAModuleInfo
with suppress(ImportError):
    from ....dyn.script.vba.xvba_script_listener import XVBAScriptListener as XVBAScriptListener
