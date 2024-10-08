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
# Namespace: com.sun.star.configuration.backend
from __future__ import annotations
from abc import abstractmethod
from .x_schema_supplier import XSchemaSupplier as XSchemaSupplier_eca11373

class XVersionedSchemaSupplier(XSchemaSupplier_eca11373):
    """
    provides access to versioned configuration component schemas.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XVersionedSchemaSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XVersionedSchemaSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.XVersionedSchemaSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.configuration.backend.XVersionedSchemaSupplier'

    @abstractmethod
    def getSchemaVersion(self, aComponent: str) -> str:
        """
        Returns the schema version for a particular component.
        
        The format of the version string is arbitrary. No meaning should be attached to it, unless an implementing service defines one. If no version can be determined, an empty string may be returned.
        
        Clients may assume that all instances of a schema with the same version are identical. The converse is not true. In particular an implementation may return the same version string for all schemas it supplies (i.e. return a version for the complete schema, including all components)

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XVersionedSchemaSupplier']

