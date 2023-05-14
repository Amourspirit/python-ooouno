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
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_presentation import XPresentation as XPresentation_30890f78

class Presentation(XPropertySet_bc180bfa, XPresentation_30890f78):
    """
    Service Class

    This service is a presentation that is available from a PresentationDocument via the XPresentationSupplier interface.

    See Also:
        `API Presentation <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1presentation_1_1Presentation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.Presentation'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def AllowAnimations(self) -> bool:
        """
        enables/disables the shape animations.
        """
        ...

    @abstractproperty
    def CustomShow(self) -> str:
        """
        If this string is not empty, it contains the name of a customized show that is used for the presentation.
        """
        ...

    @abstractproperty
    def FirstPage(self) -> str:
        """
        If this string is not empty, it contains the name of the page where the presentation is started.
        """
        ...

    @abstractproperty
    def IsAlwaysOnTop(self) -> bool:
        """
        If this property is set to TRUE, the window of the presentation is always on top of all other windows.
        """
        ...

    @abstractproperty
    def IsAutomatic(self) -> bool:
        """
        If this property is TRUE, all pages are changed automatically.
        
        This overrides the properties of the pages.
        """
        ...

    @abstractproperty
    def IsEndless(self) -> bool:
        """
        If this property is set to TRUE, the presentation is repeated endlessly.
        """
        ...

    @abstractproperty
    def IsFullScreen(self) -> bool:
        """
        If this property is set to TRUE, the presentation runs in full-screen mode.
        """
        ...

    @abstractproperty
    def IsLivePresentation(self) -> bool:
        """
        With this property, you can set the presentation to live mode.
        
        Implementations that have no live mode capability may ignore this property and always return false.
        """
        ...

    @abstractproperty
    def IsMouseVisible(self) -> bool:
        """
        If this property is TRUE, the mouse is visible during the presentation.
        """
        ...

    @abstractproperty
    def Pause(self) -> int:
        """
        is the duration of the black screen after the presentation has finished.
        
        If this is set to 0, no black screen is shown.
        """
        ...

    @abstractproperty
    def StartWithNavigator(self) -> bool:
        """
        If this is set to TRUE, the Navigator is opened at the start of the presentation.
        """
        ...

    @abstractproperty
    def UsePen(self) -> bool:
        """
        If this is TRUE, a pen is shown during presentation.
        
        You can draw on the presentation with this pen.
        """
        ...


__all__ = ['Presentation']

