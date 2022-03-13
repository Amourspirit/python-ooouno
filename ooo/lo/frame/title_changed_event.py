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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class TitleChangedEvent(EventObject_a3d70b03):
    """
    Struct Class

    Contains the information about a changed title.

    See Also:
        `API TitleChangedEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1TitleChangedEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.TitleChangedEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.TitleChangedEvent'
    """Literal Constant ``com.sun.star.frame.TitleChangedEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Title: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Title (str, optional): Title value.
        """

        if isinstance(Source, TitleChangedEvent):
            oth: TitleChangedEvent = Source
            self.Source = oth.Source
            self.Title = oth.Title
            return

        kargs = {
            "Source": Source,
            "Title": Title,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._title = kwargs["Title"]
        inst_keys = ('Title',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Title(self) -> str:
        """
        The new title.
        """
        return self._title
    
    @Title.setter
    def Title(self, value: str) -> None:
        self._title = value


__all__ = ['TitleChangedEvent']
