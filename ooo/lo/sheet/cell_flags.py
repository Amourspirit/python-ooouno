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
# Namespace: com.sun.star.sheet


class CellFlags(object):
    """
    Const Class

    These constants select different types of cell contents.
    
    The values can be combined. They are used to insert, copy, or delete contents.

    See Also:
        `API CellFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1CellFlags.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.CellFlags'
    __ooo_type_name__: str = 'const'

    VALUE = 1
    """
    selects constant numeric values that are not formatted as dates or times.
    """
    DATETIME = 2
    """
    selects constant numeric values that have a date or time number format.
    """
    STRING = 4
    """
    selects constant strings.
    """
    ANNOTATION = 8
    """
    selects cell annotations.
    """
    FORMULA = 16
    """
    selects formulas.
    """
    HARDATTR = 32
    """
    selects all explicit formatting, but not the formatting which is applied implicitly through style sheets.
    """
    STYLES = 64
    """
    selects cell styles.
    """
    OBJECTS = 128
    """
    selects drawing objects.
    """
    EDITATTR = 256
    """
    selects formatting within parts of the cell contents.
    """
    FORMATTED = 512
    """
    selects cells with formatting within the cells or cells with more than one paragraph within the cells.
    """

__all__ = ['CellFlags']
