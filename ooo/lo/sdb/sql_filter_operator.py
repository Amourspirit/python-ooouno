# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdb


class SQLFilterOperator(object):
    """
    Const Class

    These constants are used to specify the filter operator which should be applied when creating a filter with the method XSingleSelectQueryComposer.setStructuredFilter().

    See Also:
        `API SQLFilterOperator <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdb_1_1SQLFilterOperator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.SQLFilterOperator'
    __ooo_type_name__: str = 'const'

    EQUAL = 1
    """
    equal to
    """
    NOT_EQUAL = 2
    """
    not equal to
    """
    LESS = 3
    """
    less than
    """
    GREATER = 4
    """
    greater than
    """
    LESS_EQUAL = 5
    """
    less or equal than
    """
    GREATER_EQUAL = 6
    """
    greater or equal than
    """
    LIKE = 7
    """
    like
    """
    NOT_LIKE = 8
    """
    not like
    """
    SQLNULL = 9
    """
    is null
    """
    NOT_SQLNULL = 10
    """
    is not null
    """

__all__ = ['SQLFilterOperator']