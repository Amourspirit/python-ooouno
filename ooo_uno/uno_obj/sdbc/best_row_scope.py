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
from ooo_uno.base.const import ConstIntBase


class BestRowScope(ConstIntBase):
    """
    determines how long a row identifier is valid.

    See Also:
        `API BestRowScope <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1BestRowScope.html>`_
    """
    TEMPORARY = 0
    """
    indicates that the scope of the best row identifier is very temporary, lasting only while the row is being used.
    
    A possible value for the column SCOPE in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
    """
    TRANSACTION = 1
    """
    indicates that the scope of the best row identifier is the remainder of the current transaction.
    
    A possible value for the column SCOPE in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
    """
    SESSION = 2
    """
    indicates that the scope of the best row identifier is the remainder of the current session.
    
    A possible value for the column SCOPE in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
    """

