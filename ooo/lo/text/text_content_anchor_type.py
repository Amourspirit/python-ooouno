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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.text
# Libre Office Version: 7.4
from enum import Enum


class TextContentAnchorType(Enum):
    """
    Enum Class

    

    See Also:
        `API TextContentAnchorType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text.html#a470b1caeda4ff15fee438c8ff9e3d834>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextContentAnchorType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.text.TextContentAnchorType'

    AS_CHARACTER = 'AS_CHARACTER'
    """
    The object is anchored instead of a character.
    """
    AT_CHARACTER = 'AT_CHARACTER'
    """
    The object is anchored to a character.
    """
    AT_FRAME = 'AT_FRAME'
    """
    The object is anchored to a text frame.
    """
    AT_PAGE = 'AT_PAGE'
    """
    The object is anchored to the page.
    """
    AT_PARAGRAPH = 'AT_PARAGRAPH'
    """
    The anchor of the object is set at the top left position of the paragraph.
    """

__all__ = ['TextContentAnchorType']

