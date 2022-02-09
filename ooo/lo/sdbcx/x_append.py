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
# Namespace: com.sun.star.sdbcx
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XAppend(XInterface_8f010a43):
    """
    is used for creating and appending new objects to a specific container.

    See Also:
        `API XAppend <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XAppend.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.XAppend'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbcx.XAppend'

    @abstractmethod
    def appendByDescriptor(self, descriptor: 'XPropertySet_bc180bfa') -> None:
        """
        creates a new object using the given descriptor and appends it to the related container.
        
        Note:  The descriptor will not be changed and can be used again to append another object.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """


__all__ = ['XAppend']

