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

class XSDValidationPropertyHandler(XPropertyHandler_3e950fbf):
    """
    Service Class

    implements a property handler for use with a com.sun.star.inspection.ObjectInspector which provides properties related to binding form control models to XForm bindings and validating the form control content.
    
    By using an XMLFormsPropertyHandler, a com.sun.star.inspection.ObjectInspector can be used to bind form components to com.sun.star.xforms.Binding instances. Since those instances also support validating form control content (by supporting an com.sun.star.form.validation.XValidator interface), it seems reasonable to edit those validate-related properties (like the XSD data type to validate against) in the com.sun.star.inspection.ObjectInspector, too. This is what an XSDValidationPropertyHandler is good for.
    
    The handler expects a value named \"ContextDocument\" in the context in which it is created. That is, the com.sun.star.uno.XComponentContext used for creating the CellBindingPropertyHandler is examined for a value with this name. If the object in this value denotes a XML form document (indicated by supporting the com.sun.star.xforms.XFormsSupplier interface), this document is used to do XML binding related work.

    See Also:
        `API XSDValidationPropertyHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1inspection_1_1XSDValidationPropertyHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.inspection'
    __ooo_full_ns__: str = 'com.sun.star.form.inspection.XSDValidationPropertyHandler'
    __ooo_type_name__: str = 'service'


__all__ = ['XSDValidationPropertyHandler']

