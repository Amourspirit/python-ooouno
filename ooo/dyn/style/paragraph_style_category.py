# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.style
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ParagraphStyleCategory(metaclass=UnoConstMeta, type_name="com.sun.star.style.ParagraphStyleCategory", name_space="com.sun.star.style"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.style.ParagraphStyleCategory``"""
        pass

    class ParagraphStyleCategoryEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.style.ParagraphStyleCategory", name_space="com.sun.star.style"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.style.ParagraphStyleCategory`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.style import ParagraphStyleCategory as ParagraphStyleCategory
    else:
        # keep document generators happy
        from ...lo.style.paragraph_style_category import ParagraphStyleCategory as ParagraphStyleCategory

    class ParagraphStyleCategoryEnum(IntEnum):
        """
        Enum of Const Class ParagraphStyleCategory

        These constants are used to specify the category of paragraph styles in text documents.
        """
        TEXT = ParagraphStyleCategory.TEXT
        """
        is applied to styles that are used for common text.
        """
        CHAPTER = ParagraphStyleCategory.CHAPTER
        """
        is applied to styles that are used as headings.
        """
        LIST = ParagraphStyleCategory.LIST
        """
        is applied to styles that used in numberings and lists.
        """
        INDEX = ParagraphStyleCategory.INDEX
        """
        is applied to styles that are used in indexes.
        """
        EXTRA = ParagraphStyleCategory.EXTRA
        """
        is applied to styles that are used in special regions like headers, footers, and footnote text.
        """
        HTML = ParagraphStyleCategory.HTML
        """
        is applied to styles that are used to support HTML.
        """

__all__ = ['ParagraphStyleCategory', 'ParagraphStyleCategoryEnum']
