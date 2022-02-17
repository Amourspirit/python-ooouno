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
# Namespace: com.sun.star.drawing
from .connector_properties import ConnectorProperties as ConnectorProperties_3c5e0fcc
from .fill_properties import FillProperties as FillProperties_f1200da8
from .line_properties import LineProperties as LineProperties_f13f0da9
from .measure_properties import MeasureProperties as MeasureProperties_1d340ef3
from .shadow_properties import ShadowProperties as ShadowProperties_e350e87
from .text_properties import TextProperties as TextProperties_f2980dc6

class Defaults(ConnectorProperties_3c5e0fcc, FillProperties_f1200da8, LineProperties_f13f0da9, MeasureProperties_1d340ef3, ShadowProperties_e350e87, TextProperties_f2980dc6):
    """
    Service Class

    This is a set of properties to access the defaults of a drawing document.

    See Also:
        `API Defaults <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1Defaults.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.Defaults'
    __ooo_type_name__: str = 'service'



__all__ = ['Defaults']
