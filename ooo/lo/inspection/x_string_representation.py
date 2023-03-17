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
# Libre Office Version: 7.4
# Namespace: com.sun.star.inspection
from abc import abstractmethod, ABC

class XStringRepresentation(ABC):
    """
    handles string representations of property values.

    See Also:
        `API XStringRepresentation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XStringRepresentation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.inspection'
    __ooo_full_ns__: str = 'com.sun.star.inspection.XStringRepresentation'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.inspection.XStringRepresentation'

    @abstractmethod
    def convertToControlValue(self, PropertyValue: object) -> str:
        """
        converts a into a string.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def convertToPropertyValue(self, ControlValue: str, ControlValueType: object) -> object:
        """
        converts a string into an any with the type defined by the target type.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XStringRepresentation']

