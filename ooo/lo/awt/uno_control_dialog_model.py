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
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing
from abc import abstractmethod
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
from ..container.x_container import XContainer as XContainer_d6fb0cc6
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..util.color import Color as Color_68e908c5

class UnoControlDialogModel(UnoControlModel_c8ce0c58, XContainer_d6fb0cc6, XNameContainer_cb90e47, XMultiServiceFactory_191e0eb6):
    """
    Service Class

    specifies the standard model of a UnoControlDialog.
    
    **since**
    
        OOo 2.3

    See Also:
        `API UnoControlDialogModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlDialogModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlDialogModel'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def BackgroundColor(self) -> Color_68e908c5:
        """
        specifies the background color (RGB) of the dialog.
        """
        ...

    @property
    @abstractmethod
    def Closeable(self) -> bool:
        """
        specifies if the dialog is closeable.
        """
        ...

    @property
    @abstractmethod
    def DesktopAsParent(self) -> bool:
        """
        If set to true the dialog will have the desktop as parent.
        
        **since**
        
            OOo 2.3
        """
        ...

    @property
    @abstractmethod
    def Enabled(self) -> bool:
        """
        determines whether a dialog is enabled or disabled.
        """
        ...

    @property
    @abstractmethod
    def FontDescriptor(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the caption bar of the dialog.
        """
        ...

    @property
    @abstractmethod
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the caption bar of the dialog.
        """
        ...

    @property
    @abstractmethod
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the caption bar of the dialog.
        """
        ...

    @property
    @abstractmethod
    def Graphic(self) -> XGraphic_a4da0afc:
        """
        specifies a graphic to be displayed as a background image
        
        If this property is present, it interacts with the ImageURL in the following way:
        
        **since**
        
            OOo 2.4
        """
        ...

    @property
    @abstractmethod
    def HScroll(self) -> bool:
        """
        specifies that a horizontal scrollbar should be added to the dialog
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @property
    @abstractmethod
    def HelpText(self) -> str:
        """
        specifies the help text of the dialog.
        """
        ...

    @property
    @abstractmethod
    def HelpURL(self) -> str:
        """
        specifies the help URL of the dialog.
        """
        ...

    @property
    @abstractmethod
    def ImageURL(self) -> str:
        """
        specifies a URL that references a graphic that should be used as a background image.
        
        **since**
        
            OOo 2.4
        """
        ...

    @property
    @abstractmethod
    def Moveable(self) -> bool:
        """
        specifies if the dialog is moveable.
        """
        ...

    @property
    @abstractmethod
    def ScrollHeight(self) -> int:
        """
        specifies the total height of the scrollable dialog content
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @property
    @abstractmethod
    def ScrollLeft(self) -> int:
        """
        specifies the horizontal position of the scrolled dialog content
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @property
    @abstractmethod
    def ScrollTop(self) -> int:
        """
        specifies the vertical position of the scrolled dialog content
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @property
    @abstractmethod
    def ScrollWidth(self) -> int:
        """
        specifies the total width of the scrollable dialog content
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @property
    @abstractmethod
    def Sizeable(self) -> bool:
        """
        specifies if the dialog is sizeable.
        """
        ...

    @property
    @abstractmethod
    def TextColor(self) -> Color_68e908c5:
        """
        specifies the text color (RGB) of the dialog.
        """
        ...

    @property
    @abstractmethod
    def TextLineColor(self) -> Color_68e908c5:
        """
        specifies the text line color (RGB) of the dialog.
        """
        ...

    @property
    @abstractmethod
    def Title(self) -> str:
        """
        specifies the text that is displayed in the caption bar of the dialog.
        """
        ...

    @property
    @abstractmethod
    def VScroll(self) -> bool:
        """
        specifies that a vertical scrollbar should be added to the dialog
        
        **since**
        
            LibreOffice 4.0
        """
        ...


__all__ = ['UnoControlDialogModel']

