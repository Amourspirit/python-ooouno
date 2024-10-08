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
# Namespace: com.sun.star.awt
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class SpinEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies a spin button event.

    See Also:
        `API SpinEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1SpinEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.SpinEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.SpinEvent'
    """Literal Constant ``com.sun.star.awt.SpinEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, dummy1: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            dummy1 (int, optional): dummy1 value.
        """

        if isinstance(Source, SpinEvent):
            oth: SpinEvent = Source
            self.Source = oth.Source
            self.dummy1 = oth.dummy1
            return

        kargs = {
            "Source": Source,
            "dummy1": dummy1,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._dummy1 = kwargs["dummy1"]
        inst_keys = ('dummy1',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def dummy1(self) -> int:
        """
        This is a dummy field only.
        
        Please ignore.
        """
        return self._dummy1

    @dummy1.setter
    def dummy1(self, value: int) -> None:
        self._dummy1 = value


__all__ = ['SpinEvent']
