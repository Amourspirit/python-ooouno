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


class KParseType(object):
    """
    Const Class

    Constants to specify the type of a parsed token.
    
    Set by XCharacterClassification.parseAnyToken() and XCharacterClassification.parsePredefinedToken() in ParseResult.TokenType.

    See Also:
        `API KParseType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1KParseType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.KParseType'
    __ooo_type_name__: str = 'const'

    ONE_SINGLE_CHAR = 1
    """
    One single character like ! # ; : $ et al.
    """
    BOOLEAN = 2
    """
    A Boolean operator like <, >, <>, =, <=, >=.
    """
    IDENTNAME = 4
    """
    A name matching the conditions passed.
    """
    SINGLE_QUOTE_NAME = 8
    """
    \"A single-quoted name matching the conditions passed ( 'na\\'me' ).\" \"Dequoted name in ParseResult.DequotedNameOrString ( na'me ).\"
    """
    DOUBLE_QUOTE_STRING = 16
    """
    A double-quoted string ( \"str\\\"i\"\"ng\" ).
    
    Dequoted string in ParseResult.DequotedNameOrString ( str\"i\"ng ).
    """
    ASC_NUMBER = 32
    """
    A number where all digits are ASCII characters.
    
    Numerical value in ParseResult.Value.
    """
    UNI_NUMBER = 64
    """
    A number where at least some digits are Unicode (and maybe ASCII) characters.
    
    Numerical value inKParseType ParseResult.Value.
    """
    MISSING_QUOTE = 1073741824
    """
    Set (ored) if SINGLE_QUOTE_NAME or DOUBLE_QUOTE_STRING has no closing quote.
    """
    ANY_NUMBER = ASC_NUMBER | UNI_NUMBER
    """
    Any ASCII or Unicode number.
    """

__all__ = ['KParseType']