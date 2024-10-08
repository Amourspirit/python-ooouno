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


class ConditionOperator2(object):
    """
    Const Class

    is used to specify the type of XSheetCondition2.

    See Also:
        `API ConditionOperator2 <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1ConditionOperator2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.ConditionOperator2'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    no condition is specified.
    """
    EQUAL = 1
    """
    value has to be equal to the specified value.
    """
    NOT_EQUAL = 2
    """
    the value must not be equal to the specified value.
    """
    GREATER = 3
    """
    the value has to be greater than the specified value.
    """
    GREATER_EQUAL = 4
    """
    the value has to be greater than or equal to the specified value.
    """
    LESS = 5
    """
    the value has to be less than the specified value.
    """
    LESS_EQUAL = 6
    """
    the value has to be less than or equal to the specified value.
    """
    BETWEEN = 7
    """
    the value has to be between the two specified values.
    """
    NOT_BETWEEN = 8
    """
    the value has to be outside of the two specified values.
    """
    FORMULA = 9
    """
    the specified formula has to give a non-zero result.
    """
    DUPLICATE = 10
    """
    Conditionally format duplicate values.
    """
    NOT_DUPLICATE = 11
    """
    Conditionally format non-duplicate values.
    """

__all__ = ['ConditionOperator2']
