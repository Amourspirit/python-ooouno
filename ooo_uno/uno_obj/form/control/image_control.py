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
from ...awt.uno_control_image_control import UnoControlImageControl as UnoControlImageControl_29c00f2b
from ..x_bound_control import XBoundControl as XBoundControl_bba00bed

class ImageControl(UnoControlImageControl_29c00f2b, XBoundControl_bba00bed):
    """
    describes a control used for displaying images stored in a database.
    
    The model of the control has to support the com.sun.star.form.component.DatabaseImageControl service.
    
    If the model of the control is valid bound to a database field, the control allows to select an image (browsing the file system) upon double clicking into it, and forwards the URL of the chosen image to the ImageURL property of its model.

    See Also:
        `API ImageControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1control_1_1ImageControl.html>`_
    """


__all__ = ['ImageControl']

