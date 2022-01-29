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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.reflection
import typing
from abc import abstractmethod
from .x_interface_member_type_description import XInterfaceMemberTypeDescription as XInterfaceMemberTypeDescription_52ea159a
if typing.TYPE_CHECKING:
    from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1

class XInterfaceAttributeTypeDescription(XInterfaceMemberTypeDescription_52ea159a):
    """
    Reflects an interface attribute type.
    
    This type is superseded by XInterfaceAttributeTypeDescription2, which supports extended attributes.
    
    The type class of this type is TypeClass_INTERFACE_ATTRIBUTE.

    See Also:
        `API XInterfaceAttributeTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XInterfaceAttributeTypeDescription.html>`_
    """

    @abstractmethod
    def getType(self) -> 'XTypeDescription_3c210fb1':
        """
        Returns the type of the attribute.
        """
    @abstractmethod
    def isReadOnly(self) -> bool:
        """
        Returns true, if this attribute is read-only.
        """

__all__ = ['XInterfaceAttributeTypeDescription']

