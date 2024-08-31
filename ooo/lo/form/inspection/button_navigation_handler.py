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
# Namespace: com.sun.star.form.inspection
from __future__ import annotations
from ...inspection.x_property_handler import XPropertyHandler as XPropertyHandler_3e950fbf

class ButtonNavigationHandler(XPropertyHandler_3e950fbf):
    """
    Service Class

    implements a property handler for use with a com.sun.star.inspection.ObjectInspector which is able to enhance the com.sun.star.form.component.CommandButton.ButtonType and com.sun.star.form.component.CommandButton.TargetURL properties of a com.sun.star.form.component.CommandButton.
    
    For this, the two properties are superseded by new versions, where as button type, additional possible values are added for navigating the parent form of the button. For instance, in an com.sun.star.inspection.ObjectInspector using this handler, the user will be able to choose a button type saying \"move to the next record\", which, when chosen, well, moves the parent database form of the button to the next record.

    See Also:
        `API ButtonNavigationHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1inspection_1_1ButtonNavigationHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.inspection'
    __ooo_full_ns__: str = 'com.sun.star.form.inspection.ButtonNavigationHandler'
    __ooo_type_name__: str = 'service'


__all__ = ['ButtonNavigationHandler']

