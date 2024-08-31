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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdb.tools
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ...container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
    from ...lang.x_component import XComponent as XComponent_98dc0ab5
    from ..x_single_select_query_composer import XSingleSelectQueryComposer as XSingleSelectQueryComposer_66e310b9
    from .x_data_source_meta_data import XDataSourceMetaData as XDataSourceMetaData_547c0fe4
    from .x_object_names import XObjectNames as XObjectNames_ed550d43
    from .x_table_name import XTableName as XTableName_d3140c61

class XConnectionTools(ABC):
    """
    encapsulates various useful functionality around a com.sun.star.sdb.Connection
    
    Most of the functionality provided here is meaningful only relative to a given database connection. For instance, for quoting table names, you need the meta data instance of the connection. Thus, the entry point for obtaining a XConnectionTools instance is the com.sun.star.sdb.Connection service.
    
    Note that nearly all functionality provided by this interface is also available by other means, it's only provided here for convenience purposes.
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API XConnectionTools <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1tools_1_1XConnectionTools.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.tools'
    __ooo_full_ns__: str = 'com.sun.star.sdb.tools.XConnectionTools'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.tools.XConnectionTools'

    @abstractmethod
    def createTableName(self) -> XTableName_d3140c61:
        """
        creates an instance supporting the XTableName interface, which can be used to manipulate table names for various purposes.
        
        The returned object is guaranteed to not be NULL.
        """
        ...
    @abstractmethod
    def getComposer(self, commandType: int, command: str) -> XSingleSelectQueryComposer_66e310b9:
        """
        get the composer initialized with a command and command type.
        """
        ...
    @abstractmethod
    def getDataSourceMetaData(self) -> XDataSourceMetaData_547c0fe4:
        """
        provides access to the application-level data source meta data
        """
        ...
    @abstractmethod
    def getFieldsByCommandDescriptor(self, commandType: int, command: str, keepFieldsAlive: XComponent_98dc0ab5) -> XNameAccess_e2ab0cf6:
        """
        get fields for a result set given by a \"command descriptor\"
        
        A command descriptor here means:

        * ``keepFieldsAlive`` is an out direction argument.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getObjectNames(self) -> XObjectNames_ed550d43:
        """
        returns an instance supporting the XObjectNames interface, which provides access to functionality around table and query names.
        
        The returned object is guaranteed to not be NULL.
        """
        ...

__all__ = ['XConnectionTools']

