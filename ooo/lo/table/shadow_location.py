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
# Namespace: com.sun.star.table
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class ShadowLocation(Enum):
    """
    Enum Class


    See Also:
        `API ShadowLocation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1table.html#a9ab4ece6abe8ce0c4ad3123d6e3916c0>`_
    """
    __ooo_ns__: str = "com.sun.star.table"
    __ooo_full_ns__: str = "com.sun.star.table.ShadowLocation"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.table.ShadowLocation"

    BOTTOM_LEFT = "BOTTOM_LEFT"
    """
    shadow is located along the lower and left sides.
    """
    BOTTOM_RIGHT = "BOTTOM_RIGHT"
    """
    shadow is located along the lower and right sides.
    """
    NONE = "NONE"
    """
    no shadow.
    """
    TOP_LEFT = "TOP_LEFT"
    """
    shadow is located along the upper and left sides.
    """
    TOP_RIGHT = "TOP_RIGHT"
    """
    shadow is located along the upper and right sides.
    """

__all__ = ["ShadowLocation"]

