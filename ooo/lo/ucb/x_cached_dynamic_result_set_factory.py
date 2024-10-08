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
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_content_identifier_mapping import XContentIdentifierMapping as XContentIdentifierMapping_56ef1044
    from .x_dynamic_result_set import XDynamicResultSet as XDynamicResultSet_e0360d0a

class XCachedDynamicResultSetFactory(XInterface_8f010a43):
    """
    creates a CachedDynamicResultSet.
    
    Pay attention to instantiate this helper on client side where your want to read the data respectively where you have instantiated the listener to the XDynamicResultSet.
    
    The needed stub on server side can be created using XCachedDynamicResultSetStubFactory.

    See Also:
        `API XCachedDynamicResultSetFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XCachedDynamicResultSetFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XCachedDynamicResultSetFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XCachedDynamicResultSetFactory'

    @abstractmethod
    def createCachedDynamicResultSet(self, SourceStub: XDynamicResultSet_e0360d0a, ContentIdentifierMapping: XContentIdentifierMapping_56ef1044) -> XDynamicResultSet_e0360d0a:
        """
        creates a remote optimizes XDynamicResultSet.
        """
        ...

__all__ = ['XCachedDynamicResultSetFactory']

