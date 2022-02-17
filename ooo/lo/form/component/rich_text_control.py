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
from ...awt.uno_control_edit_model import UnoControlEditModel as UnoControlEditModel_fd8e0dde
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ...text.text_range import TextRange as TextRange_90540a5f

class RichTextControl(UnoControlEditModel_fd8e0dde, FormControlModel_e2990d22, TextRange_90540a5f):
    """
    Service Class

    specifies a component which extends the com.sun.star.awt.UnoControlEditModel with capabilities to display and input formatted text.

    See Also:
        `API RichTextControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1RichTextControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.RichTextControl'
    __ooo_type_name__: str = 'service'



__all__ = ['RichTextControl']

