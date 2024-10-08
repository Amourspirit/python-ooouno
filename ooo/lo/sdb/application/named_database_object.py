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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sdb.application
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class NamedDatabaseObject(object):
    """
    Struct Class

    denotes a named database object, or a named folder of database objects
    
    **since**
    
        OOo 3.0

    See Also:
        `API NamedDatabaseObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1application_1_1NamedDatabaseObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.application'
    __ooo_full_ns__: str = 'com.sun.star.sdb.application.NamedDatabaseObject'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sdb.application.NamedDatabaseObject'
    """Literal Constant ``com.sun.star.sdb.application.NamedDatabaseObject``"""

    def __init__(self, Type: typing.Optional[int] = 0, Name: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Type (int, optional): Type value.
            Name (str, optional): Name value.
        """
        super().__init__()

        if isinstance(Type, NamedDatabaseObject):
            oth: NamedDatabaseObject = Type
            self.Type = oth.Type
            self.Name = oth.Name
            return

        kargs = {
            "Type": Type,
            "Name": Name,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._type = kwargs["Type"]
        self._name = kwargs["Name"]


    @property
    def Type(self) -> int:
        """
        denotes the type of the object.
        
        This member is one of the DatabaseObject or DatabaseObjectContainer constants.
        """
        return self._type

    @Type.setter
    def Type(self, value: int) -> None:
        self._type = value

    @property
    def Name(self) -> str:
        """
        denotes the name of the object
        
        In case of forms, reports, form folders and report folders, this is the hierarchical path to the object, where the path elements are separated by a slash (/).
        
        In case of tables, this is the fully qualified name of the table, as required by the database's table name composition rules.
        
        In case of queries, this is the name of the query.
        
        In case of virtual folders denoted by DatabaseObjectContainer.CATALOG and DatabaseObjectContainer.SCHEMA, it is
        
        In case of the virtual folders denoted by DatabaseObjectContainer.TABLES, DatabaseObjectContainer.QUERIES, DatabaseObjectContainer.DATA_SOURCE, DatabaseObjectContainer.FORMS or DatabaseObjectContainer.REPORTS, this denotes the name of the data source (as denoted by com.sun.star.sdb.DataSource.Name)
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value


__all__ = ['NamedDatabaseObject']
