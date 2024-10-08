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
# Namespace: com.sun.star.awt.tab
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class TabPageActivatedEvent(EventObject_a3d70b03):
    """
    Struct Class

    An event used by a XTabPageContainer to notify changes in tab page activation.
    
    **since**
    
        OOo 3.4

    See Also:
        `API TabPageActivatedEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1tab_1_1TabPageActivatedEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tab'
    __ooo_full_ns__: str = 'com.sun.star.awt.tab.TabPageActivatedEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.tab.TabPageActivatedEvent'
    """Literal Constant ``com.sun.star.awt.tab.TabPageActivatedEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, TabPageID: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            TabPageID (int, optional): TabPageID value.
        """

        if isinstance(Source, TabPageActivatedEvent):
            oth: TabPageActivatedEvent = Source
            self.Source = oth.Source
            self.TabPageID = oth.TabPageID
            return

        kargs = {
            "Source": Source,
            "TabPageID": TabPageID,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._tab_page_id = kwargs["TabPageID"]
        inst_keys = ('TabPageID',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def TabPageID(self) -> int:
        """
        Contains the ID of the tab page.
        """
        return self._tab_page_id

    @TabPageID.setter
    def TabPageID(self, value: int) -> None:
        self._tab_page_id = value


__all__ = ['TabPageActivatedEvent']
