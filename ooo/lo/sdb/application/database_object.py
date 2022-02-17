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
# Namespace: com.sun.star.sdb.application
from ..command_type import CommandType


class DatabaseObject(object):
    """
    Const Class

    denotes different objects within a database document
    
    **since**
    
        OOo 2.2

    See Also:
        `API DatabaseObject <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdb_1_1application_1_1DatabaseObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.application'
    __ooo_full_ns__: str = 'com.sun.star.sdb.application.DatabaseObject'
    __ooo_type_name__: str = 'const'

    TABLE = CommandType.TABLE
    """
    denotes a table in a database
    
    Note that table here is a more general term. In OpenOffice.org Base, views are also represented as tables, since to the user, the behave pretty much as tables do.
    """
    QUERY = CommandType.QUERY
    """
    denotes a query in a database document
    """
    FORM = 2
    """
    denotes a form in a database document
    """
    REPORT = 3
    """
    denotes a report in a database document
    """

__all__ = ['DatabaseObject']