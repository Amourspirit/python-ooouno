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
# Namespace: com.sun.star.drawing
from abc import abstractproperty
from ..document.header_footer_settings import HeaderFooterSettings as HeaderFooterSettings_5acd1070
from ..document.settings import Settings as Settings_b2bc0bb8

class DocumentSettings(HeaderFooterSettings_5acd1070, Settings_b2bc0bb8):
    """
    Service Class

    describes properties that apply to the whole drawing document.

    See Also:
        `API DocumentSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1DocumentSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.DocumentSettings'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def IsPrintFitPage(self) -> bool:
        """
        enables or disables the fitting of the page to the printable area during print
        """
    @abstractproperty
    def IsPrintTilePage(self) -> bool:
        """
        if this is true and the paper size for printing is larger than the paper size of the printer than the content is tiled over multiple pages.
        """
    @abstractproperty
    def MeasureUnit(self) -> int:
        """
        This is the default logical measure unit that is used for string formatting inside the document, f.e.
        
        the measure text
        """
    @abstractproperty
    def PageNumberFormat(self) -> int:
        """
        is the number format used for page number fields
        
        Values 0-7 are supported.
        """
    @abstractproperty
    def ParagraphSummation(self) -> bool:
        """
        If this is true, the distance between two paragraphs is the sum of ParaBottomMargin of the previous and ParaTopMargin of the next paragraph.
        
        If false, only the greater of the two is chosen.
        """
    @abstractproperty
    def ScaleDenominator(self) -> int:
        """
        is the denominator for the logical scale of the document
        """
    @abstractproperty
    def ScaleNumerator(self) -> int:
        """
        is the numerator for the logical scale of the document
        """

__all__ = ['DocumentSettings']

