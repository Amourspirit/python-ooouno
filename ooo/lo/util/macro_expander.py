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
# Libre Office Version: 7.3
# Namespace: com.sun.star.util
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from .x_macro_expander import XMacroExpander as XMacroExpander_c8360c47

class MacroExpander(XComponent_98dc0ab5, XMacroExpander_c8360c47):
    """
    Service Class

    This meta service supports the XMacroExpander interface for expanding arbitrary macro expressions, i.e.
    
    substitute macro names. The purpose of this service is to separate the use of macrofied strings, e.g. urls from the use of services.
    
    **since**
    
        OOo 1.1.2
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API MacroExpander <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1util_1_1MacroExpander.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.MacroExpander'
    __ooo_type_name__: str = 'service'



__all__ = ['MacroExpander']

