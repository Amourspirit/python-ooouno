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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.script.vba
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.script.vba import VBAScriptEventId as VBAScriptEventId
    if hasattr(VBAScriptEventId, '_constants') and isinstance(VBAScriptEventId._constants, dict):
        VBAScriptEventId._constants['__ooo_ns__'] = 'com.sun.star.script.vba'
        VBAScriptEventId._constants['__ooo_full_ns__'] = 'com.sun.star.script.vba.VBAScriptEventId'
        VBAScriptEventId._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global VBAScriptEventIdEnum
        ls = [f for f in dir(VBAScriptEventId) if not callable(getattr(VBAScriptEventId, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(VBAScriptEventId, name)
        VBAScriptEventIdEnum = IntEnum('VBAScriptEventIdEnum', _dict)
    build_enum()
else:
    from ....lo.script.vba.vba_script_event_id import VBAScriptEventId as VBAScriptEventId

    class VBAScriptEventIdEnum(IntEnum):
        """
        Enum of Const Class VBAScriptEventId

        Identifies a VBA script event fired via XVBACompatibility.broadcastVBAScriptEvent(), and received by XVBAScriptListener.notifyVBAScriptEvent().
        """
        SCRIPT_STARTED = VBAScriptEventId.SCRIPT_STARTED
        """
        This event is fired when a VBA script in the current document has been started.
        
        Several scripts may run simultaneously, e.g. when a running script triggers a document event that starts another script.
        
        The number of running scripts can be obtained via XVBACompatibility.RunningVBAScripts. The number returned there will already contain the new script notified with this event.
        
        The member VBAScriptEvent.ModuleName of the event object will contain the name of the code module that contains the started script.
        """
        SCRIPT_STOPPED = VBAScriptEventId.SCRIPT_STOPPED
        """
        This event is fired when a VBA script in the current document stops running.
        
        Several scripts may run simultaneously, e.g. when a running script triggers a document event that starts another script.
        
        The number of scripts still running can be obtained via XVBACompatibility.RunningVBAScripts. The number returned there will not contain the stopped script notified with this event anymore.
        
        The member VBAScriptEvent.ModuleName of the event object will contain the name of the code module that contains the script that has been stopped.
        """
        INITIALIZE_USERFORM = VBAScriptEventId.INITIALIZE_USERFORM
        """
        This event is fired when a VBA script in the current document tries to instantiate a userform.
        
        The member VBAScriptEvent.ModuleName of the event object will contain the name of the userform module.
        """

__all__ = ['VBAScriptEventId', 'VBAScriptEventIdEnum']
