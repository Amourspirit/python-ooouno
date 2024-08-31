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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from .all_event_object import AllEventObject as AllEventObject_e2c20d0f
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


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

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Helper: typing.Optional[object] = None, ListenerType: typing.Optional[object] = None, MethodName: typing.Optional[str] = '', Arguments: typing.Optional[typing.Tuple[object, ...]] = (), ScriptType: typing.Optional[str] = '', ScriptCode: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Helper (object, optional): Helper value.
            ListenerType (object, optional): ListenerType value.
            MethodName (str, optional): MethodName value.
            Arguments (typing.Tuple[object, ...], optional): Arguments value.
            ScriptType (str, optional): ScriptType value.
            ScriptCode (str, optional): ScriptCode value.
        """

        if isinstance(Source, ScriptEvent):
            oth: ScriptEvent = Source
            self.Source = oth.Source
            self.Helper = oth.Helper
            self.ListenerType = oth.ListenerType
            self.MethodName = oth.MethodName
            self.Arguments = oth.Arguments
            self.ScriptType = oth.ScriptType
            self.ScriptCode = oth.ScriptCode
            return

        kargs = {
            "Source": Source,
            "Helper": Helper,
            "ListenerType": ListenerType,
            "MethodName": MethodName,
            "Arguments": Arguments,
            "ScriptType": ScriptType,
            "ScriptCode": ScriptCode,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._script_type = kwargs["ScriptType"]
        self._script_code = kwargs["ScriptCode"]
        inst_keys = ('ScriptType', 'ScriptCode')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


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
