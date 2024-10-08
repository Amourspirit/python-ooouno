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

class EditPropertyHandler(XPropertyHandler_3e950fbf):
    """
    Service Class

    implements a property handler for use with a com.sun.star.inspection.ObjectInspector which provides convenience wrappers for some properties existing at a form component derived from com.sun.star.awt.UnoControlEditModel.
    
    First, the handler supersedes the HScroll and the VScroll properties of a com.sun.star.awt.UnoControlEditModel and puts them into one common property, allowing the user to choose whether she want to have \"no\", a \"vertical\", a \"horizontal\", or \"both\" scrollbars.
    
    Second, if it detects a com.sun.star.form.component.RichTextControl to inspect, it supersedes the com.sun.star.form.component.RichTextControl.RichText and the com.sun.star.awt.UnoControlEditModel.MultiLine properties with a new one which allows choosing the text type with one single action.

    See Also:
        `API EditPropertyHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1inspection_1_1EditPropertyHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.inspection'
    __ooo_full_ns__: str = 'com.sun.star.form.inspection.EditPropertyHandler'
    __ooo_type_name__: str = 'service'


__all__ = ['EditPropertyHandler']

