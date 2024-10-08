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
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..beans.property_state import PropertyState as PropertyState_c97b0c77


class EnhancedCustomShapeAdjustmentValue(object):
    """
    Struct Class

    specifies a single AdjustmentValue

    See Also:
        `API EnhancedCustomShapeAdjustmentValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeAdjustmentValue.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.EnhancedCustomShapeAdjustmentValue'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.EnhancedCustomShapeAdjustmentValue'
    """Literal Constant ``com.sun.star.drawing.EnhancedCustomShapeAdjustmentValue``"""

    def __init__(self, Value: typing.Optional[object] = None, State: typing.Optional[PropertyState_c97b0c77] = PropertyState_c97b0c77.DIRECT_VALUE, Name: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Value (object, optional): Value value.
            State (PropertyState, optional): State value.
            Name (str, optional): Name value.
        """
        super().__init__()

        if isinstance(Value, EnhancedCustomShapeAdjustmentValue):
            oth: EnhancedCustomShapeAdjustmentValue = Value
            self.Value = oth.Value
            self.State = oth.State
            self.Name = oth.Name
            return

        kargs = {
            "Value": Value,
            "State": State,
            "Name": Name,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._value = kwargs["Value"]
        self._state = kwargs["State"]
        self._name = kwargs["Name"]


    @property
    def Value(self) -> object:
        """
        the any can be of type long or double
        """
        return self._value

    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value

    @property
    def State(self) -> PropertyState_c97b0c77:
        return self._state

    @State.setter
    def State(self, value: PropertyState_c97b0c77) -> None:
        self._state = value

    @property
    def Name(self) -> str:
        """
        optional name, used by pptx import/export for custom shape presets
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value


__all__ = ['EnhancedCustomShapeAdjustmentValue']
