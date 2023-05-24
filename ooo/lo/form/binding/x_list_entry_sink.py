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
# Namespace: com.sun.star.form.binding
from __future__ import annotations
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_list_entry_source import XListEntrySource as XListEntrySource_576b103c

class XListEntrySink(XInterface_8f010a43):
    """
    specifies support for indirect manipulation of a string list

    See Also:
        `API XListEntrySink <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1binding_1_1XListEntrySink.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.binding'
    __ooo_full_ns__: str = 'com.sun.star.form.binding.XListEntrySink'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.binding.XListEntrySink'

    @abstractmethod
    def getListEntrySource(self) -> XListEntrySource_576b103c:
        """
        retrieves the current source for the list entries of the component.
        """
        ...
    @abstractmethod
    def setListEntrySource(self, Source: XListEntrySource_576b103c) -> None:
        """
        sets the new source for the list entries of the component
        
        The list represented by this component will be cleared, and initially filled with the entries from the new list source.
        """
        ...

__all__ = ['XListEntrySink']

