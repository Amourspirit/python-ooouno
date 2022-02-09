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
if typing.TYPE_CHECKING:
    from .x_result_set import XResultSet as XResultSet_98e30aa7

class XGeneratedResultSet(XInterface_8f010a43):
    """
    provides a result set which gives access to automatically generated values after a new row was inserted.
    
    The relative order of columns in the result set returned by getGeneratedValues() must be the same as the relative order of the same columns as returned when executing a \"SELECT * FROM table\". This ensures that clients of this interface can reliably fetch the column values.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XGeneratedResultSet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XGeneratedResultSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XGeneratedResultSet'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XGeneratedResultSet'

    @abstractmethod
    def getGeneratedValues(self) -> 'XResultSet_98e30aa7':
        """
        gives access to automatically generated values after a new row was inserted.

        Raises:
            SQLException: ``SQLException``
        """


__all__ = ['XGeneratedResultSet']

