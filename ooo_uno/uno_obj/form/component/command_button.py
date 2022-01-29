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
# Namespace: com.sun.star.form.component
import typing
from abc import abstractproperty
from ...awt.uno_control_button_model import UnoControlButtonModel as UnoControlButtonModel_1c000ed4
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ..x_image_producer_supplier import XImageProducerSupplier as XImageProducerSupplier_37df0f8f
from ..x_reset import XReset as XReset_71670917
if typing.TYPE_CHECKING:
    from ..form_button_type import FormButtonType as FormButtonType_c92d0c6e

class CommandButton(UnoControlButtonModel_1c000ed4, FormControlModel_e2990d22, XImageProducerSupplier_37df0f8f, XReset_71670917):
    """
    specifies the control model for a clickable button which is part of a form component hierarchy.

    See Also:
        `API CommandButton <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1CommandButton.html>`_
    """

    @abstractproperty
    def ButtonType(self) -> 'FormButtonType_c92d0c6e':
        """
        describes the action to be executed by the button when pressed.
        """
    @abstractproperty
    def DefaultState(self) -> bool:
        """
        specifies the default toggle state for the button, used when it is reset.
        
        This property is meaningful only when com.sun.star.awt.UnoControlButtonModel.Toggle is TRUE. In this case, the DefaultState controls to which State the button will be reset.
        
        For a given implementation of the interface, if this (optional) property is present, then also the optional interface com.sun.star.form.XReset must be present.
        """
    @abstractproperty
    def TargetFrame(self) -> str:
        """
        describes the frame, where to open the document specified by the TargetURL.
        
        This property is evaluated if the button is of type URL.
        
        As always, there is a number of target names which have a special meaning, and force a special com.sun.star.frame.Frame to be used.
        """
    @abstractproperty
    def TargetURL(self) -> str:
        """
        specifies the URL, which should be opened if the button was clicked.
        
        This property is evaluated if the button is of type URL.
        """

__all__ = ['CommandButton']

