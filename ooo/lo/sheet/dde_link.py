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
from ..container.x_named import XNamed as XNamed_a6520b08
from .xdde_link import XDDELink as XDDELink_8cc609d4
from .xdde_link_results import XDDELinkResults as XDDELinkResults_dce00cc6
from ..util.x_refreshable import XRefreshable as XRefreshable_b0d60b81

class DDELink(XNamed_a6520b08, XDDELink_8cc609d4, XDDELinkResults_dce00cc6, XRefreshable_b0d60b81):
    """
    Service Class

    represents a DDE link.
    
    A DDE link controls the results of a DDE spreadsheet formula.
    
    **since**
    
        OOo 3.0

    See Also:
        `API DDELink <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DDELink.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DDELink'
    __ooo_type_name__: str = 'service'


__all__ = ['DDELink']

