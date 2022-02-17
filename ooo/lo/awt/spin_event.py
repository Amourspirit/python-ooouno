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

    def __init__(self, dummy1: int = 0, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``dummy1`` can be another ``SpinEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            dummy1 (int, optional): dummy1 value
        """
        super().__init__(**kwargs)
        if isinstance(dummy1, SpinEvent):
            oth: SpinEvent = dummy1
            self._dummy1 = oth.dummy1
            return
        else:
            self._dummy1 = dummy1



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
