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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.configuration
from __future__ import annotations
from abc import abstractmethod
from .x_read_write_access import XReadWriteAccess as XReadWriteAccess_6da510b1

class ReadWriteAccess(XReadWriteAccess_6da510b1):
    """
    Service Class

    Provides easy read/write access to the complete configuration.
    
    This service is still unpublished and unstable.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API ReadWriteAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1ReadWriteAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.ReadWriteAccess'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self, locale: str) -> None:
        """
        Service constructor.
        """
        ...

__all__ = ['ReadWriteAccess']

