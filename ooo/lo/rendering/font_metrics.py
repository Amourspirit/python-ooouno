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


class FontMetrics(object):
    """
    Struct Class

    Metrics global to the font, i.e.
    
    not specific to single glyphs. The font height is defined as ascent+descent+internalLeading, and therefore not explicitly included here.
    
    Please note that when querying FontMetrics from an XCanvasFont interface, all values here are given relative to the font cell size. That means, the referenceCharWidth and/or ascent+descent+internalLeading will approximately (rounded to integer device resolution, or exactly, if fractional font rendering is enabled) match the referenceAdvancement/cellSize members of the FontRequest for which the XCanvasFont was queried. Please be aware that the values returned in this structure only map one-to-one to device pixel, if the combined rendering transformation for text output equals the identity transformation. Otherwise, the text output (and thus the resulting metrics) will be subject to that transformation. Depending on the underlying font technology, actual device output might be off by up to one device pixel from the transformed metrics.
    
    **since**
    
        OOo 2.0

    See Also:
        `API FontMetrics <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1FontMetrics.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.FontMetrics'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.FontMetrics'
    """Literal Constant ``com.sun.star.rendering.FontMetrics``"""

    def __init__(self, Ascent: typing.Optional[float] = 0.0, Descent: typing.Optional[float] = 0.0, InternalLeading: typing.Optional[float] = 0.0, ExternalLeading: typing.Optional[float] = 0.0, ReferenceCharSize: typing.Optional[float] = 0.0, UnderlineOffset: typing.Optional[float] = 0.0, StrikeThroughOffset: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            Ascent (float, optional): Ascent value.
            Descent (float, optional): Descent value.
            InternalLeading (float, optional): InternalLeading value.
            ExternalLeading (float, optional): ExternalLeading value.
            ReferenceCharSize (float, optional): ReferenceCharSize value.
            UnderlineOffset (float, optional): UnderlineOffset value.
            StrikeThroughOffset (float, optional): StrikeThroughOffset value.
        """
        super().__init__()

        if isinstance(Ascent, FontMetrics):
            oth: FontMetrics = Ascent
            self.Ascent = oth.Ascent
            self.Descent = oth.Descent
            self.InternalLeading = oth.InternalLeading
            self.ExternalLeading = oth.ExternalLeading
            self.ReferenceCharSize = oth.ReferenceCharSize
            self.UnderlineOffset = oth.UnderlineOffset
            self.StrikeThroughOffset = oth.StrikeThroughOffset
            return

        kargs = {
            "Ascent": Ascent,
            "Descent": Descent,
            "InternalLeading": InternalLeading,
            "ExternalLeading": ExternalLeading,
            "ReferenceCharSize": ReferenceCharSize,
            "UnderlineOffset": UnderlineOffset,
            "StrikeThroughOffset": StrikeThroughOffset,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._ascent = kwargs["Ascent"]
        self._descent = kwargs["Descent"]
        self._internal_leading = kwargs["InternalLeading"]
        self._external_leading = kwargs["ExternalLeading"]
        self._reference_char_size = kwargs["ReferenceCharSize"]
        self._underline_offset = kwargs["UnderlineOffset"]
        self._strike_through_offset = kwargs["StrikeThroughOffset"]


    @property
    def Ascent(self) -> float:
        """
        Ascent (above the baseline) part of the font.
        """
        return self._ascent

    @Ascent.setter
    def Ascent(self, value: float) -> None:
        self._ascent = value

    @property
    def Descent(self) -> float:
        """
        Descent (below the baseline) part of the font.
        """
        return self._descent

    @Descent.setter
    def Descent(self, value: float) -> None:
        self._descent = value

    @property
    def InternalLeading(self) -> float:
        """
        Extra space above ascent.
        """
        return self._internal_leading

    @InternalLeading.setter
    def InternalLeading(self, value: float) -> None:
        self._internal_leading = value

    @property
    def ExternalLeading(self) -> float:
        """
        Extra space outside the font cells.
        
        It should not contain ink marks and is typically used by the font designer to modify the line distance.
        """
        return self._external_leading

    @ExternalLeading.setter
    def ExternalLeading(self, value: float) -> None:
        self._external_leading = value

    @property
    def ReferenceCharSize(self) -> float:
        """
        This value specifies the reference character width of the font.
        
        It's roughly equivalent to the average width of all characters, and if one needs a font with double character width, the referenceCharSize should be doubled.
        """
        return self._reference_char_size

    @ReferenceCharSize.setter
    def ReferenceCharSize(self, value: float) -> None:
        self._reference_char_size = value

    @property
    def UnderlineOffset(self) -> float:
        """
        Specifies the offset to be added to the baseline when drawing underlined text.
        """
        return self._underline_offset

    @UnderlineOffset.setter
    def UnderlineOffset(self, value: float) -> None:
        self._underline_offset = value

    @property
    def StrikeThroughOffset(self) -> float:
        """
        Specifies the offset to be added to the baseline when striking through the text.
        """
        return self._strike_through_offset

    @StrikeThroughOffset.setter
    def StrikeThroughOffset(self, value: float) -> None:
        self._strike_through_offset = value


__all__ = ['FontMetrics']
