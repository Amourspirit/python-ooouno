# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbcx
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6

class XIndexesSupplier(XInterface_8f010a43):
    """
    provides for access to a container of indexes, typically used for a table definition object.

    See Also:
        `API XIndexesSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XIndexesSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.XIndexesSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbcx.XIndexesSupplier'

    @abstractmethod
    def getIndexes(self) -> 'XNameAccess_e2ab0cf6':
        """
        returns the container of indexes.
        """
        ...

__all__ = ['XIndexesSupplier']

