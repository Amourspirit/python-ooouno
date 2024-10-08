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
# Namespace: com.sun.star.form.control
from __future__ import annotations
from ...awt.uno_control_combo_box import UnoControlComboBox as UnoControlComboBox_efd50d80
from ..x_bound_control import XBoundControl as XBoundControl_bba00bed

class ComboBox(UnoControlComboBox_efd50d80, XBoundControl_bba00bed):
    """
    Service Class

    describes a combo box control.
    
    The model of the control has to support the com.sun.star.form.component.ComboBox service.

    See Also:
        `API ComboBox <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1control_1_1ComboBox.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.control'
    __ooo_full_ns__: str = 'com.sun.star.form.control.ComboBox'
    __ooo_type_name__: str = 'service'


__all__ = ['ComboBox']

