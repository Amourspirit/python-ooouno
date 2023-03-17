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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XFunctionDescriptions(XIndexAccess_f0910d6d):
    """
    provides access to the property sequence of a function description via function index or identifier.
    
    The container access methods return a sequence of com.sun.star.beans.PropertyValue structs. The properties contained in the sequence are collected in the service FunctionDescription.

    See Also:
        `API XFunctionDescriptions <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XFunctionDescriptions.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XFunctionDescriptions'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XFunctionDescriptions'

    @abstractmethod
    def getById(self, nId: int) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        finds a function description by the identifier of the function.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XFunctionDescriptions']

