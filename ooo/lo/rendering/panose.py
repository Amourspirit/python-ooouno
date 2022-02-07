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

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``Panose`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``Panose``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            FamilyType (int, optional): FamilyType value
            SerifStyle (int, optional): SerifStyle value
            Weight (int, optional): Weight value
            Proportion (int, optional): Proportion value
            Contrast (int, optional): Contrast value
            StrokeVariation (int, optional): StrokeVariation value
            ArmStyle (int, optional): ArmStyle value
            Letterform (int, optional): Letterform value
            Midline (int, optional): Midline value
            XHeight (int, optional): XHeight value
        """
        self._family_type = None
        self._serif_style = None
        self._weight = None
        self._proportion = None
        self._contrast = None
        self._stroke_variation = None
        self._arm_style = None
        self._letterform = None
        self._midline = None
        self._x_height = None

        key_order = ('FamilyType', 'SerifStyle', 'Weight', 'Proportion', 'Contrast', 'StrokeVariation', 'ArmStyle', 'Letterform', 'Midline', 'XHeight')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], Panose):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("Panose.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


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
