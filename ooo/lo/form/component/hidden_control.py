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
from ..form_component import FormComponent as FormComponent_bc700c03

class HiddenControl(FormComponent_bc700c03):
    """
    Service Class

    This service specifies the model of a hidden control.
    
    The only sense of a hidden control is to store data in the form which is not visible to the user.
    
    Usually, hidden controls are used in com.sun.star.form.component.HTMLForms, where they contain data which is to be submitted.
    Nevertheless, you can use them in your own forms for storing any data, for instance to evaluate it in some scripting macro.

    See Also:
        `API HiddenControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1HiddenControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.HiddenControl'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def HiddenValue(self) -> str:
        """
        specifies the value of the component.
        """

__all__ = ['HiddenControl']

