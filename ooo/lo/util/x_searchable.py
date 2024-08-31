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
# Namespace: com.sun.star.util
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
    from .x_search_descriptor import XSearchDescriptor as XSearchDescriptor_ef600d93

class XSearchable(XInterface_8f010a43):
    """
    enables the object to look for specified contents of the object (in particular, for a text range which contains a specific string pattern).
    
    Example: in a com.sun.star.text.TextDocument: set all \"search for\" to bold using findFirst()/findNext():

    See Also:
        `API XSearchable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XSearchable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XSearchable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XSearchable'

    @abstractmethod
    def createSearchDescriptor(self) -> XSearchDescriptor_ef600d93:
        """
        creates a SearchDescriptor which contains properties that specify a search in this container.
        """
        ...
    @abstractmethod
    def findAll(self, xDesc: XSearchDescriptor_ef600d93) -> XIndexAccess_f0910d6d:
        """
        searches the contained texts for all occurrences of whatever is specified.
        """
        ...
    @abstractmethod
    def findFirst(self, xDesc: XSearchDescriptor_ef600d93) -> XInterface_8f010a43:
        """
        searches the contained texts for the next occurrence of whatever is specified.
        """
        ...
    @abstractmethod
    def findNext(self, xStartAt: XInterface_8f010a43, xDesc: XSearchDescriptor_ef600d93) -> XInterface_8f010a43:
        """
        searches the contained texts for the next occurrence of whatever is specified.
        """
        ...

__all__ = ['XSearchable']

