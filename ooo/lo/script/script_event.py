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
from .all_event_object import AllEventObject as AllEventObject_e2c20d0f


class ScriptEvent(AllEventObject_e2c20d0f):
    """
    Struct Class

    script event that gets delivered whenever a script event takes place.
    
    For that to happen, a \"ScriptEventDescriptor\" must be registered at and attached to an object by an XEventAttacherManager.

    See Also:
        `API ScriptEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1ScriptEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.ScriptEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.ScriptEvent'
    """Literal Constant ``com.sun.star.script.ScriptEvent``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ScriptEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ScriptEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ScriptType (str, optional): ScriptType value
            ScriptCode (str, optional): ScriptCode value
        """
        self._script_type = None
        self._script_code = None

        key_order = ('ScriptType', 'ScriptCode')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ScriptEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ScriptEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def ScriptType(self) -> str:
        """
        type of the script language as string; for example, \"Basic\" or \"StarScript\".
        """
        return self._script_type
    
    @ScriptType.setter
    def ScriptType(self, value: str) -> None:
        self._script_type = value

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


__all__ = ['ScriptEvent']
