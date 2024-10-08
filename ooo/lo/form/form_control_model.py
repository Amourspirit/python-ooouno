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
# Namespace: com.sun.star.form
from __future__ import annotations
from abc import abstractmethod
from ..awt.uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
from ..beans.x_fast_property_set import XFastPropertySet as XFastPropertySet_ee6b0d88
from ..beans.x_property_state import XPropertyState as XPropertyState_d55c0ccf
from .form_component import FormComponent as FormComponent_bc700c03

class FormControlModel(UnoControlModel_c8ce0c58, FormComponent_bc700c03, XFastPropertySet_ee6b0d88, XPropertyState_d55c0ccf):
    """
    Service Class

    specifies a control model within a form.
    
    Note that the model-view-paradigm is used for form controls, too.

    See Also:
        `API FormControlModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1FormControlModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.FormControlModel'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def ClassId(self) -> int:
        """
        specifies the ID for classification of the component.
        """
        ...

    @property
    @abstractmethod
    def TabIndex(self) -> int:
        """
        determines the relative taborder of the control associated with the model.
        
        The default -1 is used to indicate that the tab-order of this control should be determined automatically.
        
        Each component which supports a tabstop must provide a FormControlModel.TabIndex property.
        
        Normally, a FormController instance is evaluating this property.
        """
        ...

    @property
    @abstractmethod
    def Tag(self) -> str:
        """
        used for additional information.
        
        No semantics is given for this property, it will usually be used by the creator of a document containing form controls.
        """
        ...


__all__ = ['FormControlModel']

