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
from ooo.oenv import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
import typing


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

    def __init__(self, Identifier: int = 0, ModuleName: str = '', **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``Identifier`` can be another ``VBAScriptEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            Identifier (int, optional): Identifier value
            ModuleName (str, optional): ModuleName value
        """
        super().__init__(**kwargs)
        if isinstance(Identifier, VBAScriptEvent):
            oth: VBAScriptEvent = Identifier
            self._identifier = oth.Identifier
            self._module_name = oth.ModuleName
            return
        else:
            self._identifier = Identifier
            self._module_name = ModuleName



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