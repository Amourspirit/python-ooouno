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
# Namespace: com.sun.star.script.vba
# Libre Office Version: 7.2
from ...lang.event_object import EventObject as EventObject_a3d70b03


class VBAScriptEvent(EventObject_a3d70b03):
    """
    Struct Class

    Describes a VBA script event fired via XVBACompatibility.broadcastVBAScriptEvent(), and received by XVBAScriptListener.notifyVBAScriptEvent().

    See Also:
        `API VBAScriptEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1vba_1_1VBAScriptEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script.vba'
    __ooo_full_ns__: str = 'com.sun.star.script.vba.VBAScriptEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.vba.VBAScriptEvent'
    """Literal Constant ``com.sun.star.script.vba.VBAScriptEvent``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``VBAScriptEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``VBAScriptEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Identifier (int, optional): Identifier value
            ModuleName (str, optional): ModuleName value
        """
        self._identifier = None
        self._module_name = None

        key_order = ('Identifier', 'ModuleName')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], VBAScriptEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("VBAScriptEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Identifier(self) -> int:
        """
        Identifies the type of the event.
        """
        return self._identifier
    
    @Identifier.setter
    def Identifier(self, value: int) -> None:
        self._identifier = value

    @property
    def ModuleName(self) -> str:
        """
        Contains the name of the involved VBA module.
        """
        return self._module_name
    
    @ModuleName.setter
    def ModuleName(self, value: str) -> None:
        self._module_name = value


__all__ = ['VBAScriptEvent']
