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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from ..linguistic2.x_hyphenated_word import XHyphenatedWord as XHyphenatedWord_3a880f73


class LineBreakResults(object):
    """
    Struct Class

    Results of method XBreakIterator.getLineBreak().

    See Also:
        `API LineBreakResults <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LineBreakResults.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.LineBreakResults'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.LineBreakResults'
    """Literal Constant ``com.sun.star.i18n.LineBreakResults``"""

    def __init__(self, breakType: typing.Optional[int] = 0, breakIndex: typing.Optional[int] = 0, rHyphenatedWord: typing.Optional[XHyphenatedWord_3a880f73] = None) -> None:
        """
        Constructor

        Arguments:
            breakType (int, optional): breakType value.
            breakIndex (int, optional): breakIndex value.
            rHyphenatedWord (XHyphenatedWord, optional): rHyphenatedWord value.
        """
        super().__init__()

        if isinstance(breakType, LineBreakResults):
            oth: LineBreakResults = breakType
            self.breakType = oth.breakType
            self.breakIndex = oth.breakIndex
            self.rHyphenatedWord = oth.rHyphenatedWord
            return

        kargs = {
            "breakType": breakType,
            "breakIndex": breakIndex,
            "rHyphenatedWord": rHyphenatedWord,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._break_type = kwargs["breakType"]
        self._break_index = kwargs["breakIndex"]
        self._r_hyphenated_word = kwargs["rHyphenatedWord"]


    @property
    def breakType(self) -> int:
        """
        Type of line break, see BreakType.
        """
        return self._break_type
    
    @breakType.setter
    def breakType(self, value: int) -> None:
        self._break_type = value

    @property
    def breakIndex(self) -> int:
        """
        Position of the calculated line break.
        """
        return self._break_index
    
    @breakIndex.setter
    def breakIndex(self, value: int) -> None:
        self._break_index = value

    @property
    def rHyphenatedWord(self) -> XHyphenatedWord_3a880f73:
        """
        Return value of the hyphenator.
        """
        return self._r_hyphenated_word
    
    @rHyphenatedWord.setter
    def rHyphenatedWord(self, value: XHyphenatedWord_3a880f73) -> None:
        self._r_hyphenated_word = value


__all__ = ['LineBreakResults']
