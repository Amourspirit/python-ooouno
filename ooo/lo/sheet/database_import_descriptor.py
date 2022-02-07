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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from .data_import_mode import DataImportMode as DataImportMode_d4630c9b

class DatabaseImportDescriptor(ABC):
    """
    Service Class

    represents a description of how data from an external database is imported.
    
    **since**
    
        OOo 2.0

    See Also:
        `API DatabaseImportDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DatabaseImportDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DatabaseImportDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ConnectionResource(self) -> str:
        """
        indicates a connection URL, which locates a database driver.
        
        **since**
        
            OOo 2.0
        """
    @abstractproperty
    def DatabaseName(self) -> str:
        """
        specifies the name of the database from which data is imported.
        """
    @abstractproperty
    def IsNative(self) -> bool:
        """
        specifies whether the SQL statement is given directly to the database or is parsed before.
        
        **since**
        
            OOo 2.0
        """
    @abstractproperty
    def SourceObject(self) -> str:
        """
        specifies the table, query, or statement from which data is imported.
        
        The meaning of this is determined by the DatabaseImportDescriptor.SourceType attribute.
        """
    @abstractproperty
    def SourceType(self) -> 'DataImportMode_d4630c9b':
        """
        enables importing and specifies from what type of source data is imported.
        """

__all__ = ['DatabaseImportDescriptor']

