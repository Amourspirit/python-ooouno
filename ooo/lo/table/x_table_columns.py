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
# Namespace: com.sun.star.table
from abc import abstractmethod
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d

class XTableColumns(XIndexAccess_f0910d6d):
    """
    provides methods to access columns via index and to insert and remove columns.

    See Also:
        `API XTableColumns <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XTableColumns.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.XTableColumns'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.table.XTableColumns'

    @abstractmethod
    def insertByIndex(self, nIndex: int, nCount: int) -> None:
        """
        inserts new columns.
        """
    @abstractmethod
    def removeByIndex(self, nIndex: int, nCount: int) -> None:
        """
        deletes columns.
        """

__all__ = ['XTableColumns']

