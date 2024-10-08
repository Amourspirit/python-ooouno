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


class BarCode(object):
    """
    Struct Class

    This struct defines the attributes of a Bar Code.
    
    **since**
    
        LibreOffice 7.3

    See Also:
        `API BarCode <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1BarCode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.BarCode'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.BarCode'
    """Literal Constant ``com.sun.star.drawing.BarCode``"""

    def __init__(self, Type: typing.Optional[int] = 0, Payload: typing.Optional[str] = '', ErrorCorrection: typing.Optional[int] = 0, Border: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Type (int, optional): Type value.
            Payload (str, optional): Payload value.
            ErrorCorrection (int, optional): ErrorCorrection value.
            Border (int, optional): Border value.
        """
        super().__init__()

        if isinstance(Type, BarCode):
            oth: BarCode = Type
            self.Type = oth.Type
            self.Payload = oth.Payload
            self.ErrorCorrection = oth.ErrorCorrection
            self.Border = oth.Border
            return

        kargs = {
            "Type": Type,
            "Payload": Payload,
            "ErrorCorrection": ErrorCorrection,
            "Border": Border,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._type = kwargs["Type"]
        self._payload = kwargs["Payload"]
        self._error_correction = kwargs["ErrorCorrection"]
        self._border = kwargs["Border"]


    @property
    def Type(self) -> int:
        """
        Type of the Bar Code that is to be generated.
        
        Supported types - 0:\"QR Code\", 1:\"Code 128\"
        """
        return self._type

    @Type.setter
    def Type(self, value: int) -> None:
        self._type = value

    @property
    def Payload(self) -> str:
        """
        Text for which Bar Code is made.
        """
        return self._payload

    @Payload.setter
    def Payload(self, value: str) -> None:
        self._payload = value

    @property
    def ErrorCorrection(self) -> int:
        """
        Bar Code Error Correction Level.
        """
        return self._error_correction

    @ErrorCorrection.setter
    def ErrorCorrection(self, value: int) -> None:
        self._error_correction = value

    @property
    def Border(self) -> int:
        """
        Border surrounding the Bar Code It is a non-negative value.
        
        One Border unit is equal to one dot in the generated Bar code.
        """
        return self._border

    @Border.setter
    def Border(self, value: int) -> None:
        self._border = value


__all__ = ['BarCode']
