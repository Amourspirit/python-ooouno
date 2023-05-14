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
# Namespace: com.sun.star.form.component
from abc import abstractproperty
from ...awt.uno_control_radio_button_model import UnoControlRadioButtonModel as UnoControlRadioButtonModel_6ad310c3
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ..x_reset import XReset as XReset_71670917

class RadioButton(UnoControlRadioButtonModel_6ad310c3, FormControlModel_e2990d22, XReset_71670917):
    """
    Service Class

    specifies a component which acts as a radio button as needed in HTMLForms.
    
    Radio buttons are controls which can be grouped together, and in every group, only one of the controls can be check. This means if one of them is checked by a user interaction, all other controls in the same group are automatically unchecked
    
    Like in HTML, radio buttons are grouped together if and only if they have the same name (see com.sun.star.form.FormComponent.Name).

    See Also:
        `API RadioButton <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1RadioButton.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.RadioButton'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DefaultState(self) -> int:
        """
        contains a default value for the control.
        
        This value is used when the control is initially displayed, and for resetting it.
        
        In a group of radio buttons only one button should be checked by default.
        """
        ...

    @abstractproperty
    def RefValue(self) -> str:
        """
        contains a reference value which is used for submission in a HTML form.
        
        If the form the control belongs to is to be submitted (see com.sun.star.form.XSubmit), and the control is checked, this reference value is used for submission.
        """
        ...

    @abstractproperty
    def UncheckedRefValue(self) -> str:
        """
        specifies a value which is to be associated with the control when it's not selected.
        
        In various situations, the RefValue is associated with the control if and only if it is selected.UncheckedRefValue provides an extension of this concept: If present, the value should be associated with the control when it is not selected.
        """
        ...


__all__ = ['RadioButton']

