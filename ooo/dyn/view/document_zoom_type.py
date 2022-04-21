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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.view
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.view import DocumentZoomType as DocumentZoomType
    if hasattr(DocumentZoomType, '_constants') and isinstance(DocumentZoomType._constants, dict):
        DocumentZoomType._constants['__ooo_ns__'] = 'com.sun.star.view'
        DocumentZoomType._constants['__ooo_full_ns__'] = 'com.sun.star.view.DocumentZoomType'
        DocumentZoomType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global DocumentZoomTypeEnum
        ls = [f for f in dir(DocumentZoomType) if not callable(getattr(DocumentZoomType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(DocumentZoomType, name)
        DocumentZoomTypeEnum = IntEnum('DocumentZoomTypeEnum', _dict)
    build_enum()
else:
    from ...lo.view.document_zoom_type import DocumentZoomType as DocumentZoomType

    class DocumentZoomTypeEnum(IntEnum):
        """
        Enum of Const Class DocumentZoomType

        These constants specify how the document content is zoomed into the document view.
        """
        OPTIMAL = DocumentZoomType.OPTIMAL
        """
        The page content width (excluding margins) at the current selection is fit into the view.
        """
        PAGE_WIDTH = DocumentZoomType.PAGE_WIDTH
        """
        The page width at the current selection is fit into the view.
        """
        ENTIRE_PAGE = DocumentZoomType.ENTIRE_PAGE
        """
        A complete page of the document is fit into the view.
        """
        BY_VALUE = DocumentZoomType.BY_VALUE
        """
        The zoom is relative and is to be set via the property ViewSettings.ZoomValue.
        """
        PAGE_WIDTH_EXACT = DocumentZoomType.PAGE_WIDTH_EXACT
        """
        The page width at the current selection is fit into the view, with the view ends exactly at the end of the page.
        """

__all__ = ['DocumentZoomType', 'DocumentZoomTypeEnum']
