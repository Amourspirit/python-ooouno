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
# Namespace: com.sun.star.rendering
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class Panose(object):
    """
    Struct Class


    See Also:
        `API Panose <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1Panose.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.Panose'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.Panose'
    """Literal Constant ``com.sun.star.rendering.Panose``"""

    def __init__(self, FamilyType: typing.Optional[int] = 0, SerifStyle: typing.Optional[int] = 0, Weight: typing.Optional[int] = 0, Proportion: typing.Optional[int] = 0, Contrast: typing.Optional[int] = 0, StrokeVariation: typing.Optional[int] = 0, ArmStyle: typing.Optional[int] = 0, Letterform: typing.Optional[int] = 0, Midline: typing.Optional[int] = 0, XHeight: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            FamilyType (int, optional): FamilyType value.
            SerifStyle (int, optional): SerifStyle value.
            Weight (int, optional): Weight value.
            Proportion (int, optional): Proportion value.
            Contrast (int, optional): Contrast value.
            StrokeVariation (int, optional): StrokeVariation value.
            ArmStyle (int, optional): ArmStyle value.
            Letterform (int, optional): Letterform value.
            Midline (int, optional): Midline value.
            XHeight (int, optional): XHeight value.
        """
        super().__init__()

        if isinstance(FamilyType, Panose):
            oth: Panose = FamilyType
            self.FamilyType = oth.FamilyType
            self.SerifStyle = oth.SerifStyle
            self.Weight = oth.Weight
            self.Proportion = oth.Proportion
            self.Contrast = oth.Contrast
            self.StrokeVariation = oth.StrokeVariation
            self.ArmStyle = oth.ArmStyle
            self.Letterform = oth.Letterform
            self.Midline = oth.Midline
            self.XHeight = oth.XHeight
            return

        kargs = {
            "FamilyType": FamilyType,
            "SerifStyle": SerifStyle,
            "Weight": Weight,
            "Proportion": Proportion,
            "Contrast": Contrast,
            "StrokeVariation": StrokeVariation,
            "ArmStyle": ArmStyle,
            "Letterform": Letterform,
            "Midline": Midline,
            "XHeight": XHeight,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._family_type = kwargs["FamilyType"]
        self._serif_style = kwargs["SerifStyle"]
        self._weight = kwargs["Weight"]
        self._proportion = kwargs["Proportion"]
        self._contrast = kwargs["Contrast"]
        self._stroke_variation = kwargs["StrokeVariation"]
        self._arm_style = kwargs["ArmStyle"]
        self._letterform = kwargs["Letterform"]
        self._midline = kwargs["Midline"]
        self._x_height = kwargs["XHeight"]


    @property
    def FamilyType(self) -> int:
        """
        PanoseFamilyTypes.
        """
        return self._family_type

    @FamilyType.setter
    def FamilyType(self, value: int) -> None:
        self._family_type = value

    @property
    def SerifStyle(self) -> int:
        """
        PanoseSerifStyle.
        """
        return self._serif_style

    @SerifStyle.setter
    def SerifStyle(self, value: int) -> None:
        self._serif_style = value

    @property
    def Weight(self) -> int:
        """
        PanoseWeight.
        """
        return self._weight

    @Weight.setter
    def Weight(self, value: int) -> None:
        self._weight = value

    @property
    def Proportion(self) -> int:
        """
        PanoseProportion.
        """
        return self._proportion

    @Proportion.setter
    def Proportion(self, value: int) -> None:
        self._proportion = value

    @property
    def Contrast(self) -> int:
        """
        PanoseContrast.
        """
        return self._contrast

    @Contrast.setter
    def Contrast(self, value: int) -> None:
        self._contrast = value

    @property
    def StrokeVariation(self) -> int:
        """
        PanoseStrokeVariation.
        """
        return self._stroke_variation

    @StrokeVariation.setter
    def StrokeVariation(self, value: int) -> None:
        self._stroke_variation = value

    @property
    def ArmStyle(self) -> int:
        """
        PanoseArmStyle.
        """
        return self._arm_style

    @ArmStyle.setter
    def ArmStyle(self, value: int) -> None:
        self._arm_style = value

    @property
    def Letterform(self) -> int:
        """
        PanoseLetterForm.
        """
        return self._letterform

    @Letterform.setter
    def Letterform(self, value: int) -> None:
        self._letterform = value

    @property
    def Midline(self) -> int:
        """
        PanoseMidline.
        """
        return self._midline

    @Midline.setter
    def Midline(self, value: int) -> None:
        self._midline = value

    @property
    def XHeight(self) -> int:
        """
        PanoseXHeight.
        """
        return self._x_height

    @XHeight.setter
    def XHeight(self, value: int) -> None:
        self._x_height = value


__all__ = ['Panose']
