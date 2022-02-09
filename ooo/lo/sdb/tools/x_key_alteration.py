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
# Namespace: com.sun.star.sdb.tools
import typing
from abc import abstractmethod
from .x_connection_supplier import XConnectionSupplier as XConnectionSupplier_57f3105c
if typing.TYPE_CHECKING:
    from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XKeyAlteration(XConnectionSupplier_57f3105c):
    """
    allows to alter the keys of a table.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XKeyAlteration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1tools_1_1XKeyAlteration.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.tools'
    __ooo_full_ns__: str = 'com.sun.star.sdb.tools.XKeyAlteration'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.tools.XKeyAlteration'

    @abstractmethod
    def addKey(self, table: 'XPropertySet_bc180bfa', descriptor: 'XPropertySet_bc180bfa') -> None:
        """
        creates a new object using the given descriptor and appends it to the related container.
        
        Note:  The descriptor will not be changed and can be used again to append another object.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    @abstractmethod
    def dropKey(self, table: 'XPropertySet_bc180bfa', key: 'XPropertySet_bc180bfa') -> None:
        """
        drops an object of the related container identified by its name.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """


__all__ = ['XKeyAlteration']

