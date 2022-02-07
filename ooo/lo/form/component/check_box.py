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
from abc import abstractproperty
from ...awt.uno_control_check_box_model import UnoControlCheckBoxModel as UnoControlCheckBoxModel_383d0f5f
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ..x_reset import XReset as XReset_71670917

class CheckBox(UnoControlCheckBoxModel_383d0f5f, FormControlModel_e2990d22, XReset_71670917):
    """
    Service Class

    specifies the model of a check box control
    
    The model supports the properties required for HTML, thus you can build up HTMLForms with it

    See Also:
        `API CheckBox <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1CheckBox.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.CheckBox'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DefaultState(self) -> int:
        """
        contains a default value for the control.
        
        This value is used when the control is initially displayed, and for resetting it.
        """
    @abstractproperty
    def RefValue(self) -> str:
        """
        contains a reference value which is used for submission in a HTML form
        
        When submitting a HTMLForm which contains a check box, which is checked, the RefValue is used for submission.
        """

__all__ = ['CheckBox']

