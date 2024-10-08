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
# Namespace: com.sun.star.formula
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class SymbolDescriptor(object):
    """
    Struct Class

    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API SymbolDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1formula_1_1SymbolDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.formula'
    __ooo_full_ns__: str = 'com.sun.star.formula.SymbolDescriptor'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.formula.SymbolDescriptor'
    """Literal Constant ``com.sun.star.formula.SymbolDescriptor``"""

    def __init__(self, sName: typing.Optional[str] = '', sExportName: typing.Optional[str] = '', sSymbolSet: typing.Optional[str] = '', nCharacter: typing.Optional[int] = 0, sFontName: typing.Optional[str] = '', nCharSet: typing.Optional[int] = 0, nFamily: typing.Optional[int] = 0, nPitch: typing.Optional[int] = 0, nWeight: typing.Optional[int] = 0, nItalic: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            sName (str, optional): sName value.
            sExportName (str, optional): sExportName value.
            sSymbolSet (str, optional): sSymbolSet value.
            nCharacter (int, optional): nCharacter value.
            sFontName (str, optional): sFontName value.
            nCharSet (int, optional): nCharSet value.
            nFamily (int, optional): nFamily value.
            nPitch (int, optional): nPitch value.
            nWeight (int, optional): nWeight value.
            nItalic (int, optional): nItalic value.
        """
        super().__init__()

        if isinstance(sName, SymbolDescriptor):
            oth: SymbolDescriptor = sName
            self.sName = oth.sName
            self.sExportName = oth.sExportName
            self.sSymbolSet = oth.sSymbolSet
            self.nCharacter = oth.nCharacter
            self.sFontName = oth.sFontName
            self.nCharSet = oth.nCharSet
            self.nFamily = oth.nFamily
            self.nPitch = oth.nPitch
            self.nWeight = oth.nWeight
            self.nItalic = oth.nItalic
            return

        kargs = {
            "sName": sName,
            "sExportName": sExportName,
            "sSymbolSet": sSymbolSet,
            "nCharacter": nCharacter,
            "sFontName": sFontName,
            "nCharSet": nCharSet,
            "nFamily": nFamily,
            "nPitch": nPitch,
            "nWeight": nWeight,
            "nItalic": nItalic,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._s_name = kwargs["sName"]
        self._s_export_name = kwargs["sExportName"]
        self._s_symbol_set = kwargs["sSymbolSet"]
        self._n_character = kwargs["nCharacter"]
        self._s_font_name = kwargs["sFontName"]
        self._n_char_set = kwargs["nCharSet"]
        self._n_family = kwargs["nFamily"]
        self._n_pitch = kwargs["nPitch"]
        self._n_weight = kwargs["nWeight"]
        self._n_italic = kwargs["nItalic"]


    @property
    def sName(self) -> str:
        """
        The name of the symbol.
        """
        return self._s_name

    @sName.setter
    def sName(self, value: str) -> None:
        self._s_name = value

    @property
    def sExportName(self) -> str:
        """
        The export name of the symbol.
        """
        return self._s_export_name

    @sExportName.setter
    def sExportName(self, value: str) -> None:
        self._s_export_name = value

    @property
    def sSymbolSet(self) -> str:
        """
        Specifies the name of the symbol set to which this symbol belongs.
        """
        return self._s_symbol_set

    @sSymbolSet.setter
    def sSymbolSet(self, value: str) -> None:
        self._s_symbol_set = value

    @property
    def nCharacter(self) -> int:
        """
        Specifies the Unicode character of the symbol.
        """
        return self._n_character

    @nCharacter.setter
    def nCharacter(self, value: int) -> None:
        self._n_character = value

    @property
    def sFontName(self) -> str:
        """
        Specifies the exact name of the font (\"Arial\", \"Courier\", etc.).
        """
        return self._s_font_name

    @sFontName.setter
    def sFontName(self, value: str) -> None:
        self._s_font_name = value

    @property
    def nCharSet(self) -> int:
        """
        Specifies the character set which is supported by the font.
        """
        return self._n_char_set

    @nCharSet.setter
    def nCharSet(self, value: int) -> None:
        self._n_char_set = value

    @property
    def nFamily(self) -> int:
        """
        Specifies the general style of the font.
        """
        return self._n_family

    @nFamily.setter
    def nFamily(self, value: int) -> None:
        self._n_family = value

    @property
    def nPitch(self) -> int:
        """
        Specifies the pitch of the font.
        """
        return self._n_pitch

    @nPitch.setter
    def nPitch(self, value: int) -> None:
        self._n_pitch = value

    @property
    def nWeight(self) -> int:
        """
        Specifies the thickness of the line.
        
        The allowed integer values correspond as follows: 0 : com.sun.star.awt.FontWeight.DONTKNOW 1 : com.sun.star.awt.FontWeight.THIN 2 : com.sun.star.awt.FontWeight.ULTRALIGHT 3 : com.sun.star.awt.FontWeight.LIGHT 4 : com.sun.star.awt.FontWeight.SEMILIGHT 5 : com.sun.star.awt.FontWeight.NORMAL 7 : com.sun.star.awt.FontWeight.SEMIBOLD 8 : com.sun.star.awt.FontWeight.BOLD 9 : com.sun.star.awt.FontWeight.ULTRABOLD 10 : com.sun.star.awt.FontWeight.BLACK
        """
        return self._n_weight

    @nWeight.setter
    def nWeight(self, value: int) -> None:
        self._n_weight = value

    @property
    def nItalic(self) -> int:
        """
        Specifies if the font is italic.
        
        The values com.sun.star.awt.FontSlant.REVERSE_OBLIQUE and com.sun.star.awt.FontSlant.REVERSE_ITALIC may not be used.
        """
        return self._n_italic

    @nItalic.setter
    def nItalic(self, value: int) -> None:
        self._n_italic = value


__all__ = ['SymbolDescriptor']
