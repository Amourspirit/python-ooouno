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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbc
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XBatchExecution(XInterface_8f010a43):
    """
    is used for collecting and executing a set of SQL statements.

    See Also:
        `API XBatchExecution <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XBatchExecution.html>`_
    """

    @abstractmethod
    def addBatch(self, sql: str) -> None:
        """
        adds a SQL command to the current batch of commands for the statement object.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def clearBatch(self) -> None:
        """
        makes the set of commands in the current batch empty.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def executeBatch(self) -> 'typing.List[int]':
        """
        submits a batch of commands to the database for execution.

        Raises:
            SQLException: ``SQLException``
        """

__all__ = ['XBatchExecution']

