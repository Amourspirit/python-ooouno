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

class GroupDescriptor(Descriptor_a5200b3b):
    """
    Service Class

    is used to create a new group in a database.

    See Also:
        `API GroupDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1GroupDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.GroupDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Name(self) -> str:
        """
        is the name of the group.
        """



__all__ = ['GroupDescriptor']

