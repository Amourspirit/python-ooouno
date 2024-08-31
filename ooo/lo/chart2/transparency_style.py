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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class TransparencyStyle(Enum):
    """
    Enum Class

    ENUM TransparencyStyle

    See Also:
        `API TransparencyStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#acc7ba74ba6531a134bb92607b8616cb6>`_
    """
    __ooo_ns__: str = "com.sun.star.chart2"
    __ooo_full_ns__: str = "com.sun.star.chart2.TransparencyStyle"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.chart2.TransparencyStyle"

    GRADIENT = "GRADIENT"
    """
    The property TransparencyGradient is evaluated, Transparency is ignored.
    """
    LINEAR = "LINEAR"
    """
    The property Transparency is evaluated, TransparencyGradient is ignored.
    """
    NONE = "NONE"
    """
    Default, no pies are exploded.
    
    no transparency attribute is evaluated
    
    The symbol is invisible.
    """

__all__ = ["TransparencyStyle"]

