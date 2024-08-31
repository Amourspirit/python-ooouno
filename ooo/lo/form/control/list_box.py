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
from ...awt.uno_control_list_box import UnoControlListBox as UnoControlListBox_e2b20d2c
from ..x_bound_control import XBoundControl as XBoundControl_bba00bed
from ..x_change_broadcaster import XChangeBroadcaster as XChangeBroadcaster_fabf0dc4

class ListBox(UnoControlListBox_e2b20d2c, XBoundControl_bba00bed, XChangeBroadcaster_fabf0dc4):
    """
    Service Class

    describes a list box control which can (but not necessarily has to) be bound to a database field.
    
    The model of the control has to support the com.sun.star.form.component.ListBox service.

    See Also:
        `API ListBox <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1control_1_1ListBox.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.control'
    __ooo_full_ns__: str = 'com.sun.star.form.control.ListBox'
    __ooo_type_name__: str = 'service'


__all__ = ['ListBox']

