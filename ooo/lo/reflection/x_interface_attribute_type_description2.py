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
# Namespace: com.sun.star.reflection
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_interface_attribute_type_description import XInterfaceAttributeTypeDescription as XInterfaceAttributeTypeDescription_98c716f6
if typing.TYPE_CHECKING:
    from .x_compound_type_description import XCompoundTypeDescription as XCompoundTypeDescription_c7be12f6

class XInterfaceAttributeTypeDescription2(XInterfaceAttributeTypeDescription_98c716f6):
    """
    Reflects an interface attribute, supporting extended attributes that are bound or raise exceptions.
    
    This type supersedes XInterfaceAttributeTypeDescription, which does not support extended attributes.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XInterfaceAttributeTypeDescription2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XInterfaceAttributeTypeDescription2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.XInterfaceAttributeTypeDescription2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.reflection.XInterfaceAttributeTypeDescription2'

    @abstractmethod
    def getGetExceptions(self) -> typing.Tuple[XCompoundTypeDescription_c7be12f6, ...]:
        """
        Returns the exceptions that can be raised by the attribute's getter.
        """
        ...
    @abstractmethod
    def getSetExceptions(self) -> typing.Tuple[XCompoundTypeDescription_c7be12f6, ...]:
        """
        Returns the exceptions that can be raised by the attribute's setter.
        """
        ...
    @abstractmethod
    def isBound(self) -> bool:
        """
        Returns whether this object reflects a bound attribute.
        """
        ...

__all__ = ['XInterfaceAttributeTypeDescription2']

