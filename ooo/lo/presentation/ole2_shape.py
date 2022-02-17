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
# Namespace: com.sun.star.presentation
from ..drawing.ole2_shape import OLE2Shape as OLE2Shape_add20af7
from .shape import Shape as Shape_c0c80c15

class OLE2Shape(OLE2Shape_add20af7, Shape_c0c80c15):
    """
    Service Class

    This service is implemented by the OLE2 presentation shape.
    
    Presentation shapes can be used in a presentation page layouts and their position and size is by default set by the presentation shapes on the com.sun.star.drawing.MasterPage.

    See Also:
        `API OLE2Shape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1presentation_1_1OLE2Shape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.OLE2Shape'
    __ooo_type_name__: str = 'service'



__all__ = ['OLE2Shape']
