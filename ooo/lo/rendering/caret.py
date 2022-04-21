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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing


class Caret(object):
    """
    Struct Class

    This structure contains the caret information.
    
    This structure is used from the XTextLayout interface to transport information regarding a text caret.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Caret <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1Caret.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.Caret'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.Caret'
    """Literal Constant ``com.sun.star.rendering.Caret``"""

    def __init__(self, MainCaretIndex: typing.Optional[int] = 0, SecondaryCaretIndex: typing.Optional[int] = 0, CaretAngle: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            MainCaretIndex (int, optional): MainCaretIndex value.
            SecondaryCaretIndex (int, optional): SecondaryCaretIndex value.
            CaretAngle (float, optional): CaretAngle value.
        """
        super().__init__()

        if isinstance(MainCaretIndex, Caret):
            oth: Caret = MainCaretIndex
            self.MainCaretIndex = oth.MainCaretIndex
            self.SecondaryCaretIndex = oth.SecondaryCaretIndex
            self.CaretAngle = oth.CaretAngle
            return

        kargs = {
            "MainCaretIndex": MainCaretIndex,
            "SecondaryCaretIndex": SecondaryCaretIndex,
            "CaretAngle": CaretAngle,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._main_caret_index = kwargs["MainCaretIndex"]
        self._secondary_caret_index = kwargs["SecondaryCaretIndex"]
        self._caret_angle = kwargs["CaretAngle"]


    @property
    def MainCaretIndex(self) -> int:
        """
        This contains the main caret index.
        
        The main caret index corresponds to the insert position when inserting text in the layout's main text direction.
        """
        return self._main_caret_index
    
    @MainCaretIndex.setter
    def MainCaretIndex(self, value: int) -> None:
        self._main_caret_index = value

    @property
    def SecondaryCaretIndex(self) -> int:
        """
        This contains the secondary caret index.
        
        The secondary caret index, when different from the main caret index, corresponds to the insert position when inserting text at a direction change opposite to the layout's main text direction.
        """
        return self._secondary_caret_index
    
    @SecondaryCaretIndex.setter
    def SecondaryCaretIndex(self, value: int) -> None:
        self._secondary_caret_index = value

    @property
    def CaretAngle(self) -> float:
        """
        The angle of the caret.
        
        This member contains the rotation angle of the caret in degrees, with 0 denoting an unrotated caret (the unrotated caret orientation depends on the writing mode, horizontally or vertically). The rotation angle is positive for counter-clockwise rotations.
        """
        return self._caret_angle
    
    @CaretAngle.setter
    def CaretAngle(self, value: float) -> None:
        self._caret_angle = value


__all__ = ['Caret']
