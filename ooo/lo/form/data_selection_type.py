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
# Namespace: com.sun.star.form
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class DataSelectionType(Enum):
    """
    Enum Class


    See Also:
        `API DataSelectionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#abce772d425e368c8a4f81abe7afa7279>`_
    """
    __ooo_ns__: str = "com.sun.star.form"
    __ooo_full_ns__: str = "com.sun.star.form.DataSelectionType"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.form.DataSelectionType"

    QUERY = "QUERY"
    """
    The control should be filled with the results of a database query.
    """
    SQL = "SQL"
    """
    The control should be filled with the results of a database statement.
    """
    SQLPASSTHROUGH = "SQLPASSTHROUGH"
    """
    The control should be filled with the results of a database statement, which is not evaluated by the database engine.
    """
    TABLE = "TABLE"
    """
    The control should be filled with the data of a table.
    """

__all__ = ["DataSelectionType"]

