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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.container
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing


class ContainerEvent(EventObject_a3d70b03):
    """
    Struct Class

    This event is fired when an element is inserted in a container.

    See Also:
        `API ContainerEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1container_1_1ContainerEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.container'
    __ooo_full_ns__: str = 'com.sun.star.container.ContainerEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.container.ContainerEvent'
    """Literal Constant ``com.sun.star.container.ContainerEvent``"""

    def __init__(self, Accessor: object = None, Element: object = None, ReplacedElement: object = None, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``Accessor`` can be another ``ContainerEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            Accessor (object, optional): Accessor value
            Element (object, optional): Element value
            ReplacedElement (object, optional): ReplacedElement value
        """
        super().__init__(**kwargs)
        if isinstance(Accessor, ContainerEvent):
            oth: ContainerEvent = Accessor
            self._accessor = oth.Accessor
            self._element = oth.Element
            self._replaced_element = oth.ReplacedElement
            return
        else:
            self._accessor = Accessor
            self._element = Element
            self._replaced_element = ReplacedElement



    @property
    def Accessor(self) -> object:
        """
        It contains the accessor to the element which is inserted or removed.
        
        The type and the value of the accessor depends on the service.
        """
        return self._accessor
    
    @Accessor.setter
    def Accessor(self, value: object) -> None:
        self._accessor = value

    @property
    def Element(self) -> object:
        """
        This contains the element that was inserted or removed.
        """
        return self._element
    
    @Element.setter
    def Element(self, value: object) -> None:
        self._element = value

    @property
    def ReplacedElement(self) -> object:
        """
        This contains the replaced element.
        """
        return self._replaced_element
    
    @ReplacedElement.setter
    def ReplacedElement(self, value: object) -> None:
        self._replaced_element = value


__all__ = ['ContainerEvent']