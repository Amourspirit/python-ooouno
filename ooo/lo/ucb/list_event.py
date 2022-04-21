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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .list_action import ListAction as ListAction_8df40a3c


class ListEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies the type of event fired by an XDynamicResultSet

    See Also:
        `API ListEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1ListEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.ListEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.ListEvent'
    """Literal Constant ``com.sun.star.ucb.ListEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Changes: typing.Optional[typing.Tuple[ListAction_8df40a3c, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Changes (typing.Tuple[ListAction, ...], optional): Changes value.
        """

        if isinstance(Source, ListEvent):
            oth: ListEvent = Source
            self.Source = oth.Source
            self.Changes = oth.Changes
            return

        kargs = {
            "Source": Source,
            "Changes": Changes,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._changes = kwargs["Changes"]
        inst_keys = ('Changes',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Changes(self) -> typing.Tuple[ListAction_8df40a3c, ...]:
        """
        If you apply the given ListActions one after the other to the old version of a result set in given order, you will get the positions in the new version.
        """
        return self._changes
    
    @Changes.setter
    def Changes(self, value: typing.Tuple[ListAction_8df40a3c, ...]) -> None:
        self._changes = value


__all__ = ['ListEvent']
