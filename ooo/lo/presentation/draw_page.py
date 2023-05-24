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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.presentation
from __future__ import annotations
import typing
from abc import abstractproperty
from ..document.link_target import LinkTarget as LinkTarget_ca220c5c
from ..drawing.draw_page import DrawPage as DrawPage_a56e0aff
if typing.TYPE_CHECKING:
    from com.sun.star.presentation.FadeEffect import FadeEffectProto
    from com.sun.star.presentation.AnimationSpeed import AnimationSpeedProto

class DrawPage(LinkTarget_ca220c5c, DrawPage_a56e0aff):
    """
    Service Class

    This is the service provided by a com.sun.star.drawing.DrawPage inside a PresentationDocument.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API DrawPage <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1presentation_1_1DrawPage.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.DrawPage'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Change(self) -> int:
        """
        specifies how the page change is triggered.
        
        If this is 0, the user must click to start each object animation and to change the page. If set to 1, the page is automatically switched. If it is set to 2, all object effects run automatically, but the user has to click on the page to change it.
        """
        ...

    @abstractproperty
    def DateTimeFormat(self) -> int:
        """
        defines the format that is used to format a date and time text field on this page.
        
        This is only used if IsDateTimeFixed is FALSE.
        """
        ...

    @abstractproperty
    def DateTimeText(self) -> str:
        """
        defines the text that is displayed in a date and time textfield rendered on this page.
        
        This value is only used if IsDateTimeFixed is TRUE.
        """
        ...

    @abstractproperty
    def Duration(self) -> int:
        """
        If the property com.sun.star.drawing.DrawPage.Change is set to 1, this is the time in seconds this page is shown before switching to the next page.
        """
        ...

    @abstractproperty
    def Effect(self) -> FadeEffectProto:
        """
        This is the effect that is used to fade in this page.
        """
        ...

    @abstractproperty
    def FooterText(self) -> str:
        """
        defines the text that is displayed in a footer textfield rendered on this page.
        """
        ...

    @abstractproperty
    def HeaderText(self) -> str:
        """
        defines the text that is displayed in a header textfield rendered on this page.
        """
        ...

    @abstractproperty
    def HighResDuration(self) -> float:
        """
        If the property com.sun.star.drawing.DrawPage.Change is set to 1, this is the time in seconds this page is shown before switching to the next page, also permitting sub-second precision here.
        """
        ...

    @abstractproperty
    def IsDateTimeFixed(self) -> bool:
        """
        defines if a date and time text field shows a fixed string value or the current date on this page.
        """
        ...

    @abstractproperty
    def IsDateTimeVisible(self) -> bool:
        """
        defines if a date and time presentation shape from the master page is visible on this page.
        """
        ...

    @abstractproperty
    def IsFooterVisible(self) -> bool:
        """
        defines if a footer presentation shape from the master page is visible on this page.
        """
        ...

    @abstractproperty
    def IsHeaderVisible(self) -> bool:
        """
        defines if a header presentation shape from the master page is visible on this page.
        """
        ...

    @abstractproperty
    def IsPageNumberVisible(self) -> bool:
        """
        defines if a page number presentation shape from the master page is visible on this page.
        """
        ...

    @abstractproperty
    def Layout(self) -> int:
        """
        If this property is not ZERO, this number specifies a presentation layout for this page.
        """
        ...

    @abstractproperty
    def Speed(self) -> AnimationSpeedProto:
        """
        Defines the speed of the fade-in effect of this page.
        """
        ...

    @abstractproperty
    def TransitionDuration(self) -> float:
        """
        Specifies slide transition time in seconds.
        
        **since**
        
            LibreOffice 6.1
        """
        ...


__all__ = ['DrawPage']

