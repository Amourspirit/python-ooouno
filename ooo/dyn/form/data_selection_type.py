# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.form.DataSelectionType import QUERY as DATA_SELECTION_TYPE_QUERY
    from com.sun.star.form.DataSelectionType import SQL as DATA_SELECTION_TYPE_SQL
    from com.sun.star.form.DataSelectionType import SQLPASSTHROUGH as DATA_SELECTION_TYPE_SQLPASSTHROUGH
    from com.sun.star.form.DataSelectionType import TABLE as DATA_SELECTION_TYPE_TABLE

    class DataSelectionType(uno.Enum):
        """
        Enum Class


        See Also:
            `API DataSelectionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#abce772d425e368c8a4f81abe7afa7279>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.form.DataSelectionType', value)

        __ooo_ns__: str = 'com.sun.star.form'
        __ooo_full_ns__: str = 'com.sun.star.form.DataSelectionType'
        __ooo_type_name__: str = 'enum'

        QUERY: DataSelectionType = DATA_SELECTION_TYPE_QUERY
        """
        The control should be filled with the results of a database query.
        """
        SQL: DataSelectionType = DATA_SELECTION_TYPE_SQL
        """
        The control should be filled with the results of a database statement.
        """
        SQLPASSTHROUGH: DataSelectionType = DATA_SELECTION_TYPE_SQLPASSTHROUGH
        """
        The control should be filled with the results of a database statement, which is not evaluated by the database engine.
        """
        TABLE: DataSelectionType = DATA_SELECTION_TYPE_TABLE
        """
        The control should be filled with the data of a table.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class DataSelectionType(metaclass=UnoEnumMeta, type_name="com.sun.star.form.DataSelectionType", name_space="com.sun.star.form"):
        """Dynamically created class that represents ``com.sun.star.form.DataSelectionType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['DataSelectionType']
