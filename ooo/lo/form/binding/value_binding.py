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
# Namespace: com.sun.star.form.binding
from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_value_binding import XValueBinding as XValueBinding_271b0ed5
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from ...util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0

class ValueBinding(XPropertySet_bc180bfa, XValueBinding_271b0ed5, XComponent_98dc0ab5, XModifyBroadcaster_fd990df0):
    """
    Service Class

    defines a component which allows access to a single value
    
    Read/Write access to the value represented by this component is supported, as well as (optionally) active broadcasting of value changes

    See Also:
        `API ValueBinding <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1binding_1_1ValueBinding.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.binding'
    __ooo_full_ns__: str = 'com.sun.star.form.binding.ValueBinding'
    __ooo_type_name__: str = 'service'



__all__ = ['ValueBinding']

