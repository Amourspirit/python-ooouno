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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.i18n
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import KParseTokens
else:
    from ...lo.i18n.k_parse_tokens import KParseTokens as KParseTokens


class KParseTokensEnum(IntFlag):
    """
    Enum of Const Class KParseTokens

    These constants specify the characters a name or identifier token to be parsed can have.
    
    They are passed to XCharacterClassification.parseAnyToken() and XCharacterClassification.parsePredefinedToken(). They are also set in the ParseResult.StartFlags and ParseResult.ContFlags.
    
    **since**
    
        LibreOffice 6.2
    """
    ASC_UPALPHA = KParseTokens.ASC_UPALPHA
    """
    ASCII A-Z upper alpha.
    """
    ASC_LOALPHA = KParseTokens.ASC_LOALPHA
    """
    ASCII a-z lower alpha.
    """
    ASC_DIGIT = KParseTokens.ASC_DIGIT
    """
    ASCII 0-9 digit.
    """
    ASC_UNDERSCORE = KParseTokens.ASC_UNDERSCORE
    """
    ASCII '_' underscore.
    """
    ASC_DOLLAR = KParseTokens.ASC_DOLLAR
    """
    ASCII '$' dollar.
    """
    ASC_DOT = KParseTokens.ASC_DOT
    """
    ASCII '.' dot/point.
    """
    ASC_COLON = KParseTokens.ASC_COLON
    """
    ASCII ':' colon.
    """
    ASC_CONTROL = KParseTokens.ASC_CONTROL
    """
    Special value to allow control characters (0x00 < char < 0x20)
    """
    ASC_ANY_BUT_CONTROL = KParseTokens.ASC_ANY_BUT_CONTROL
    """
    Special value to allow anything below 128 except control characters.
    
    Not set in ParseResult.
    """
    ASC_OTHER = KParseTokens.ASC_OTHER
    """
    Additional flag set in ParseResult.StartFlags or ParseResult.ContFlags.
    
    Set if none of the above ASC_... (except ASC_ANY_...) single values match an ASCII character parsed.
    """
    UNI_UPALPHA = KParseTokens.UNI_UPALPHA
    """
    Unicode (above 127) upper case letter.
    """
    UNI_LOALPHA = KParseTokens.UNI_LOALPHA
    """
    Unicode (above 127) lower case letter.
    """
    UNI_DIGIT = KParseTokens.UNI_DIGIT
    """
    Unicode (above 127) decimal digit number.
    """
    UNI_TITLE_ALPHA = KParseTokens.UNI_TITLE_ALPHA
    """
    Unicode (above 127) title case letter.
    """
    UNI_MODIFIER_LETTER = KParseTokens.UNI_MODIFIER_LETTER
    """
    Unicode (above 127) modifier letter.
    """
    UNI_OTHER_LETTER = KParseTokens.UNI_OTHER_LETTER
    """
    Unicode (above 127) other letter.
    """
    UNI_LETTER_NUMBER = KParseTokens.UNI_LETTER_NUMBER
    """
    Unicode (above 127) letter number.
    """
    UNI_OTHER_NUMBER = KParseTokens.UNI_OTHER_NUMBER
    """
    Unicode (above 127) other number.
    """
    GROUP_SEPARATOR_IN_NUMBER = KParseTokens.GROUP_SEPARATOR_IN_NUMBER
    """
    If this bit is set in nContCharFlags parameters, the locale's group separator characters in numbers are accepted and ignored/skipped.
    
    Else a group separator in a number ends the current token. A leading group separator is never accepted. If an accepted group separator was encountered in a number (ParseResult.TokenType is KParseType.ASC_NUMBER or KParseType.UNI_NUMBER) this bit is also set in ParseResult.ContFlags.
    
    NOTE: absence of this bit in nContCharFlags changes the default behaviour that in prior releases accepted numbers with group separators but lead to unexpected results when parsing formula expressions where the user entered a (wrong) separator that happened to be the group separator instead of an intended decimal separator. Usually inline numbers in a formula expression do not contain group separators.
    
    **since**
    
        LibreOffice 6.2
    """
    TWO_DOUBLE_QUOTES_BREAK_STRING = KParseTokens.TWO_DOUBLE_QUOTES_BREAK_STRING
    """
    If this bit is set in nContCharFlags parameters and a string enclosed in double quotes is parsed and two consecutive double quotes are encountered, the string is ended.
    
    If this bit is not set, the two double quotes are parsed as one escaped double quote and string parsing continues. The bit is ignored in nStartCharFlags parameters.
    
    Example:
    \"abc\"\"def\" --> bit not set => abc\"def <br/>
    \"abc\"\"def\" --> bit set => abc
    """
    UNI_OTHER = KParseTokens.UNI_OTHER
    """
    Additional flag set in ParseResult.StartFlags or ParseResult.ContFlags.
    
    Set if none of the above UNI_... single values match a Unicode character parsed.
    """
    IGNORE_LEADING_WS = KParseTokens.IGNORE_LEADING_WS
    """
    Only valid for nStartCharFlags parameter to CharacterClassification.parseAnyToken() and CharacterClassification.parsePredefinedToken(), ignored on nContCharFlags parameter.
    
    Not set in ParseResult.
    """
    ASC_ALPHA = KParseTokens.ASC_ALPHA
    """
    ASCII a-zA-Z lower or upper alpha.
    """
    ASC_ALNUM = KParseTokens.ASC_ALNUM
    """
    ASCII a-zA-Z0-9 alphanumeric.
    """
    UNI_ALPHA = KParseTokens.UNI_ALPHA
    """
    Unicode (above 127) lower or upper or title case alpha.
    """
    UNI_ALNUM = KParseTokens.UNI_ALNUM
    """
    Unicode (above 127) alphanumeric.
    """
    UNI_LETTER = KParseTokens.UNI_LETTER
    """
    Unicode (above 127) alpha or letter.
    """
    UNI_NUMBER = KParseTokens.UNI_NUMBER
    """
    Unicode (above 127) number.
    """
    ANY_ALPHA = KParseTokens.ANY_ALPHA
    """
    any (ASCII or Unicode) alpha
    """
    ANY_DIGIT = KParseTokens.ANY_DIGIT
    """
    any (ASCII or Unicode) digit
    """
    ANY_ALNUM = KParseTokens.ANY_ALNUM
    """
    any (ASCII or Unicode) alphanumeric
    """
    ANY_LETTER = KParseTokens.ANY_LETTER
    """
    any (ASCII or Unicode) letter
    """
    ANY_NUMBER = KParseTokens.ANY_NUMBER
    """
    any (ASCII or Unicode) number
    """
    ANY_LETTER_OR_NUMBER = KParseTokens.ANY_LETTER_OR_NUMBER
    """
    any (ASCII or Unicode) letter or number
    """

__all__ = ['KParseTokens', 'KParseTokensEnum']
