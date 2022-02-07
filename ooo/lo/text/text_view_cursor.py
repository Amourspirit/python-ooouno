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
from .text_layout_cursor import TextLayoutCursor as TextLayoutCursor_e5530d6e
from ..view.x_screen_cursor import XScreenCursor as XScreenCursor_bc4a0bf9

class TextViewCursor(TextLayoutCursor_e5530d6e, XScreenCursor_bc4a0bf9):
    """
    Service Class

    A TextViewCursor is a TextRange which can travel within a view of a Text object.

    See Also:
        `API TextViewCursor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextViewCursor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextViewCursor'
    __ooo_type_name__: str = 'service'


__all__ = ['TextViewCursor']

