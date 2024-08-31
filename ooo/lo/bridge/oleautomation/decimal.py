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
# Namespace: com.sun.star.bridge.oleautomation
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class Decimal(object):
    """
    Struct Class

    is the UNO representation of the Automation type DECIMAL.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Decimal <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1Decimal.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge.oleautomation'
    __ooo_full_ns__: str = 'com.sun.star.bridge.oleautomation.Decimal'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.bridge.oleautomation.Decimal'
    """Literal Constant ``com.sun.star.bridge.oleautomation.Decimal``"""

    def __init__(self, Scale: typing.Optional[int] = 0, Sign: typing.Optional[int] = 0, LowValue: typing.Optional[int] = 0, MiddleValue: typing.Optional[int] = 0, HighValue: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Scale (int, optional): Scale value.
            Sign (int, optional): Sign value.
            LowValue (int, optional): LowValue value.
            MiddleValue (int, optional): MiddleValue value.
            HighValue (int, optional): HighValue value.
        """
        super().__init__()

        if isinstance(Scale, Decimal):
            oth: Decimal = Scale
            self.Scale = oth.Scale
            self.Sign = oth.Sign
            self.LowValue = oth.LowValue
            self.MiddleValue = oth.MiddleValue
            self.HighValue = oth.HighValue
            return

        kargs = {
            "Scale": Scale,
            "Sign": Sign,
            "LowValue": LowValue,
            "MiddleValue": MiddleValue,
            "HighValue": HighValue,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._scale = kwargs["Scale"]
        self._sign = kwargs["Sign"]
        self._low_value = kwargs["LowValue"]
        self._middle_value = kwargs["MiddleValue"]
        self._high_value = kwargs["HighValue"]


    @property
    def Scale(self) -> int:
        """
        corresponds to DECIMAL.scale.
        """
        return self._scale

    @Scale.setter
    def Scale(self, value: int) -> None:
        self._scale = value

    @property
    def Sign(self) -> int:
        """
        corresponds to DECIMAL.sign.
        """
        return self._sign

    @Sign.setter
    def Sign(self, value: int) -> None:
        self._sign = value

    @property
    def LowValue(self) -> int:
        """
        corresponds to DECIMAL.Lo32.
        """
        return self._low_value

    @LowValue.setter
    def LowValue(self, value: int) -> None:
        self._low_value = value

    @property
    def MiddleValue(self) -> int:
        """
        corresponds to DECIMAL.Mid32.
        """
        return self._middle_value

    @MiddleValue.setter
    def MiddleValue(self, value: int) -> None:
        self._middle_value = value

    @property
    def HighValue(self) -> int:
        """
        corresponds to DECIMAL.Hi32.
        """
        return self._high_value

    @HighValue.setter
    def HighValue(self, value: int) -> None:
        self._high_value = value


__all__ = ['Decimal']
