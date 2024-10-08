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
# Namespace: com.sun.star.uno
from __future__ import annotations
from abc import abstractmethod, ABC

class XInterface(ABC):
    """
    base interface of all UNO interfaces
    
    It provides lifetime control by reference counting and the possibility of querying for other interfaces of the same logical object.
    
    \"Logical Object\" in this case means that the interfaces actually can be supported by internal (e.g. aggregated) physical objects.
    
    Deriving from this interface is mandatory for all UNO interfaces.
    
    Each language binding (Java, C++, StarBasic, Python, ... ) may provide a different mapping of this interface, please look into the language dependent documentation.
    
    The UNO object does not export the state of the reference count (acquire() and release() do not have return values). In general, also the UNO object itself should not make any assumption on the concrete value of the reference count (except on the transition from one to zero ).

    See Also:
        `API XInterface <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.XInterface'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.uno.XInterface'

    @abstractmethod
    def acquire(self) -> None:
        """
        increases the reference counter by one.
        
        When you have called acquire() on the UNO object, it is often said, that you have a reference or a hard reference to the object.
        
        It is only allowed to invoke a method on a UNO object, when you keep a hard reference to it.
        
        Every call to acquire must be followed by a corresponding call to release some time later, which may eventually lead to the destruction of the object.
        """
        ...
    @abstractmethod
    def queryInterface(self, aType: object) -> object:
        """
        queries for a new interface to an existing UNO object.
        
        The queryInterface() method is the entry point to obtain other interfaces which are exported by the object. The caller asks the implementation of the object, if it supports the interface specified by the type argument. The call may either return with an interface reference of the requested type or with a void any.
        
        There are certain specifications, a queryInterface() implementation must not violate.
        
        1) If queryInterface on a specific object has once returned a valid interface reference for a given type, it must return a valid reference for any successive queryInterface calls on this object for the same type.
        
        2) If queryInterface on a specific object has once returned a null reference for a given type, it must always return a null reference for the same type.
        
        3) If queryInterface on a reference A returns reference B, queryInterface on B for Type A must return interface reference A or calls made on the returned reference must be equivalent to calls made on reference A.
        
        4) If queryInterface on a reference A returns reference B, queryInterface on A and B for XInterface must return the same interface reference (object identity).
        
        The reason for the strong specification is, that a Uno Runtime Environment (URE) may choose to cache queryInterface() calls.
        
        As mentioned above, certain language bindings may map this function differently also with different specifications, please visit the language dependent specification for it. The current C++ binding sticks to the specification state
        
        The rules mentioned above are basically identical to the rules of QueryInterface in MS COM.
        """
        ...
    @abstractmethod
    def release(self) -> None:
        """
        decreases the reference counter by one.
        
        When the reference counter reaches 0, the object gets deleted.
        
        Calling release() on the object is often called releasing or clearing the reference to an object.
        """
        ...

__all__ = ['XInterface']

