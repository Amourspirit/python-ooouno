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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script
# Libre Office Version: 7.2
import os
from .all_event_object import AllEventObject as AllEventObject_e2c20d0f
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class ScriptEvent(AllEventObject_e2c20d0f):
    """
    Struct Class

    script event that gets delivered whenever a script event takes place.
    
    For that to happen, a \"ScriptEventDescriptor\" must be registered at and attached to an object by an XEventAttacherManager.

    See Also:
        `API ScriptEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1ScriptEvent.html>`_


    Note:
        | At runtime ScriptEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | ScriptEvent is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, ScriptCode: typing.Optional[str] = None, ScriptType: typing.Optional[str] = None):
        self._script_code = ScriptCode
        self._script_type = ScriptType

    @property
    def ScriptCode(self) -> str:
        """
        script code as string.
        
        The code has to correspond with the language defined by ScriptType.
        """
        return self._script_code
    
    @ScriptCode.setter
    def ScriptCode(self, value: str) -> None:
        self._script_code = value

    @property
    def ScriptType(self) -> str:
        """
        type of the script language as string; for example, \"Basic\" or \"StarScript\".
        """
        return self._script_type
    
    @ScriptType.setter
    def ScriptType(self, value: str) -> None:
        self._script_type = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global ScriptEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('ScriptCode', 'ScriptType')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.script.ScriptEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ScriptEvent = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['ScriptEvent']
