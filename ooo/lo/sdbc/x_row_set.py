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
# Namespace: com.sun.star.sdbc
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_result_set import XResultSet as XResultSet_98e30aa7
if typing.TYPE_CHECKING:
    from .x_row_set_listener import XRowSetListener as XRowSetListener_d3580ca6

class XRowSet(XResultSet_98e30aa7):
    """
    enhances the functionality of a result set.
    
    It allows implementation of a special behavior for a result set and notifies an application on certain row set events such as a change in its value.
    
    The XRowSet interface is unique in that it is intended to be a software layer on top of an SDBC driver. Implementations of the RowSet interface can be provided by anyone.

    See Also:
        `API XRowSet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XRowSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XRowSet'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XRowSet'

    @abstractmethod
    def addRowSetListener(self, listener: XRowSetListener_d3580ca6) -> None:
        """
        adds the specified listener to receive the events \"cursorMoved\", \"rowChanged\", and \"rowSetChanged\".
        """
        ...
    @abstractmethod
    def execute(self) -> None:
        """
        populates a row set with data.
        
        The description of the data source and other important information for filling the row set with data.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def removeRowSetListener(self, listener: XRowSetListener_d3580ca6) -> None:
        """
        removes the specified listener.
        """
        ...

__all__ = ['XRowSet']

