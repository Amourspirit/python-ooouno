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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .xsql_query_composer import XSQLQueryComposer as XSQLQueryComposer_dd370ce7

class XSQLQueryComposerFactory(XInterface_8f010a43):
    """
    is a factory for instances of service com.sun.star.sdb.SQLQueryComposer.

    See Also:
        `API XSQLQueryComposerFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XSQLQueryComposerFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.XSQLQueryComposerFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.XSQLQueryComposerFactory'

    @abstractmethod
    def createQueryComposer(self) -> 'XSQLQueryComposer_dd370ce7':
        """
        creates a new query composer.
        """

__all__ = ['XSQLQueryComposerFactory']

