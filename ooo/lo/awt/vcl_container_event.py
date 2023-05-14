# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43


class VclContainerEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies a container event.
    
    These events are provided only for notification purposes.

    See Also:
        `API VclContainerEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1VclContainerEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.VclContainerEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.VclContainerEvent'
    """Literal Constant ``com.sun.star.awt.VclContainerEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Child: typing.Optional[XInterface_8f010a43] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Child (XInterface, optional): Child value.
        """

        if isinstance(Source, VclContainerEvent):
            oth: VclContainerEvent = Source
            self.Source = oth.Source
            self.Child = oth.Child
            return

        kargs = {
            "Source": Source,
            "Child": Child,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._child = kwargs["Child"]
        inst_keys = ('Child',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Child(self) -> XInterface_8f010a43:
        """
        returns the child component that was added or removed.
        """
        return self._child

    @Child.setter
    def Child(self, value: XInterface_8f010a43) -> None:
        self._child = value


__all__ = ['VclContainerEvent']
