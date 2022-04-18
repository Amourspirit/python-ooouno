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
# Libre Office Version: 7.3
# Namespace: com.sun.star.beans
import typing
from abc import abstractmethod
from .x_property_bag import XPropertyBag as XPropertyBag_bbd00bd8

class PropertyBag(XPropertyBag_bbd00bd8):
    """
    Service Class

    Implementation of this service can keep any properties and is useful when an XPropertySet is to be used, for example, as parameters for a method call.
    
    Scripting engines might not be able to use such objects as normal property sets, giving direct access to the properties. In this case, use the methods like XPropertySet.getPropertyValue().

    See Also:
        `API PropertyBag <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1beans_1_1PropertyBag.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.PropertyBag'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createDefault(self) -> None:
        """
        """
    @abstractmethod
    def createWithTypes(self, AllowedTypes: 'typing.Tuple[object, ...]', AllowEmptyPropertyName: bool, AutomaticAddition: bool) -> None:
        """
        """


__all__ = ['PropertyBag']

