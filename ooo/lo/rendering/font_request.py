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
import typing
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from .font_info import FontInfo as FontInfo_bded0be9


class FontRequest(object):
    """
    Struct Class

    This structure contains all information necessary to describe a font to be queried from XCanvas.
    
    Note: Outline fonts are to be requested as a special family, set FontInfo.FamilyName appropriately. Emboss/relief must be emulated by upper layers.
    
    Leave the FontInfo.FamilyName and FontInfo.StyleName empty, if font selection should only happen via the PANOSE description.
    
    **since**
    
        OOo 2.0

    See Also:
        `API FontRequest <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1FontRequest.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.FontRequest'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.FontRequest'
    """Literal Constant ``com.sun.star.rendering.FontRequest``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``FontRequest`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``FontRequest``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            FontDescription (FontInfo, optional): FontDescription value
            CellSize (float, optional): CellSize value
            ReferenceAdvancement (float, optional): ReferenceAdvancement value
            Locale (Locale, optional): Locale value
        """
        self._font_description = None
        self._cell_size = None
        self._reference_advancement = None
        self._locale = None

        key_order = ('FontDescription', 'CellSize', 'ReferenceAdvancement', 'Locale')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], FontRequest):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("FontRequest.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def FontDescription(self) -> 'FontInfo_bded0be9':
        """
        The description of the font.
        
        This member contains the description of the font as returned by the font listing methods.
        """
        return self._font_description
    
    @FontDescription.setter
    def FontDescription(self, value: 'FontInfo_bded0be9') -> None:
        self._font_description = value

    @property
    def CellSize(self) -> float:
        """
        The size of the font in device coordinate space.
        
        This value corresponds to the font height in Western scripts, but is independent of the writing direction (see FontRequest.IsVertical below). That means, the value specified here is always measured orthogonal to the text advancement (height for horizontal writing, and width for vertical writing).
        
        When this value is negative, its absolute value is taken as the character size of the font. If this value is positive, it's taken as the cell size of the font.
        
        This member and the referenceAdvancement member are mutually exclusive, one of them has to be set to 0 (which means don't care).
        
        For distorted fonts, the render transformation must be used. That is, the size specified here corresponds to device pixel only if the combined render transformation during text output equals the identity transform. This also applies to all query methods, for both XCanvasFont and XTextLayout.
        """
        return self._cell_size
    
    @CellSize.setter
    def CellSize(self, value: float) -> None:
        self._cell_size = value

    @property
    def ReferenceAdvancement(self) -> float:
        """
        This value specifies the size of the font in the writing direction (i.e.
        
        width for horizontal writing, and height for vertical writing).
        
        It is equivalent to the referenceCharSize of the FontMetrics structure.
        
        This member and the cellSize member are mutually exclusive, one of them has to be set to 0 (which means don't care). For distorted fonts, the font matrix must be used.
        """
        return self._reference_advancement
    
    @ReferenceAdvancement.setter
    def ReferenceAdvancement(self, value: float) -> None:
        self._reference_advancement = value

    @property
    def Locale(self) -> 'Locale_70d308fa':
        """
        The locale this font should be able to render.
        
        This member supplements the FontInfo.UnicodeRange0 entry with a specific locale; this is e.g. important when selecting between traditional and simplified Chinese is necessary (since the letters have the same Unicode ranges and character values).
        """
        return self._locale
    
    @Locale.setter
    def Locale(self, value: 'Locale_70d308fa') -> None:
        self._locale = value


__all__ = ['FontRequest']
