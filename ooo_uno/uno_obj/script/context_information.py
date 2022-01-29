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
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class ContextInformation(object):
    """
    Struct Class

    provides information about a certain stack frame.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ContextInformation <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1ContextInformation.html>`_


    Note:
        | At runtime ContextInformation will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | ContextInformation is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, EndColumn: typing.Optional[int] = None, EndLine: typing.Optional[int] = None, LocalVariableNames: 'typing.Optional[typing.List[str]]' = None, Name: typing.Optional[str] = None, SourceCode: typing.Optional[str] = None, StartColumn: typing.Optional[int] = None, StartLine: typing.Optional[int] = None):
        self._end_column = EndColumn
        self._end_line = EndLine
        self._local_variable_names = LocalVariableNames
        self._name = Name
        self._source_code = SourceCode
        self._start_column = StartColumn
        self._start_line = StartLine

    @property
    def EndColumn(self) -> int:
        """
        contains the first column in the EndLine that is NOT associated with the context.
        """
        return self._end_column
    
    @EndColumn.setter
    def EndColumn(self, value: int) -> None:
        self._end_column = value

    @property
    def EndLine(self) -> int:
        """
        contains the last line in the module's source code associated with the context.
        """
        return self._end_line
    
    @EndLine.setter
    def EndLine(self, value: int) -> None:
        self._end_line = value

    @property
    def LocalVariableNames(self) -> 'typing.List[str]':
        """
        Get all names of the local variable in this context.
        """
        return self._local_variable_names
    
    @LocalVariableNames.setter
    def LocalVariableNames(self, value: 'typing.List[str]') -> None:
        self._local_variable_names = value

    @property
    def Name(self) -> str:
        """
        Full qualified name to address the module or function associated with the context.
        
        If the module or function can't be addressed by name, e.g., in case that a runtime generated eval-module is executed, this string is empty
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def SourceCode(self) -> str:
        """
        Source code of the Module, that is associated with the context.
        
        If the source can be accessed using the ModuleName or if the source is unknown (executing compiled code) this string can be empty.
        """
        return self._source_code
    
    @SourceCode.setter
    def SourceCode(self, value: str) -> None:
        self._source_code = value

    @property
    def StartColumn(self) -> int:
        """
        contains the first column in the StartLine associated with the context.
        """
        return self._start_column
    
    @StartColumn.setter
    def StartColumn(self, value: int) -> None:
        self._start_column = value

    @property
    def StartLine(self) -> int:
        """
        contains the first line in the module's source code associated with the context.
        
        If \"name\" addresses a function, all line and column values are nevertheless given relative to the module's source. If source code is not available, this value addresses a binary position in the compiled code.
        """
        return self._start_line
    
    @StartLine.setter
    def StartLine(self, value: int) -> None:
        self._start_line = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global ContextInformation
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('EndColumn', 'EndLine', 'LocalVariableNames', 'Name', 'SourceCode', 'StartColumn', 'StartLine')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.script.ContextInformation')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ContextInformation = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['ContextInformation']
