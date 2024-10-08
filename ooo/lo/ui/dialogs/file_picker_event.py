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
# Namespace: com.sun.star.ui.dialogs
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class FilePickerEvent(EventObject_a3d70b03):
    """
    Struct Class

    Context information in case of a FilePicker event.

    See Also:
        `API FilePickerEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1FilePickerEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.FilePickerEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ui.dialogs.FilePickerEvent'
    """Literal Constant ``com.sun.star.ui.dialogs.FilePickerEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, ElementId: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            ElementId (int, optional): ElementId value.
        """

        if isinstance(Source, FilePickerEvent):
            oth: FilePickerEvent = Source
            self.Source = oth.Source
            self.ElementId = oth.ElementId
            return

        kargs = {
            "Source": Source,
            "ElementId": ElementId,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._element_id = kwargs["ElementId"]
        inst_keys = ('ElementId',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def ElementId(self) -> int:
        """
        Identifies the affected element.
        """
        return self._element_id

    @ElementId.setter
    def ElementId(self, value: int) -> None:
        self._element_id = value


__all__ = ['FilePickerEvent']
