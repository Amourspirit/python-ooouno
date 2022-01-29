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
# Namespace: com.sun.star.sdbcx
from abc import abstractproperty
from .descriptor import Descriptor as Descriptor_a5200b3b

class ViewDescriptor(Descriptor_a5200b3b):
    """
    is used to define a new view for a database.

    See Also:
        `API ViewDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1ViewDescriptor.html>`_
    """

    @abstractproperty
    def CatalogName(self) -> str:
        """
        is the name of the views catalog, may be empty.
        """
    @abstractproperty
    def CheckOption(self) -> int:
        """
        indicates if a check option should be used for the view.
        """
    @abstractproperty
    def Command(self) -> str:
        """
        is the command for creating the view.
        
        After appending a view to its container, the command may be empty. This is typically a SQL Select-Statement.
        """
    @abstractproperty
    def SchemaName(self) -> str:
        """
        is the name of the views schema, may be empty.
        """

__all__ = ['ViewDescriptor']

