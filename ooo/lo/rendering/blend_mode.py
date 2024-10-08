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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.rendering


class BlendMode(object):
    """
    Const Class

    These constants determine some extra ways how the primitive color is combined with the background.
    
    Please refer to the PDF specification for explanations of this constants.

    See Also:
        `API BlendMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1BlendMode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.BlendMode'
    __ooo_type_name__: str = 'const'

    NORMAL = 0
    MULTIPLY = 1
    SCREEN = 2
    OVERLAY = 3
    DARKEN = 4
    LIGHTEN = 5
    COLOR_DODGE = 6
    COLOR_BURN = 7
    HARD_LIGHT = 8
    SOFT_LIGHT = 9
    DIFFERENCE = 10
    EXCLUSION = 11
    HUE = 12
    SATURATION = 13
    COLOR = 14
    LUMINOSITY = 15

__all__ = ['BlendMode']
