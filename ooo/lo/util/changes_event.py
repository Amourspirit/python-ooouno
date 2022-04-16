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
# Namespace: com.sun.star.util
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .changes_set import ChangesSet as ChangesSet_99de0aab


class ChangesEvent(EventObject_a3d70b03):
    """
    Struct Class

    This event is fired when a set of changes becomes effective on the source of the event.

    See Also:
        `API ChangesEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1ChangesEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.ChangesEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.ChangesEvent'
    """Literal Constant ``com.sun.star.util.ChangesEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Base: typing.Optional[object] = None, Changes: typing.Optional[ChangesSet_99de0aab] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Base (object, optional): Base value.
            Changes (ChangesSet, optional): Changes value.
        """

        if isinstance(Source, ChangesEvent):
            oth: ChangesEvent = Source
            self.Source = oth.Source
            self.Base = oth.Base
            self.Changes = oth.Changes
            return

        kargs = {
            "Source": Source,
            "Base": Base,
            "Changes": Changes,
        }
        if kargs["Changes"] is UNO_NONE:
            kargs["Changes"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._base = kwargs["Base"]
        self._changes = kwargs["Changes"]
        inst_keys = ('Base', 'Changes')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Base(self) -> object:
        """
        contains the accessor to the common root of the changed elements.
        
        Type and value of the accessor depend on the service.
        """
        return self._base
    
    @Base.setter
    def Base(self, value: object) -> None:
        self._base = value

    @property
    def Changes(self) -> ChangesSet_99de0aab:
        """
        contains the changes which occurred.
        """
        return self._changes
    
    @Changes.setter
    def Changes(self, value: ChangesSet_99de0aab) -> None:
        self._changes = value


__all__ = ['ChangesEvent']
