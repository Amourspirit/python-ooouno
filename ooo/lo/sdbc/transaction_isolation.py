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
# Namespace: com.sun.star.sdbc


class TransactionIsolation(object):
    """
    Const Class

    distinguishes different possible transaction isolation levels.

    See Also:
        `API TransactionIsolation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1TransactionIsolation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.TransactionIsolation'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    indicates that transactions are not supported.
    """
    READ_UNCOMMITTED = 1
    """
    Dirty reads, non-repeatable reads and phantom reads can occur.
    
    This level allows a row changed by one transaction to be read by another transaction before any changes in that row have been committed (a \"dirty read\"). If any of the changes are rolled back, the second transaction will have retrieved an invalid row.
    """
    READ_COMMITTED = 2
    """
    Dirty reads are prevented; non-repeatable reads and phantom reads can occur.
    
    This level only prohibits a transaction from reading a row with uncommitted changes in it.
    """
    REPEATABLE_READ = 4
    """
    Dirty reads and non-repeatable reads are prevented; phantom reads can occur.
    
    This level prohibits a transaction from reading a row with uncommitted changes in it, and it also prohibits the situation where one transaction reads a row, a second transaction alters the row, and the first transaction rereads the row, getting different values the second time (a \"non-repeatable read\").
    """
    SERIALIZABLE = 8
    """
    Dirty reads, non-repeatable reads and phantom reads are prevented.
    
    This level includes the prohibitions in REPEATABLE_READ and further prohibits the situation where one transaction reads all rows that satisfy a WHERE condition, a second transaction inserts a row that satisfies that WHERE condition, and the first transaction rereads for the same condition, retrieving the additional \"phantom\" row in the second read.
    """

__all__ = ['TransactionIsolation']
