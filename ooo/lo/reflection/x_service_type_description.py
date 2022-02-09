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
from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1
if typing.TYPE_CHECKING:
    from .x_interface_type_description import XInterfaceTypeDescription as XInterfaceTypeDescription_d92e1342
    from .x_property_type_description import XPropertyTypeDescription as XPropertyTypeDescription_ca171316

class XServiceTypeDescription(XTypeDescription_3c210fb1):
    """
    Reflects a service.
    
    This type is superseded by XServiceTypeDescription2, which supports single-interface–based services, in addition to the obsolete, accumulation-based services.
    
    The type class of this type is com.sun.star.uno.TypeClass.SERVICE.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XServiceTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XServiceTypeDescription.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.XServiceTypeDescription'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.reflection.XServiceTypeDescription'

    @abstractmethod
    def getMandatoryInterfaces(self) -> 'typing.Tuple[XInterfaceTypeDescription_d92e1342, ...]':
        """
        Returns the type descriptions of the mandatory interfaces defined for this service.
        """
    @abstractmethod
    def getMandatoryServices(self) -> 'typing.Tuple[XServiceTypeDescription, ...]':
        """
        Returns the type descriptions of the mandatory services defined for this service.
        """
    @abstractmethod
    def getOptionalInterfaces(self) -> 'typing.Tuple[XInterfaceTypeDescription_d92e1342, ...]':
        """
        Returns the type descriptions of the optional interface defined for this service.
        """
    @abstractmethod
    def getOptionalServices(self) -> 'typing.Tuple[XServiceTypeDescription, ...]':
        """
        Returns the type descriptions of the optional services defined for this service.
        """
    @abstractmethod
    def getProperties(self) -> 'typing.Tuple[XPropertyTypeDescription_ca171316, ...]':
        """
        Returns the properties defined for this service.
        """


__all__ = ['XServiceTypeDescription']

