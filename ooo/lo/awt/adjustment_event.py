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
from .adjustment_type import AdjustmentType as AdjustmentType_bd050c15


class AdjustmentEvent(EventObject_a3d70b03):
    """
    Struct Class

    adjustment event emitted by adjustable objects.

    See Also:
        `API AdjustmentEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1AdjustmentEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.AdjustmentEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.AdjustmentEvent'
    """Literal Constant ``com.sun.star.awt.AdjustmentEvent``"""

    def __init__(self, Value: int = 0, Type: AdjustmentType_bd050c15 = AdjustmentType_bd050c15.ADJUST_LINE, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``Value`` can be another ``AdjustmentEvent`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            Value (int, optional): Value value
            Type (AdjustmentType, optional): Type value
        """
        super().__init__(**kwargs)
        if isinstance(Value, AdjustmentEvent):
            oth: AdjustmentEvent = Value
            self._value = oth.Value
            self._type = oth.Type
            return
        else:
            self._value = Value
            self._type = Type



    @property
    def Value(self) -> int:
        """
        contains the current value in the adjustment event.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: int) -> None:
        self._value = value

    @property
    def Type(self) -> AdjustmentType_bd050c15:
        """
        contains the type of the adjustment event.
        """
        return self._type
    
    @Type.setter
    def Type(self, value: AdjustmentType_bd050c15) -> None:
        self._type = value


__all__ = ['AdjustmentEvent']