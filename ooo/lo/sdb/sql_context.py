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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.2
from ..sdbc.sql_warning import SQLWarning as SQLWarning_96f10a6a

class SQLContext(SQLWarning_96f10a6a):
    """
    provides special information about the context where a com.sun.star.sdbc.SQLException occurred.
    
    As usual for SQLExceptions, several SQLContext-objects may be chained, then the most recent context is appended to the list's tail.

    See Also:
        `API SQLContext <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdb_1_1SQLContext.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.SQLContext'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.sdb.SQLContext'
    __pyunostruct__: str = 'com.sun.star.sdb.SQLContext'

    typeName: str = 'com.sun.star.sdb.SQLContext'
    """Literal Constant ``com.sun.star.sdb.SQLContext``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)



