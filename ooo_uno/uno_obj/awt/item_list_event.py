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
import os
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class ItemListEvent(EventObject_a3d70b03):
    """
    Struct Class

    is the event broadcasted by a XListItems implementation for changes in its item list.

    See Also:
        `API ItemListEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1ItemListEvent.html>`_


    Note:
        | At runtime ItemListEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | ItemListEvent is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, ItemImageURL: typing.Optional[object] = None, ItemPosition: typing.Optional[int] = None, ItemText: typing.Optional[object] = None):
        self._item_image_url = ItemImageURL
        self._item_position = ItemPosition
        self._item_text = ItemText

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

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global ItemListEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('ItemImageURL', 'ItemPosition', 'ItemText')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.awt.ItemListEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ItemListEvent = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['ItemListEvent']
