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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03


class ItemListEvent(EventObject_a3d70b03):
    """
    Struct Class

    is the event broadcasted by a XListItems implementation for changes in its item list.

    See Also:
        `API ItemListEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1ItemListEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.ItemListEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.ItemListEvent'
    """Literal Constant ``com.sun.star.awt.ItemListEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ItemListEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ItemListEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ItemPosition (int, optional): ItemPosition value
            ItemText (object, optional): ItemText value
            ItemImageURL (object, optional): ItemImageURL value
        """
        self._item_position = None
        self._item_text = None
        self._item_image_url = None

        key_order = ('ItemPosition', 'ItemText', 'ItemImageURL')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ItemListEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ItemListEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def ItemPosition(self) -> int:
        """
        specifies the position of the item which is affected by the event
        
        In case the event is not related to a single item, but to the complete list, the value of this member is undefined.
        """
        return self._item_position
    
    @ItemPosition.setter
    def ItemPosition(self, value: int) -> None:
        self._item_position = value

    @property
    def ItemText(self) -> object:
        """
        the text of the item.
        
        If the event being notified did not touch the text of an item, this member is empty. For instance, upon invocation of XItemList.setItemImage(), only ItemImageURL will be set, and ItemText will be empty.
        """
        return self._item_text
    
    @ItemText.setter
    def ItemText(self, value: object) -> None:
        self._item_text = value

    @property
    def ItemImageURL(self) -> object:
        """
        the URL of the image of the item
        
        If the event being notified did not touch the image of an item, this member is empty. For instance, upon invocation of XItemList.setItemText(), only ItemText will be set, and ItemImageURL will be empty.
        """
        return self._item_image_url
    
    @ItemImageURL.setter
    def ItemImageURL(self, value: object) -> None:
        self._item_image_url = value


__all__ = ['ItemListEvent']
