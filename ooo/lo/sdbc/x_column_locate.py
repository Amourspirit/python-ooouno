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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbc
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XColumnLocate(XInterface_8f010a43):
    """
    provides the possibility to find columns by their name.
    
    When several columns have the same name, then the value of the first matching column will be returned. The column name option is designed to be used when column names are used in the SQL query. For columns that are NOT explicitly named in the query, it is best to use column numbers. If column names are used, there is no way for the programmer to guarantee that they actually refer to the intended columns.

    See Also:
        `API XColumnLocate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XColumnLocate.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XColumnLocate'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XColumnLocate'

    @abstractmethod
    def findColumn(self, columnName: str) -> int:
        """
        maps the given ResultSet column name to its ResultSet column index.
        
        The specification before LibreOffice 4.2 left unspecified what should happen for an invalid column name. As a result some drivers written against the older specification may return a special invalid value, such as a negative number, zero, or a number greater than the number of columns.

        Raises:
            SQLException: ``SQLException``
        """


__all__ = ['XColumnLocate']

