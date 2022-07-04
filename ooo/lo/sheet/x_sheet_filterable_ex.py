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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from .x_sheet_filterable import XSheetFilterable as XSheetFilterable_eeed0d6c
if typing.TYPE_CHECKING:
    from .x_sheet_filter_descriptor import XSheetFilterDescriptor as XSheetFilterDescriptor_47cc0ff7

class XSheetFilterableEx(XSheetFilterable_eeed0d6c):
    """
    represents something from which criteria for filtering can be read.
    
    In general the current object will be used only to create the descriptor to filter another object, i.e. the advanced filter feature in a spreadsheet.

    See Also:
        `API XSheetFilterableEx <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetFilterableEx.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetFilterableEx'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetFilterableEx'

    @abstractmethod
    def createFilterDescriptorByObject(self, xObject: 'XSheetFilterable_eeed0d6c') -> 'XSheetFilterDescriptor_47cc0ff7':
        """
        creates a filter descriptor for the specified filterable object from the contents of this object.
        """
        ...

__all__ = ['XSheetFilterableEx']

