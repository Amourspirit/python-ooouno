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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.xml.crypto.sax
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ...sax.x_attribute_list import XAttributeList as XAttributeList_eec70d7b


class ElementStackItem(object):
    """
    Struct Class

    A struct to keep a startElement/endElement SAX event.

    See Also:
        `API ElementStackItem <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1ElementStackItem.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.sax.ElementStackItem'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.xml.crypto.sax.ElementStackItem'
    """Literal Constant ``com.sun.star.xml.crypto.sax.ElementStackItem``"""

    def __init__(self, isStartElementEvent: typing.Optional[bool] = False, elementName: typing.Optional[str] = '', xAttributes: typing.Optional[XAttributeList_eec70d7b] = None) -> None:
        """
        Constructor

        Arguments:
            isStartElementEvent (bool, optional): isStartElementEvent value.
            elementName (str, optional): elementName value.
            xAttributes (XAttributeList, optional): xAttributes value.
        """
        super().__init__()

        if isinstance(isStartElementEvent, ElementStackItem):
            oth: ElementStackItem = isStartElementEvent
            self.isStartElementEvent = oth.isStartElementEvent
            self.elementName = oth.elementName
            self.xAttributes = oth.xAttributes
            return

        kargs = {
            "isStartElementEvent": isStartElementEvent,
            "elementName": elementName,
            "xAttributes": xAttributes,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._is_start_element_event = kwargs["isStartElementEvent"]
        self._element_name = kwargs["elementName"]
        self._x_attributes = kwargs["xAttributes"]


    @property
    def isStartElementEvent(self) -> bool:
        """
        whether it is a startElement event
        """
        return self._is_start_element_event

    @isStartElementEvent.setter
    def isStartElementEvent(self, value: bool) -> None:
        self._is_start_element_event = value

    @property
    def elementName(self) -> str:
        """
        the name of the element
        """
        return self._element_name

    @elementName.setter
    def elementName(self, value: str) -> None:
        self._element_name = value

    @property
    def xAttributes(self) -> XAttributeList_eec70d7b:
        """
        attribute list for a startElement event
        """
        return self._x_attributes

    @xAttributes.setter
    def xAttributes(self, value: XAttributeList_eec70d7b) -> None:
        self._x_attributes = value


__all__ = ['ElementStackItem']
