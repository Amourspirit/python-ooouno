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
# Namespace: com.sun.star.text
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .text_content import TextContent as TextContent_a6810b4d
from .x_text_field import XTextField as XTextField_9a630aae

class TextField(TextContent_a6810b4d, XPropertySet_bc180bfa, XTextField_9a630aae):
    """
    Service Class

    A TextField is a TextContent which fades its textual representation into the text range to which it is anchored.
    
    **since**
    
        OOo 2.0.1

    See Also:
        `API TextField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextField'
    __ooo_type_name__: str = 'service'



__all__ = ['TextField']

