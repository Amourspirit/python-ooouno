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
# Namespace: com.sun.star.form.control
from __future__ import annotations
from ...awt.uno_control_edit import UnoControlEdit as UnoControlEdit_bc4e0bed
from ..x_bound_control import XBoundControl as XBoundControl_bba00bed
from ..x_change_broadcaster import XChangeBroadcaster as XChangeBroadcaster_fabf0dc4

class TextField(UnoControlEdit_bc4e0bed, XBoundControl_bba00bed, XChangeBroadcaster_fabf0dc4):
    """
    Service Class

    describes a control for entering arbitrary text which can (but not necessarily has to) be bound to a database field.
    
    The model of the control has to support the com.sun.star.form.component.TextField service.
    
    In addition, this control can be used in HTML forms. It triggers the com.sun.star.form.XSubmit.submit() method of the form it belongs to if the enter is pressed while it has the focus.

    See Also:
        `API TextField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1control_1_1TextField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.control'
    __ooo_full_ns__: str = 'com.sun.star.form.control.TextField'
    __ooo_type_name__: str = 'service'


__all__ = ['TextField']

