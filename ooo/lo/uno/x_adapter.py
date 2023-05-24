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
# Namespace: com.sun.star.uno
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_reference import XReference as XReference_8ecb0a41

class XAdapter(XInterface_8f010a43):
    """
    This is the server-side interface to a weak adapter.
    
    The implementation of XAdapter must know but not hold the adapted object, because it must not affect the lifetime of the adapted object.

    See Also:
        `API XAdapter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XAdapter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.XAdapter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.uno.XAdapter'

    @abstractmethod
    def addReference(self, xRef: XReference_8ecb0a41) -> None:
        """
        adds a reference to the adapter.
        
        All added references are called when the adapted object dies.
        """
        ...
    @abstractmethod
    def queryAdapted(self) -> XInterface_8f010a43:
        """
        queries the adapted object if it is alive.
        """
        ...
    @abstractmethod
    def removeReference(self, xRef: XReference_8ecb0a41) -> None:
        """
        removes a reference from the adapter.
        """
        ...

__all__ = ['XAdapter']

