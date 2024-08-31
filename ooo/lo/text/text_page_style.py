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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_text import XText as XText_690408ca
    from .x_text_columns import XTextColumns as XTextColumns_b17f0bab
    from ..util.color import Color as Color_68e908c5

class TextPageStyle(ABC):
    """
    Service Class

    represents a page style for a text document.
    
    This service extends the service com.sun.star.style.PageStyle with specific properties for text documents.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API TextPageStyle <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextPageStyle.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextPageStyle'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def FooterText(self) -> XText_690408ca:
        """
        contains the interface to the text of the footer.
        """
        ...

    @property
    @abstractmethod
    def FooterTextFirst(self) -> XText_690408ca:
        """
        contains the interface to the text of the footer of a first page.
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @property
    @abstractmethod
    def FooterTextLeft(self) -> XText_690408ca:
        """
        contains the interface to the text of the footer of a left page.
        """
        ...

    @property
    @abstractmethod
    def FooterTextRight(self) -> XText_690408ca:
        """
        contains the interface to the text of the footer of a right page.
        """
        ...

    @property
    @abstractmethod
    def FootnoteHeight(self) -> int:
        """
        contains the maximum height of the footnote area (in 1/100 mm).
        
        If set to zero, the height of the current page is used as limit.
        """
        ...

    @property
    @abstractmethod
    def FootnoteLineAdjust(self) -> int:
        """
        contains the adjustment of the separator line between the text and the footnote area.
        """
        ...

    @property
    @abstractmethod
    def FootnoteLineColor(self) -> Color_68e908c5:
        """
        contains the color of the separator line between the text and the footnote area.
        """
        ...

    @property
    @abstractmethod
    def FootnoteLineDistance(self) -> int:
        """
        contains the distance between the footnote area and the separator line between the text and the footnote area (in 1/100 mm).
        """
        ...

    @property
    @abstractmethod
    def FootnoteLineRelativeWidth(self) -> int:
        """
        contains the relative width of the separator line between the text and the footnote area (in percent).
        """
        ...

    @property
    @abstractmethod
    def FootnoteLineTextDistance(self) -> int:
        """
        contains the distance between the text and the separator line between the text and the footnote area (in 1/100 mm).
        """
        ...

    @property
    @abstractmethod
    def FootnoteLineWeight(self) -> int:
        """
        contains the weight of the separator line between the text and the footnote area (in 1/100 mm).
        """
        ...

    @property
    @abstractmethod
    def HeaderText(self) -> XText_690408ca:
        """
        contains the interface to the text of the header.
        """
        ...

    @property
    @abstractmethod
    def HeaderTextFirst(self) -> XText_690408ca:
        """
        contains the interface to the text of the header of first pages.
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @property
    @abstractmethod
    def HeaderTextLeft(self) -> XText_690408ca:
        """
        contains the interface to the text of the header of left pages.
        """
        ...

    @property
    @abstractmethod
    def HeaderTextRight(self) -> XText_690408ca:
        """
        contains the interface to the text of the header of right pages.
        """
        ...

    @property
    @abstractmethod
    def RegisterModeActive(self) -> bool:
        """
        determines whether the register mode is active on that page.
        """
        ...

    @property
    @abstractmethod
    def RegisterParagraphStyle(self) -> str:
        """
        contains the name of the paragraph style that is used as reference of the register mode.
        """
        ...

    @property
    @abstractmethod
    def TextColumns(self) -> XTextColumns_b17f0bab:
        """
        contains the column settings of the page.
        """
        ...


__all__ = ['TextPageStyle']

