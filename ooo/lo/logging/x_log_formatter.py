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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.logging
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .log_record import LogRecord as LogRecord_b0c20b70

class XLogFormatter(ABC):
    """
    specifies the interface to be used for formatting log records
    
    **since**
    
        OOo 2.3

    See Also:
        `API XLogFormatter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1logging_1_1XLogFormatter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.logging'
    __ooo_full_ns__: str = 'com.sun.star.logging.XLogFormatter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.logging.XLogFormatter'

    @abstractmethod
    def format(self, Record: LogRecord_b0c20b70) -> str:
        """
        formats the given log record for output
        
        A XLogHandler will call this method to format a given log record. The resulting string will be emitted to the handler's output channel, without processing it any further (except possibly encoding it with the handler's Encoding).
        """
        ...
    @abstractmethod
    def getHead(self) -> str:
        """
        returns the header string for the log
        
        This can be used to generate a header string, which by the XLogHandler is emitted to its output channel before actually logging any concrete LogRecord.
        
        For instance, a formatter might produce table-like plain text output, and could return a table-head string (potentially including line breaks) here.
        """
        ...
    @abstractmethod
    def getTail(self) -> str:
        """
        returns the footer string for the log
        
        This can be used to generate a footer string, which by the XLogHandler is emitted to its output channel before it is finally being closed.
        """
        ...

__all__ = ['XLogFormatter']

