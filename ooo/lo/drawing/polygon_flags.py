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
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class PolygonFlags(Enum):
    """
    Enum Class


    See Also:
        `API PolygonFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#af3965fa427851bc02bfe32c5d95d7406>`_
    """
    __ooo_ns__: str = "com.sun.star.drawing"
    __ooo_full_ns__: str = "com.sun.star.drawing.PolygonFlags"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.drawing.PolygonFlags"

    CONTROL = "CONTROL"
    """
    the point is a control point, to control the curve from the user interface.
    """
    NORMAL = "NORMAL"
    """
    the text is drawn along the path without scaling.
    
    the point is normal, from the curve discussion view.
    """
    SMOOTH = "SMOOTH"
    """
    the point is smooth, the first derivation from the curve discussion view.
    
    With SMOOTH shading, the colors of the lit vertices is interpolated.
    """
    SYMMETRIC = "SYMMETRIC"
    """
    the point is symmetric, the second derivation from the curve discussion view.
    """

__all__ = ["PolygonFlags"]

