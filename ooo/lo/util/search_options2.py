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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from .search_options import SearchOptions as SearchOptions_bd140c08
from .search_algorithms import SearchAlgorithms as SearchAlgorithms_e2c00d36
from ..lang.locale import Locale as Locale_70d308fa
import typing


class SearchOptions2(SearchOptions_bd140c08):
    """
    Struct Class

    This augments com.sun.star.util.SearchOptions to be able to specify additional search algorithms for use with com.sun.star.util.XTextSearch2.
    
    **since**
    
        LibreOffice 5.2

    See Also:
        `API SearchOptions2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1SearchOptions2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.SearchOptions2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.SearchOptions2'
    """Literal Constant ``com.sun.star.util.SearchOptions2``"""

    def __init__(self, algorithmType: typing.Optional[SearchAlgorithms_e2c00d36] = SearchAlgorithms_e2c00d36.ABSOLUTE, searchFlag: typing.Optional[int] = 0, searchString: typing.Optional[str] = '', replaceString: typing.Optional[str] = '', Locale: typing.Optional[Locale_70d308fa] = UNO_NONE, changedChars: typing.Optional[int] = 0, deletedChars: typing.Optional[int] = 0, insertedChars: typing.Optional[int] = 0, transliterateFlags: typing.Optional[int] = 0, AlgorithmType2: typing.Optional[int] = 0, WildcardEscapeCharacter: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            algorithmType (SearchAlgorithms, optional): algorithmType value.
            searchFlag (int, optional): searchFlag value.
            searchString (str, optional): searchString value.
            replaceString (str, optional): replaceString value.
            Locale (Locale, optional): Locale value.
            changedChars (int, optional): changedChars value.
            deletedChars (int, optional): deletedChars value.
            insertedChars (int, optional): insertedChars value.
            transliterateFlags (int, optional): transliterateFlags value.
            AlgorithmType2 (int, optional): AlgorithmType2 value.
            WildcardEscapeCharacter (int, optional): WildcardEscapeCharacter value.
        """

        if isinstance(algorithmType, SearchOptions2):
            oth: SearchOptions2 = algorithmType
            self.algorithmType = oth.algorithmType
            self.searchFlag = oth.searchFlag
            self.searchString = oth.searchString
            self.replaceString = oth.replaceString
            self.Locale = oth.Locale
            self.changedChars = oth.changedChars
            self.deletedChars = oth.deletedChars
            self.insertedChars = oth.insertedChars
            self.transliterateFlags = oth.transliterateFlags
            self.AlgorithmType2 = oth.AlgorithmType2
            self.WildcardEscapeCharacter = oth.WildcardEscapeCharacter
            return

        kargs = {
            "algorithmType": algorithmType,
            "searchFlag": searchFlag,
            "searchString": searchString,
            "replaceString": replaceString,
            "Locale": Locale,
            "changedChars": changedChars,
            "deletedChars": deletedChars,
            "insertedChars": insertedChars,
            "transliterateFlags": transliterateFlags,
            "AlgorithmType2": AlgorithmType2,
            "WildcardEscapeCharacter": WildcardEscapeCharacter,
        }
        if kargs["Locale"] is UNO_NONE:
            kargs["Locale"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._algorithm_type2 = kwargs["AlgorithmType2"]
        self._wildcard_escape_character = kwargs["WildcardEscapeCharacter"]
        inst_keys = ('AlgorithmType2', 'WildcardEscapeCharacter')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def AlgorithmType2(self) -> int:
        """
        Search type, one of com.sun.star.util.SearchAlgorithms2 constants.
        
        This is preferred over the content of the SearchAlgorithms SearchOptions.algorithmType enum field.
        """
        return self._algorithm_type2
    
    @AlgorithmType2.setter
    def AlgorithmType2(self, value: int) -> None:
        self._algorithm_type2 = value

    @property
    def WildcardEscapeCharacter(self) -> int:
        """
        The escape character to be used with a com.sun.star.util.SearchAlgorithms2.WILDCARD search.
        
        A Unicode character, if not 0 escapes the special meaning of a question mark, asterisk or escape character that follows immediately after the escape character. If 0 defines no escape character is used.
        
        Common values are '\\' (U+005C REVERSE SOLIDUS) aka backslash in text processing context, or '~' (U+007E TILDE) in spreadsheet processing context.
        """
        return self._wildcard_escape_character
    
    @WildcardEscapeCharacter.setter
    def WildcardEscapeCharacter(self, value: int) -> None:
        self._wildcard_escape_character = value


__all__ = ['SearchOptions2']
