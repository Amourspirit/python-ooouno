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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class FontHeight(object):
    """
    Struct Class

    describes the characteristics of a font.
    
    For example, this can be used to select a font.
    
    **since**
    
        OOo 2.0

    See Also:
        `API FontHeight <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1FontHeight.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.FontHeight'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.FontHeight'
    """Literal Constant ``com.sun.star.frame.status.FontHeight``"""

    def __init__(self, Height: typing.Optional[float] = 0.0, Prop: typing.Optional[int] = 0, Diff: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            Height (float, optional): Height value.
            Prop (int, optional): Prop value.
            Diff (float, optional): Diff value.
        """
        super().__init__()

        if isinstance(Height, FontHeight):
            oth: FontHeight = Height
            self.Height = oth.Height
            self.Prop = oth.Prop
            self.Diff = oth.Diff
            return

        kargs = {
            "Height": Height,
            "Prop": Prop,
            "Diff": Diff,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._height = kwargs["Height"]
        self._prop = kwargs["Prop"]
        self._diff = kwargs["Diff"]


    @property
    def Height(self) -> float:
        """
        specifies the current height of the font.
        """
        return self._height
    
    @Height.setter
    def Height(self, value: float) -> None:
        self._height = value

    @property
    def Prop(self) -> int:
        """
        specifies the height of the font in the measure of the destination.
        """
        return self._prop
    
    @Prop.setter
    def Prop(self, value: int) -> None:
        self._prop = value

    @property
    def Diff(self) -> float:
        """
        specifies the width of the font in the measure of the destination.
        """
        return self._diff
    
    @Diff.setter
    def Diff(self, value: float) -> None:
        self._diff = value


__all__ = ['FontHeight']
