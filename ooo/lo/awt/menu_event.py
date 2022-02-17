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
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing


class MenuEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies a menu event.

    See Also:
        `API MenuEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1MenuEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.MenuEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.MenuEvent'
    """Literal Constant ``com.sun.star.awt.MenuEvent``"""

    def __init__(self, MenuId: int = 0, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``MenuId`` can be another ``MenuEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            MenuId (int, optional): MenuId value
        """
        super().__init__(**kwargs)
        if isinstance(MenuId, MenuEvent):
            oth: MenuEvent = MenuId
            self._menu_id = oth.MenuId
            return
        else:
            self._menu_id = MenuId



    @property
    def MenuId(self) -> int:
        """
        contains the item ID.
        """
        return self._menu_id
    
    @MenuId.setter
    def MenuId(self, value: int) -> None:
        self._menu_id = value


__all__ = ['MenuEvent']
