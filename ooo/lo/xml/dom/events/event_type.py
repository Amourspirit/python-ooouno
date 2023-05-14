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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.xml.dom.events
# Libre Office Version: 7.4
from enum import Enum


class EventType(Enum):
    """
    Enum Class

    ENUM EventType

    See Also:
        `API EventType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1events.html#a2628ea8d12e8b2563c32f05dc7fff6fa>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom.events'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.events.EventType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.xml.dom.events.EventType'

    DOMActivate = 'DOMActivate'
    """
    """
    DOMAttrModified = 'DOMAttrModified'
    """
    """
    DOMCharacterDataModified = 'DOMCharacterDataModified'
    """
    """
    DOMFocusIn = 'DOMFocusIn'
    """
    """
    DOMFocusOut = 'DOMFocusOut'
    """
    """
    DOMNodeInserted = 'DOMNodeInserted'
    """
    """
    DOMNodeInsertedIntoDocument = 'DOMNodeInsertedIntoDocument'
    """
    """
    DOMNodeRemoved = 'DOMNodeRemoved'
    """
    """
    DOMNodeRemovedFromDocument = 'DOMNodeRemovedFromDocument'
    """
    """
    DOMSubtreeModified = 'DOMSubtreeModified'
    """
    """
    click = 'click'
    """
    """
    mousedown = 'mousedown'
    """
    """
    mousemove = 'mousemove'
    """
    """
    mouseout = 'mouseout'
    """
    """
    mouseover = 'mouseover'
    """
    """
    mouseup = 'mouseup'
    """
    """

__all__ = ['EventType']

