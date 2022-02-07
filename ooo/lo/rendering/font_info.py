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
    from .panose import Panose as Panose_a6bc0b2c
    from ..util.tri_state import TriState as TriState_85af09f6


class FontInfo(object):
    """
    Struct Class

    This structure provides information about a specific font.
    
    **since**
    
        OOo 2.0

    See Also:
        `API FontInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1FontInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.FontInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.FontInfo'
    """Literal Constant ``com.sun.star.rendering.FontInfo``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``FontInfo`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``FontInfo``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            FontDescription (Panose, optional): FontDescription value
            FamilyName (str, optional): FamilyName value
            StyleName (str, optional): StyleName value
            UnicodeRanges0 (int, optional): UnicodeRanges0 value
            UnicodeRanges1 (int, optional): UnicodeRanges1 value
            UnicodeRanges2 (int, optional): UnicodeRanges2 value
            UnicodeRanges3 (int, optional): UnicodeRanges3 value
            IsSymbolFont (TriState, optional): IsSymbolFont value
            IsVertical (TriState, optional): IsVertical value
        """
        self._font_description = None
        self._family_name = None
        self._style_name = None
        self._unicode_ranges0 = None
        self._unicode_ranges1 = None
        self._unicode_ranges2 = None
        self._unicode_ranges3 = None
        self._is_symbol_font = None
        self._is_vertical = None

        key_order = ('FontDescription', 'FamilyName', 'StyleName', 'UnicodeRanges0', 'UnicodeRanges1', 'UnicodeRanges2', 'UnicodeRanges3', 'IsSymbolFont', 'IsVertical')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], FontInfo):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("FontInfo.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def FontDescription(self) -> 'Panose_a6bc0b2c':
        """
        The PANOSE font classification.
        
        TODO: Document semantics in Panose.idl
        """
        return self._font_description
    
    @FontDescription.setter
    def FontDescription(self, value: 'Panose_a6bc0b2c') -> None:
        self._font_description = value

    @property
    def FamilyName(self) -> str:
        """
        The name of the font family.
        
        The family name is the one normally associated to a font, such as Times New Roman, Thorndale, Andale or Arial.
        
        Note: outlined fonts are now specified with \"outline\" as part of the family name.
        """
        return self._family_name
    
    @FamilyName.setter
    def FamilyName(self, value: str) -> None:
        self._family_name = value

    @property
    def StyleName(self) -> str:
        """
        The name of the specific font style within its family.
        
        For example, oblique, italic, or narrow.
        """
        return self._style_name
    
    @StyleName.setter
    def StyleName(self, value: str) -> None:
        self._style_name = value

    @property
    def UnicodeRanges0(self) -> int:
        """
        This value specifies which Unicode ranges are supported by this font.
        
        This is to be interpreted as a split-up 128-bit value, see Adobe's OpenType specification for the specific meaning of each bit. UnicodeRanges0 contains the least significant bits, UnicodeRanges3 the most significant ones.
        
        const int128 UNICODE_RANGE_BASIC_LATIN = 1; const int128 UNICODE_RANGE_LATIN_SUPPLEMENT = 2; const int128 UNICODE_RANGE_LATIN_EXTENDED_A = 4; const int128 UNICODE_RANGE_LATIN_EXTENDED_B = 4; ... const int128 UNICODE_RANGE_MASK_LATIN = 1; const int128 UNICODE_RANGE_MASK_CJK = (31<<48) + (3<<55) + (1<<59); const int128 UNICODE_RANGE_MASK_CTL = (1<<11) + (1<<13) + (0x3FFF<<15) + (0x0FFF<<70);
        """
        return self._unicode_ranges0
    
    @UnicodeRanges0.setter
    def UnicodeRanges0(self, value: int) -> None:
        self._unicode_ranges0 = value

    @property
    def UnicodeRanges1(self) -> int:
        return self._unicode_ranges1
    
    @UnicodeRanges1.setter
    def UnicodeRanges1(self, value: int) -> None:
        self._unicode_ranges1 = value

    @property
    def UnicodeRanges2(self) -> int:
        return self._unicode_ranges2
    
    @UnicodeRanges2.setter
    def UnicodeRanges2(self, value: int) -> None:
        self._unicode_ranges2 = value

    @property
    def UnicodeRanges3(self) -> int:
        return self._unicode_ranges3
    
    @UnicodeRanges3.setter
    def UnicodeRanges3(self, value: int) -> None:
        self._unicode_ranges3 = value

    @property
    def IsSymbolFont(self) -> 'TriState_85af09f6':
        """
        Specifies whether the font is a symbol font.
        
        If yes, text written in this symbol font does not have a specified meaning.
        """
        return self._is_symbol_font
    
    @IsSymbolFont.setter
    def IsSymbolFont(self, value: 'TriState_85af09f6') -> None:
        self._is_symbol_font = value

    @property
    def IsVertical(self) -> 'TriState_85af09f6':
        """
        Set to true, if the font is usable for vertical text output.
        
        Vertical fonts have subtle differences to horizontal ones, e.g. rotated or differently shaped glyphs, or special rotated versions of normally upright glyphs (e.g. brackets).
        """
        return self._is_vertical
    
    @IsVertical.setter
    def IsVertical(self, value: 'TriState_85af09f6') -> None:
        self._is_vertical = value


__all__ = ['FontInfo']
