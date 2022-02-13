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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XRename(XInterface_8f010a43):
    """
    supports the renaming of definition objects.
    
    This is a very desirable feature which is not supported by all databases. There is no standard SQL statement provided for this feature.

    See Also:
        `API XRename <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XRename.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.XRename'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbcx.XRename'

    @abstractmethod
    def rename(self, newName: str) -> None:
        """
        is intended to alter the name of an object.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """

__all__ = ['XRename']

