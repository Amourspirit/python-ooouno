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


class TableOperationMode(Enum):
    """
    Enum Class


    See Also:
        `API TableOperationMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a91d4f5595c9dc2a8c09e532e59f395d9>`_
    """
    __ooo_ns__: str = "com.sun.star.sheet"
    __ooo_full_ns__: str = "com.sun.star.sheet.TableOperationMode"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.sheet.TableOperationMode"

    BOTH = "BOTH"
    """
    is applied to rows and columns.
    
    In this mode, the row and the column contain values. A formula using both row and column values is specified separately.
    """
    COLUMN = "COLUMN"
    """
    the field is used as a column field.
    
    is applied to the columns.
    
    In this mode, the column contains values and the row contains formulas.
    """
    ROW = "ROW"
    """
    the field is used as a row field.
    
    is applied to the rows.
    
    In this mode, the row contains values and the column contains formulas.
    """

__all__ = ["TableOperationMode"]

