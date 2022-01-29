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
    from .x_service_type_description import XServiceTypeDescription as XServiceTypeDescription_b4481282

class XSingletonTypeDescription(XTypeDescription_3c210fb1):
    """
    Reflects a singleton.
    
    This type is superseded by XSingletonTypeDescription2, which supports interface-based singletons, in addition to the obsolete, service-based singletons.
    
    The type class of this type is com.sun.star.uno.TypeClass.SINGLETON.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XSingletonTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XSingletonTypeDescription.html>`_
    """

    @abstractmethod
    def getService(self) -> 'XServiceTypeDescription_b4481282':
        """
        Returns the service associated with the singleton.
        """

__all__ = ['XSingletonTypeDescription']

