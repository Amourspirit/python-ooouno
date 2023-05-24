# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.text.textfield
from __future__ import annotations
from abc import abstractproperty
from ..dependent_text_field import DependentTextField as DependentTextField_fed90ded

class DatabaseNumberOfSet(DependentTextField_fed90ded):
    """
    Service Class

    specifies service of text field that conditionally set the selection of a database cursor.
    
    Only one of the properties DataBaseName, DataBaseURL and DataBaseResource should be set. If more than one are set the last one will be used.
    
    **since**
    
        OOo 2.0

    See Also:
        `API DatabaseNumberOfSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1DatabaseNumberOfSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text.textfield'
    __ooo_full_ns__: str = 'com.sun.star.text.textfield.DatabaseNumberOfSet'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Condition(self) -> str:
        """
        contains the conditions that determines whether the SetNumber is applied or not.
        """
        ...

    @abstractproperty
    def DataBaseName(self) -> str:
        """
        specifies the database name.
        """
        ...

    @abstractproperty
    def DataBaseResource(self) -> str:
        """
        indicates a connection URL, which locates a database driver.
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def DataBaseURL(self) -> str:
        """
        indicates the URL of a database file.
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def DataCommandType(self) -> int:
        """
        determines the interpretation of the property DataTableName.
        """
        ...

    @abstractproperty
    def DataTableName(self) -> str:
        """
        contains the name of the database table, query or a statement depending on the DataCommandType property.
        """
        ...

    @abstractproperty
    def SetNumber(self) -> int:
        """
        contains the set number that is to be applied.
        """
        ...


__all__ = ['DatabaseNumberOfSet']

