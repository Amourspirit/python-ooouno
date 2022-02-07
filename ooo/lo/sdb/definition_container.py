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
# Namespace: com.sun.star.sdb
from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
from ..lang.x_single_service_factory import XSingleServiceFactory as XSingleServiceFactory_27210f0d
from ..util.x_refreshable import XRefreshable as XRefreshable_b0d60b81

class DefinitionContainer(XEnumerationAccess_4bac0ffc, XIndexAccess_f0910d6d, XNameContainer_cb90e47, XSingleServiceFactory_27210f0d, XRefreshable_b0d60b81):
    """
    Service Class

    describes a container which provides access to database related definitions like commands, forms, and reports.
    
    The container supports access to its elements by the elements name or by the elements position.
    
    Simple enumeration must be supported as well.
    
    To reflect the changes with the underlying database, a refresh mechanism needs to be supported.

    See Also:
        `API DefinitionContainer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DefinitionContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DefinitionContainer'
    __ooo_type_name__: str = 'service'


__all__ = ['DefinitionContainer']

