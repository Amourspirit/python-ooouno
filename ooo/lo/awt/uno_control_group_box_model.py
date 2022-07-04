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
# Namespace: com.sun.star.awt
import typing
from abc import abstractproperty
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..util.color import Color as Color_68e908c5

class UnoControlGroupBoxModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlGroupBox.
    
    **since**
    
        OOo 3.1

    See Also:
        `API UnoControlGroupBoxModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlGroupBoxModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlGroupBoxModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...

    @abstractproperty
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """
        ...

    @abstractproperty
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...

    @abstractproperty
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...

    @abstractproperty
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...

    @abstractproperty
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...

    @abstractproperty
    def Label(self) -> str:
        """
        specifies the label of the control.
        """
        ...

    @abstractproperty
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
        ...

    @abstractproperty
    def TextColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """
        ...

    @abstractproperty
    def TextLineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """
        ...

    @abstractproperty
    def WritingMode(self) -> int:
        """
        denotes the writing mode used in the control, as specified in the com.sun.star.text.WritingMode2 constants group.
        
        Only com.sun.star.text.WritingMode2.LR_TB and com.sun.star.text.WritingMode2.RL_TB are supported at the moment.
        
        **since**
        
            OOo 3.1
        """
        ...



__all__ = ['UnoControlGroupBoxModel']

