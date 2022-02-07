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
# Namespace: com.sun.star.form.control
from ...awt.uno_control_time_field import UnoControlTimeField as UnoControlTimeField_fdcd0dda
from ..x_bound_control import XBoundControl as XBoundControl_bba00bed

class TimeField(UnoControlTimeField_fdcd0dda, XBoundControl_bba00bed):
    """
    Service Class

    describes a control for inputting time values which can (but not necessarily has to) be bound to a database field.
    
    The model of the control has to support the com.sun.star.form.component.TimeField service.

    See Also:
        `API TimeField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1control_1_1TimeField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.control'
    __ooo_full_ns__: str = 'com.sun.star.form.control.TimeField'
    __ooo_type_name__: str = 'service'


__all__ = ['TimeField']

