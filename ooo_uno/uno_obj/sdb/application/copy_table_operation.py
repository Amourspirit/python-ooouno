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
from ooo_uno.base.const import ConstIntBase


class CopyTableOperation(ConstIntBase):
    """
    specifies the different basic operations a CopyTableWizard can do.
    
    **since**
    
        OOo 2.4

    See Also:
        `API CopyTableOperation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdb_1_1application_1_1CopyTableOperation.html>`_
    """
    CopyDefinitionAndData = 0
    """
    specifies that the wizard should copy the source table to the target database, by creating a new table and copying all data.
    """
    CopyDefinitionOnly = 1
    """
    specifies that the wizard should copy the source table to the target database, by only creating a new table with the same structure as the source table.
    """
    CreateAsView = 2
    """
    specifies the wizard should create the source table as view
    
    This option is not available if the target database does not support views.
    """
    AppendData = 3
    """
    specifies the wizard should append the source table's data to an existing table in the target database.
    """

