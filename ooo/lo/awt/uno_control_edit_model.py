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
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.style.VerticalAlignment import VerticalAlignmentProto  # type: ignore

class UnoControlEditModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlEdit.
    
    **since**
    
        OOo 2.3

    See Also:
        `API UnoControlEditModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlEditModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlEditModel'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def Align(self) -> int:
        """
        specifies the horizontal alignment of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def AutoHScroll(self) -> bool:
        """
        If set to true an horizontal scrollbar will be added automatically when needed.
        
        **since**
        
            OOo 2.3
        """
        ...

    @property
    @abstractmethod
    def AutoVScroll(self) -> bool:
        """
        If set to true a vertical scrollbar will be added automatically when needed.
        
        **since**
        
            OOo 2.3
        """
        ...

    @property
    @abstractmethod
    def BackgroundColor(self) -> Color_68e908c5:
        """
        specifies the background color (RGB) of the control.
        """
        ...

    @property
    @abstractmethod
    def Border(self) -> int:
        """
        specifies the border style of the control.
        """
        ...

    @property
    @abstractmethod
    def BorderColor(self) -> int:
        """
        specifies the color of the border, if present
        
        Not every border style (see Border) may support coloring. For instance, usually a border with 3D effect will ignore the BorderColor setting.
        
        **since**
        
            OOo 2.0
        """
        ...

    @property
    @abstractmethod
    def EchoChar(self) -> int:
        """
        specifies the echo character for a password edit field.
        """
        ...

    @property
    @abstractmethod
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...

    @property
    @abstractmethod
    def FontDescriptor(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...

    @property
    @abstractmethod
    def HScroll(self) -> bool:
        """
        specifies if the content of the control can be scrolled in the horizontal direction.
        """
        ...

    @property
    @abstractmethod
    def HardLineBreaks(self) -> bool:
        """
        specifies if hard line breaks will be returned in the XTextComponent.getText() method.
        """
        ...

    @property
    @abstractmethod
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...

    @property
    @abstractmethod
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...

    @property
    @abstractmethod
    def HideInactiveSelection(self) -> bool:
        """
        specifies whether the selection in the control should be hidden when the control is not active (focused).
        
        **since**
        
            OOo 2.0
        """
        ...

    @property
    @abstractmethod
    def HighlightColor(self) -> Color_68e908c5:
        """
        specifies the background color (RGB) of selected text in the control which is highlighted.
        
        **since**
        
            LibreOffice 7.5
        """
        ...

    @property
    @abstractmethod
    def HighlightTextColor(self) -> Color_68e908c5:
        """
        specifies the text color (RGB) of selected text in the control which is highlighted.
        
        **since**
        
            LibreOffice 7.5
        """
        ...

    @property
    @abstractmethod
    def LineEndFormat(self) -> int:
        """
        specifies which line end type should be used for multi line text
        
        Controls working with this model care for this setting when the user enters text. Every line break entered into the control will be treated according to this setting, so that the Text property always contains only line ends in the format specified.
        
        Possible values are all constants from the LineEndFormat group.
        
        Note that this setting is usually not relevant when you set new text via the API. No matter which line end format is used in this new text then, usual control implementations should recognize all line end formats and display them properly.
        
        **since**
        
            OOo 2.0
        """
        ...

    @property
    @abstractmethod
    def MaxTextLen(self) -> int:
        """
        specifies the maximum character count.
        
        There's no limitation, if set to 0.
        """
        ...

    @property
    @abstractmethod
    def MultiLine(self) -> bool:
        """
        specifies that the control may have more than one line.
        """
        ...

    @property
    @abstractmethod
    def PaintTransparent(self) -> bool:
        """
        specifies whether the control paints it background or not.
        
        **since**
        
            OOo 2.3
        """
        ...

    @property
    @abstractmethod
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
        ...

    @property
    @abstractmethod
    def ReadOnly(self) -> bool:
        """
        specifies that the content of the control cannot be modified by the user.
        """
        ...

    @property
    @abstractmethod
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        """
        ...

    @property
    @abstractmethod
    def Text(self) -> str:
        """
        specifies the text displayed in the control.
        """
        ...

    @property
    @abstractmethod
    def TextColor(self) -> Color_68e908c5:
        """
        specifies the text color (RGB) of the control.
        """
        ...

    @property
    @abstractmethod
    def TextLineColor(self) -> Color_68e908c5:
        """
        specifies the text line color (RGB) of the control.
        """
        ...

    @property
    @abstractmethod
    def VScroll(self) -> bool:
        """
        specifies if the content of the control can be scrolled in the vertical direction.
        """
        ...

    @property
    @abstractmethod
    def VerticalAlign(self) -> VerticalAlignmentProto:
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 3.3
        """
        ...

    @property
    @abstractmethod
    def WritingMode(self) -> int:
        """
        denotes the writing mode used in the control, as specified in the com.sun.star.text.WritingMode2 constants group.
        
        Only com.sun.star.text.WritingMode2.LR_TB and com.sun.star.text.WritingMode2.RL_TB are supported at the moment.
        
        **since**
        
            OOo 3.1
        """
        ...


__all__ = ['UnoControlEditModel']