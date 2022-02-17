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
# Namespace: com.sun.star.beans
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .get_direct_property_tolerant_result import GetDirectPropertyTolerantResult as GetDirectPropertyTolerantResult_e91c13b9
    from .get_property_tolerant_result import GetPropertyTolerantResult as GetPropertyTolerantResult_7c4e115e
    from .set_property_tolerant_failed import SetPropertyTolerantFailed as SetPropertyTolerantFailed_7cbd1130

class XTolerantMultiPropertySet(XInterface_8f010a43):
    """
    provides access to multiple iformation of a set of properties with a single call.
    
    The speciality of this interface is that none of the functions will throw the usual exceptions associated with setting and retrieving of property values. Instead the data for the failures is collected and returned.
    
    Note: There is no support for property change listeners in this interface.

    See Also:
        `API XTolerantMultiPropertySet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XTolerantMultiPropertySet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.XTolerantMultiPropertySet'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.beans.XTolerantMultiPropertySet'

    @abstractmethod
    def getDirectPropertyValuesTolerant(self, aPropertyNames: 'typing.Tuple[str, ...]') -> 'typing.Tuple[GetDirectPropertyTolerantResult_e91c13b9, ...]':
        """
        retrieve only those values of the specified properties which are direct values.
        
        Since the count of returned elements may be different from the number of supplied property names the returned elements will also state the name of the property.
        
        If the names are not sorted the behaviour of the method is undefined!
        """
    @abstractmethod
    def getPropertyValuesTolerant(self, aPropertyNames: 'typing.Tuple[str, ...]') -> 'typing.Tuple[GetPropertyTolerantResult_7c4e115e, ...]':
        """
        retrieve the values of the specified properties
        
        The count and order of the values in the returned sequence will be the same as the order of the names in the argument.
        
        If the names are not sorted the behaviour of the method is undefined!
        """
    @abstractmethod
    def setPropertyValuesTolerant(self, aPropertyNames: 'typing.Tuple[str, ...]', aValues: 'typing.Tuple[object, ...]') -> 'typing.Tuple[SetPropertyTolerantFailed_7cbd1130, ...]':
        """
        sets the values to the properties with the specified names.
        
        If the names are not sorted the behaviour of the method is undefined!
        
        Otherwise for every property value that could not successfully be set an entry of the com.sun.star.beans.SetPropertyTolerantFailed will be present in this sequence. The order of the properties is also alphabetically ascending.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XTolerantMultiPropertySet']
