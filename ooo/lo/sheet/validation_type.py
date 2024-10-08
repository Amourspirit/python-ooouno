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
# Namespace: com.sun.star.sheet
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class ValidationType(Enum):
    """
    Enum Class


    See Also:
        `API ValidationType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#aa5aa6dbecaeb5e18a476b0a58279c57a>`_
    """
    __ooo_ns__: str = "com.sun.star.sheet"
    __ooo_full_ns__: str = "com.sun.star.sheet.ValidationType"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.sheet.ValidationType"

    ANY = "ANY"
    """
    any cell content is valid; no conditions are used.
    """
    CUSTOM = "CUSTOM"
    """
    The specified formula determines which contents are valid.
    """
    DATE = "DATE"
    """
    specifies an arithmetic series for date values.
    
    any date value matching the specified condition is valid.
    
    Cell by cell, the value used to fill the cells is increased by a specified number of days
    """
    DECIMAL = "DECIMAL"
    """
    any number matching the specified condition is valid.
    """
    LIST = "LIST"
    """
    Only strings from a specified list are valid.
    """
    TEXT_LEN = "TEXT_LEN"
    """
    string is valid if its length matches the specified condition.
    """
    TIME = "TIME"
    """
    any time value matching the specified condition is valid.
    """
    WHOLE = "WHOLE"
    """
    any whole number matching the specified condition is valid.
    """

__all__ = ["ValidationType"]

