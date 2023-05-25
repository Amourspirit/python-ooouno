# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.container
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_map import XMap as XMap_90a60a41
if typing.TYPE_CHECKING:
    from .x_enumeration import XEnumeration as XEnumeration_f2180daa

class XEnumerableMap(XMap_90a60a41):
    """
    extends XMap with enumeration capabilities.
    
    No assumption should be made about the ordering of the elements returned by the various enumerators. In particular, you cannot assume the elements are returned in the same order as they were inserted. Also, you should not expect the XMap implementation to make use of a possibly existing strict ordering defined on the domain of all possible key values.
    
    You can create enumerators for the keys of the map, its values, and its key-value pairs.
    
    In all cases, you can create an isolated enumerator, which works on a copy of the map's content. Such an iterator is not affected by changes done to the map after creation of the enumerator.
    
    On the contrary, an enumerator which is non-isolated works directly on the map data. This is less expensive than an isolated enumerator, but means that changes to the map while an enumeration is running potentially invalidate your enumerator. The concrete behavior in this case is undefined, it's up to the service implementing the XEnumerableMap interface to specify it in more detail.
    
    Implementations of this interface might decide to support only isolated enumerators, or only non-isolated enumerators. Again, it's up to the service to specify this. Requesting an enumerator type which is not supported will generally result in a com.sun.star.lang.NoSupportException being thrown.

    See Also:
        `API XEnumerableMap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XEnumerableMap.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.container'
    __ooo_full_ns__: str = 'com.sun.star.container.XEnumerableMap'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.container.XEnumerableMap'

    @abstractmethod
    def createElementEnumeration(self, Isolated: bool) -> XEnumeration_f2180daa:
        """
        creates an enumerator for the key-value pairs of the map
        
        The elements returned by the enumerator are instances of com.sun.star.beans.Pair, holding the key-value-pairs which are part of the map.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...
    @abstractmethod
    def createKeyEnumeration(self, Isolated: bool) -> XEnumeration_f2180daa:
        """
        creates an enumerator for the keys of the map

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...
    @abstractmethod
    def createValueEnumeration(self, Isolated: bool) -> XEnumeration_f2180daa:
        """
        creates an enumerator for the values of the map

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...

__all__ = ['XEnumerableMap']


