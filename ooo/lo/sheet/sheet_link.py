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
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from ..util.x_refreshable import XRefreshable as XRefreshable_b0d60b81

class SheetLink(XPropertySet_bc180bfa, XNamed_a6520b08, XRefreshable_b0d60b81):
    """
    Service Class

    represents a sheet link.
    
    A sheet link contains the source data of linked sheets, i.e. the URL and sheet name of the external document.
    
    To create a linked sheet, the sheet which will be used as linked sheet has to exist already. The method XSheetLinkable.link() creates a SheetLink object in the document's SheetLinks collection and links the sheet to the specified external sheet.

    See Also:
        `API SheetLink <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SheetLink.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SheetLink'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Filter(self) -> str:
        """
        specifies the name of the filter needed to load the source document.
        """

    @abstractproperty
    def FilterOptions(self) -> str:
        """
        specifies the filter options needed to load the source document.
        """

    @abstractproperty
    def Url(self) -> str:
        """
        specifies the URL of the source document.
        """



__all__ = ['SheetLink']

