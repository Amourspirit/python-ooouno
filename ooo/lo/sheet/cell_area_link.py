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
from .x_area_link import XAreaLink as XAreaLink_98db0a80
from ..util.x_refreshable import XRefreshable as XRefreshable_b0d60b81

class CellAreaLink(XPropertySet_bc180bfa, XAreaLink_98db0a80, XRefreshable_b0d60b81):
    """
    Service Class

    represents a linked cell range.
    
    A linked cell range is a range which is linked to an equal-sized range in an external document. The contents of the external range is copied into the range of this document.
    
    **since**
    
        OOo 2.0

    See Also:
        `API CellAreaLink <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1CellAreaLink.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.CellAreaLink'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Filter(self) -> str:
        """
        specifies the name of the filter used to load the source document.
        """

    @abstractproperty
    def FilterOptions(self) -> str:
        """
        specifies the filter options needed to load the source document.
        """

    @abstractproperty
    def RefreshDelay(self) -> int:
        """
        specifies the delay time between two refresh actions in seconds.
        """

    @abstractproperty
    def RefreshPeriod(self) -> int:
        """
        specifies the time between two refresh actions in seconds.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def Url(self) -> str:
        """
        specifies the URL of the source document.
        """



__all__ = ['CellAreaLink']

