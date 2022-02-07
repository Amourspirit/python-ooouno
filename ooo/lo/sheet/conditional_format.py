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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_conditional_format import XConditionalFormat as XConditionalFormat_be90e56
if typing.TYPE_CHECKING:
    from .x_sheet_cell_ranges import XSheetCellRanges as XSheetCellRanges_edef0d52

class ConditionalFormat(XPropertySet_bc180bfa, XConditionalFormat_be90e56):
    """
    Service Class

    represents a conditional format

    See Also:
        `API ConditionalFormat <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1ConditionalFormat.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.ConditionalFormat'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ID(self) -> int:
        """
        """
    @abstractproperty
    def Range(self) -> 'XSheetCellRanges_edef0d52':
        """
        represents the range for the conditional format All ranges have to be in the same sheet.
        """

__all__ = ['ConditionalFormat']

