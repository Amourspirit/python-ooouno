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
# Libre Office Version: 7.2


class ParseResult(object):
    """
    Struct Class

    Parser results returned by XCharacterClassification.parseAnyToken() and XCharacterClassification.parsePredefinedToken().

    See Also:
        `API ParseResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1ParseResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.ParseResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.ParseResult'
    """Literal Constant ``com.sun.star.i18n.ParseResult``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ParseResult`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ParseResult``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            LeadingWhiteSpace (int, optional): LeadingWhiteSpace value
            EndPos (int, optional): EndPos value
            CharLen (int, optional): CharLen value
            Value (float, optional): Value value
            TokenType (int, optional): TokenType value
            StartFlags (int, optional): StartFlags value
            ContFlags (int, optional): ContFlags value
            DequotedNameOrString (str, optional): DequotedNameOrString value
        """
        self._leading_white_space = None
        self._end_pos = None
        self._char_len = None
        self._value = None
        self._token_type = None
        self._start_flags = None
        self._cont_flags = None
        self._dequoted_name_or_string = None

        key_order = ('LeadingWhiteSpace', 'EndPos', 'CharLen', 'Value', 'TokenType', 'StartFlags', 'ContFlags', 'DequotedNameOrString')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ParseResult):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ParseResult.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def LeadingWhiteSpace(self) -> int:
        """
        Count of ignored leading whitespace, in UTF-16 code units, not Unicode code points.
        """
        return self._leading_white_space
    
    @LeadingWhiteSpace.setter
    def LeadingWhiteSpace(self, value: int) -> None:
        self._leading_white_space = value

    @property
    def EndPos(self) -> int:
        """
        UTF-16 code unit index of first unprocessed character.
        """
        return self._end_pos
    
    @EndPos.setter
    def EndPos(self, value: int) -> None:
        self._end_pos = value

    @property
    def CharLen(self) -> int:
        """
        Number of code points (not UTF-16 code units) of the parsed token, not including leading whitespace.
        """
        return self._char_len
    
    @CharLen.setter
    def CharLen(self, value: int) -> None:
        self._char_len = value

    @property
    def Value(self) -> float:
        """
        Value of token in case of numeric.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: float) -> None:
        self._value = value

    @property
    def TokenType(self) -> int:
        """
        KParseType token type like KParseType.IDENTNAME.
        """
        return self._token_type
    
    @TokenType.setter
    def TokenType(self, value: int) -> None:
        self._token_type = value

    @property
    def StartFlags(self) -> int:
        """
        KParseTokens flags of first character of actual token matched.
        
        If TokenType is a KParseType.SINGLE_QUOTE_NAME or a KParseType.DOUBLE_QUOTE_STRING the first character is the first character inside the quotes, not the quote itself.
        """
        return self._start_flags
    
    @StartFlags.setter
    def StartFlags(self, value: int) -> None:
        self._start_flags = value

    @property
    def ContFlags(self) -> int:
        """
        KParseTokens flags of remaining characters of actual token matched.
        """
        return self._cont_flags
    
    @ContFlags.setter
    def ContFlags(self, value: int) -> None:
        self._cont_flags = value

    @property
    def DequotedNameOrString(self) -> str:
        """
        If a quoted name or string is encountered the dequoted result goes here.
        """
        return self._dequoted_name_or_string
    
    @DequotedNameOrString.setter
    def DequotedNameOrString(self, value: str) -> None:
        self._dequoted_name_or_string = value


__all__ = ['ParseResult']
