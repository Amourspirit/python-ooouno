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
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class Panose(object):
    """
    Struct Class


    See Also:
        `API Panose <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1Panose.html>`_


    Note:
        | At runtime Panose will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | Panose is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, ArmStyle: typing.Optional[int] = None, Contrast: typing.Optional[int] = None, FamilyType: typing.Optional[int] = None, Letterform: typing.Optional[int] = None, Midline: typing.Optional[int] = None, Proportion: typing.Optional[int] = None, SerifStyle: typing.Optional[int] = None, StrokeVariation: typing.Optional[int] = None, Weight: typing.Optional[int] = None, XHeight: typing.Optional[int] = None):
        self._arm_style = ArmStyle
        self._contrast = Contrast
        self._family_type = FamilyType
        self._letterform = Letterform
        self._midline = Midline
        self._proportion = Proportion
        self._serif_style = SerifStyle
        self._stroke_variation = StrokeVariation
        self._weight = Weight
        self._x_height = XHeight

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
    def Contrast(self) -> int:
        """
        PanoseContrast.
        """
        return self._contrast
    
    @Contrast.setter
    def Contrast(self, value: int) -> None:
        self._contrast = value

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
    def Proportion(self) -> int:
        """
        PanoseProportion.
        """
        return self._proportion
    
    @Proportion.setter
    def Proportion(self, value: int) -> None:
        self._proportion = value

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
    def StrokeVariation(self) -> int:
        """
        PanoseStrokeVariation.
        """
        return self._stroke_variation
    
    @StrokeVariation.setter
    def StrokeVariation(self, value: int) -> None:
        self._stroke_variation = value

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
    def XHeight(self) -> int:
        """
        PanoseXHeight.
        """
        return self._x_height
    
    @XHeight.setter
    def XHeight(self, value: int) -> None:
        self._x_height = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global Panose
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('ArmStyle', 'Contrast', 'FamilyType', 'Letterform', 'Midline', 'Proportion', 'SerifStyle', 'StrokeVariation', 'Weight', 'XHeight')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.rendering.Panose')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        Panose = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['Panose']
