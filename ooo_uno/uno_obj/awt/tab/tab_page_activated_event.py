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
# Namespace: com.sun.star.awt.tab
# Libre Office Version: 7.2
from ...lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class TabPageActivatedEvent(EventObject_a3d70b03):
        """
        Struct Class

        An event used by a XTabPageContainer to notify changes in tab page activation.
        
        **since**
        
            OOo 3.4

        See Also:
            `API TabPageActivatedEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1tab_1_1TabPageActivatedEvent.html>`_


        Note:
            | At runtime TabPageActivatedEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | TabPageActivatedEvent is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, TabPageID: typing.Optional[int] = None):
            self._tab_page_id = TabPageID

        @property
        def TabPageID(self) -> int:
            """
            Contains the ID of the tab page.
            """
            return self._tab_page_id
        
        @TabPageID.setter
        def TabPageID(self, value: int) -> None:
            self._tab_page_id = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global TabPageActivatedEvent
        order = ('TabPageID',)

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.awt.tab.TabPageActivatedEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        TabPageActivatedEvent = _struct_init

    _dynamic_struct()

__all__ = ['TabPageActivatedEvent']
