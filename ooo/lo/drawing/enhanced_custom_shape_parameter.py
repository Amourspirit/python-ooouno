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


class EnhancedCustomShapeParameter(object):
    """
    Struct Class

    specifies a single value which is used with EnhancedCustomShapes

    See Also:
        `API EnhancedCustomShapeParameter <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeParameter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.EnhancedCustomShapeParameter'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.EnhancedCustomShapeParameter'
    """Literal Constant ``com.sun.star.drawing.EnhancedCustomShapeParameter``"""

    def __init__(self, Value: typing.Optional[object] = None, Type: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Value (object, optional): Value value.
            Type (int, optional): Type value.
        """
        super().__init__()

        if isinstance(Value, EnhancedCustomShapeParameter):
            oth: EnhancedCustomShapeParameter = Value
            self.Value = oth.Value
            self.Type = oth.Type
            return

        kargs = {
            "Value": Value,
            "Type": Type,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._value = kwargs["Value"]
        self._type = kwargs["Type"]


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
    def Type(self) -> int:
        return self._type

    @Type.setter
    def Type(self, value: int) -> None:
        self._type = value


__all__ = ['EnhancedCustomShapeParameter']
