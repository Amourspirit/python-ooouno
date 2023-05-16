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
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoEnumMeta
    class TextContentAnchorType(metaclass=UnoEnumMeta, type_name="com.sun.star.text.TextContentAnchorType", name_space="com.sun.star.text"):
        """Dynamically created class that represents ``com.sun.star.text.TextContentAnchorType`` Enum. Class loosly mimics Enum"""
        pass
else:
    from com.sun.star.text.TextContentAnchorType import AS_CHARACTER as TEXT_CONTENT_ANCHOR_TYPE_AS_CHARACTER
    from com.sun.star.text.TextContentAnchorType import AT_CHARACTER as TEXT_CONTENT_ANCHOR_TYPE_AT_CHARACTER
    from com.sun.star.text.TextContentAnchorType import AT_FRAME as TEXT_CONTENT_ANCHOR_TYPE_AT_FRAME
    from com.sun.star.text.TextContentAnchorType import AT_PAGE as TEXT_CONTENT_ANCHOR_TYPE_AT_PAGE
    from com.sun.star.text.TextContentAnchorType import AT_PARAGRAPH as TEXT_CONTENT_ANCHOR_TYPE_AT_PARAGRAPH


    class TextContentAnchorType(uno.Enum):
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

        AS_CHARACTER = TEXT_CONTENT_ANCHOR_TYPE_AS_CHARACTER
        """
        The object is anchored instead of a character.
        """
        AT_CHARACTER = TEXT_CONTENT_ANCHOR_TYPE_AT_CHARACTER
        """
        The object is anchored to a character.
        """
        AT_FRAME = TEXT_CONTENT_ANCHOR_TYPE_AT_FRAME
        """
        The object is anchored to a text frame.
        """
        AT_PAGE = TEXT_CONTENT_ANCHOR_TYPE_AT_PAGE
        """
        The object is anchored to the page.
        """
        AT_PARAGRAPH = TEXT_CONTENT_ANCHOR_TYPE_AT_PARAGRAPH
        """
        The anchor of the object is set at the top left position of the paragraph.
        """

__all__ = ['TextContentAnchorType']

