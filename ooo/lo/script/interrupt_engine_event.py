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
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from .interrupt_reason import InterruptReason as InterruptReason_f3d00dd2


class InterruptEngineEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes an interrupt which occurs in the scripting engine.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API InterruptEngineEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1InterruptEngineEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.InterruptEngineEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.InterruptEngineEvent'
    """Literal Constant ``com.sun.star.script.InterruptEngineEvent``"""

    def __init__(self, Name: str = '', SourceCode: str = '', StartLine: int = 0, StartColumn: int = 0, EndLine: int = 0, EndColumn: int = 0, ErrorMessage: str = '', Reason: InterruptReason_f3d00dd2 = InterruptReason_f3d00dd2.Cancel, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``Name`` can be another ``InterruptEngineEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            Name (str, optional): Name value
            SourceCode (str, optional): SourceCode value
            StartLine (int, optional): StartLine value
            StartColumn (int, optional): StartColumn value
            EndLine (int, optional): EndLine value
            EndColumn (int, optional): EndColumn value
            ErrorMessage (str, optional): ErrorMessage value
            Reason (InterruptReason, optional): Reason value
        """
        super().__init__(**kwargs)
        if isinstance(Name, InterruptEngineEvent):
            oth: InterruptEngineEvent = Name
            self._name = oth.Name
            self._source_code = oth.SourceCode
            self._start_line = oth.StartLine
            self._start_column = oth.StartColumn
            self._end_line = oth.EndLine
            self._end_column = oth.EndColumn
            self._error_message = oth.ErrorMessage
            self._reason = oth.Reason
            return
        else:
            self._name = Name
            self._source_code = SourceCode
            self._start_line = StartLine
            self._start_column = StartColumn
            self._end_line = EndLine
            self._end_column = EndColumn
            self._error_message = ErrorMessage
            self._reason = Reason



    @property
    def Name(self) -> str:
        """
        fully qualified name to address the module or function affected by the event that took place.
        
        If the module or function can't be addressed by name (for example, in case that a runtime-generated eval-module is executed), this string is empty.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def SourceCode(self) -> str:
        """
        source code of the Module affected by the event that took place.
        
        If the source can be accessed using the ModuleName, or if the source is unknown (executing compiled code), this string can be empty.
        """
        return self._source_code
    
    @SourceCode.setter
    def SourceCode(self, value: str) -> None:
        self._source_code = value

    @property
    def StartLine(self) -> int:
        """
        contains the first line in the module's source code that is affected by the event that took place.
        
        If \"name\" addresses a function, all line and column values are nevertheless given relative to the module's source. If source code is not available, this value addresses a binary position in the compiled code.
        """
        return self._start_line
    
    @StartLine.setter
    def StartLine(self, value: int) -> None:
        self._start_line = value

    @property
    def StartColumn(self) -> int:
        """
        contains the first column in the \"StartLine\" that is affected by the event that took place.
        """
        return self._start_column
    
    @StartColumn.setter
    def StartColumn(self, value: int) -> None:
        self._start_column = value

    @property
    def EndLine(self) -> int:
        """
        contains the last line in the module's source code that is affected by the event that took place.
        """
        return self._end_line
    
    @EndLine.setter
    def EndLine(self, value: int) -> None:
        self._end_line = value

    @property
    def EndColumn(self) -> int:
        """
        contains the first column in the \"EndLine\" which is NOT affected by the event that took place.
        """
        return self._end_column
    
    @EndColumn.setter
    def EndColumn(self, value: int) -> None:
        self._end_column = value

    @property
    def ErrorMessage(self) -> str:
        """
        error message.
        
        Only valid if Reason is RuntimeError or CompileError.
        """
        return self._error_message
    
    @ErrorMessage.setter
    def ErrorMessage(self, value: str) -> None:
        self._error_message = value

    @property
    def Reason(self) -> InterruptReason_f3d00dd2:
        """
        contains the interrupt reason.
        """
        return self._reason
    
    @Reason.setter
    def Reason(self, value: InterruptReason_f3d00dd2) -> None:
        self._reason = value


__all__ = ['InterruptEngineEvent']