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


class HatchStyle(Enum):
    """
    Enum Class


    See Also:
        `API HatchStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a021284aa8478781ba1b958b81da7b608>`_
    """
    __ooo_ns__: str = "com.sun.star.drawing"
    __ooo_full_ns__: str = "com.sun.star.drawing.HatchStyle"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.drawing.HatchStyle"

    DOUBLE = "DOUBLE"
    """
    the hatch has a horizontal and a vertical line
    """
    SINGLE = "SINGLE"
    """
    the hatch consists of a single horizontal line
    """
    TRIPLE = "TRIPLE"
    """
    the hatch has a horizontal, a vertical and a diagonal line
    """

__all__ = ["HatchStyle"]

