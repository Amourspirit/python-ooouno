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
# Namespace: com.sun.star.lang
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_event_listener import XEventListener as XEventListener_c7230c4a

class XComponent(XInterface_8f010a43):
    """
    allows to explicitly free resources and break cyclic references.
    
    Actually the real lifetime of a UNO object is controlled by references kept on interfaces of this object. But there are two distinct meanings in keeping a reference to an interface: 1st to own the object and 2nd to know the object.
    
    You are only allowed to keep references of interfaces to UNO objects if you are by definition the owner of that object or your reference is very temporary or you have registered an EventListener at that object and release the reference when \"disposing\" is called.

    See Also:
        `API XComponent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XComponent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.lang'
    __ooo_full_ns__: str = 'com.sun.star.lang.XComponent'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.lang.XComponent'

    @abstractmethod
    def addEventListener(self, xListener: XEventListener_c7230c4a) -> None:
        """
        adds an event listener to the object.
        
        The broadcaster fires the disposing method of this listener if the XComponent.dispose() method is called.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        
        If this XComponent is already disposed when XComponent.addEventListener() is called, the call will not fail with a DisposedException, but the caller will be notified via the XEventListener.disposing() callback. This callback can occur synchronously within the addEventListener() call.
        """
        ...
    @abstractmethod
    def dispose(self) -> None:
        """
        The owner of an object calls this method to explicitly free all resources kept by this object and thus break cyclic references.
        
        Only the owner of this object is allowed to call this method. The object should release all resources and references in the easiest possible manner ( for instance no serialization should take place anymore ).
        
        The object must notify all registered listeners using the method XEventListener.disposing(). All notified objects should release their references to this object without calling XComponent.removeEventListener() (the disposed object will release the listeners eitherway).
        
        After this method has been called, the object should behave as passive as possible, thus it should ignore all calls in case it can comply with its specification (for instance addEventListener()). Often the object can't fulfill its specification anymore, in this case it must throw the DisposedException (which is derived from com.sun.star.uno.RuntimeException) when it gets called.
        
        For some objects no real owner can be identified, thus it can be disposed from multiple reference holders. In this case the object should be able to cope with multiple dispose()-calls (which are inevitable in a multithreaded environment).
        """
        ...
    @abstractmethod
    def removeEventListener(self, aListener: XEventListener_c7230c4a) -> None:
        """
        removes an event listener from the listener list.
        
        It is a \"noop\" if the specified listener is not registered.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        
        If this XComponent is already disposed when XComponent.removeEventListener() is called, the call will not fail with a DisposedException, but will rather be ignored silently.
        """
        ...

__all__ = ['XComponent']

