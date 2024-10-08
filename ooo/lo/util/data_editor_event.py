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
# Namespace: com.sun.star.util
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .data_editor_event_type import DataEditorEventType as DataEditorEventType_b080e4b


class DataEditorEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an event broadcasted by an XDataEditor.

    See Also:
        `API DataEditorEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1DataEditorEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.DataEditorEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.DataEditorEvent'
    """Literal Constant ``com.sun.star.util.DataEditorEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Type: typing.Optional[DataEditorEventType_b080e4b] = DataEditorEventType_b080e4b.DONE) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Type (DataEditorEventType, optional): Type value.
        """

        if isinstance(Source, DataEditorEvent):
            oth: DataEditorEvent = Source
            self.Source = oth.Source
            self.Type = oth.Type
            return

        kargs = {
            "Source": Source,
            "Type": Type,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._type = kwargs["Type"]
        inst_keys = ('Type',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Type(self) -> DataEditorEventType_b080e4b:
        """
        specifies the type of the event.
        """
        return self._type

    @Type.setter
    def Type(self, value: DataEditorEventType_b080e4b) -> None:
        self._type = value


__all__ = ['DataEditorEvent']
