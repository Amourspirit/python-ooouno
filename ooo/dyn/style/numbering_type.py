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
# Namespace: com.sun.star.style
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.style import NumberingType
else:
    from ...lo.style.numbering_type import NumberingType as NumberingType


class NumberingTypeEnum(IntEnum):
    """
    Enum of Const Class NumberingType

    These constants are used to specify which numbering style is used.
    
    **since**
    
        LibreOffice 7.0
    """
    CHARS_UPPER_LETTER = NumberingType.CHARS_UPPER_LETTER
    """
    Numbering is put in upper case letters as \"A, B, C, D, ...\".
    """
    CHARS_LOWER_LETTER = NumberingType.CHARS_LOWER_LETTER
    """
    Numbering is in lower case letters as \"a, b, c, e,...\".
    """
    ROMAN_UPPER = NumberingType.ROMAN_UPPER
    """
    Numbering is in Roman numbers with upper case letters as \"I, II, III, IV, ...\".
    """
    ROMAN_LOWER = NumberingType.ROMAN_LOWER
    """
    Numbering is in Roman numbers with lower case letters as \"i, ii, iii, iv, ...\".
    """
    ARABIC = NumberingType.ARABIC
    """
    Numbering is in Arabic numbers as \"1, 2, 3, 4, ...\".
    """
    NUMBER_NONE = NumberingType.NUMBER_NONE
    """
    Numbering is invisible.
    """
    CHAR_SPECIAL = NumberingType.CHAR_SPECIAL
    """
    Use a character from a specified font.
    """
    PAGE_DESCRIPTOR = NumberingType.PAGE_DESCRIPTOR
    """
    Numbering is specified in the page style.
    """
    BITMAP = NumberingType.BITMAP
    """
    Numbering is displayed as a bitmap graphic.
    """
    CHARS_UPPER_LETTER_N = NumberingType.CHARS_UPPER_LETTER_N
    """
    Numbering is put in upper case letters as \"A, B, ..., Y, Z, AA, BB, CC, ...
    
    AAA, ...\".
    """
    CHARS_LOWER_LETTER_N = NumberingType.CHARS_LOWER_LETTER_N
    """
    Numbering is put in lower case letters as \"a, b, ..., y, z, aa, bb, cc, ...
    
    aaa, ...\".
    """
    TRANSLITERATION = NumberingType.TRANSLITERATION
    """
    A transliteration module will be used to produce numbers in Chinese, Japanese, etc.
    """
    NATIVE_NUMBERING = NumberingType.NATIVE_NUMBERING
    """
    The NativeNumberSupplier service will be called to produce numbers in native languages.
    """
    FULLWIDTH_ARABIC = NumberingType.FULLWIDTH_ARABIC
    """
    Numbering for fullwidth Arabic number.
    """
    CIRCLE_NUMBER = NumberingType.CIRCLE_NUMBER
    """
    Bullet for Circle Number.
    """
    NUMBER_LOWER_ZH = NumberingType.NUMBER_LOWER_ZH
    """
    Numbering for Chinese lower case number as \"&#19968;,&#20108;,&#19977;...\".
    """
    NUMBER_UPPER_ZH = NumberingType.NUMBER_UPPER_ZH
    """
    Numbering for Chinese upper case number.
    """
    NUMBER_UPPER_ZH_TW = NumberingType.NUMBER_UPPER_ZH_TW
    """
    Numbering for Traditional Chinese upper case number.
    """
    TIAN_GAN_ZH = NumberingType.TIAN_GAN_ZH
    """
    Bullet for Chinese Tian Gan as \"&#30002;,&#20057;,&#19993;...\".
    """
    DI_ZI_ZH = NumberingType.DI_ZI_ZH
    """
    Bullet for Chinese Di Zi as \"&#23376;,&#19985;,&#23493;...\".
    """
    NUMBER_TRADITIONAL_JA = NumberingType.NUMBER_TRADITIONAL_JA
    """
    Numbering for Japanese traditional number.
    """
    AIU_FULLWIDTH_JA = NumberingType.AIU_FULLWIDTH_JA
    """
    Bullet for Japanese AIU fullwidth.
    """
    AIU_HALFWIDTH_JA = NumberingType.AIU_HALFWIDTH_JA
    """
    Bullet for Japanese AIU halfwidth.
    """
    IROHA_FULLWIDTH_JA = NumberingType.IROHA_FULLWIDTH_JA
    """
    Bullet for Japanese IROHA fullwidth.
    """
    IROHA_HALFWIDTH_JA = NumberingType.IROHA_HALFWIDTH_JA
    """
    Bullet for Japanese IROHA halfwidth.
    """
    NUMBER_UPPER_KO = NumberingType.NUMBER_UPPER_KO
    """
    Numbering for Korean upper case number as \"&#22777;,&#36019;,&#21443;...\".
    """
    NUMBER_HANGUL_KO = NumberingType.NUMBER_HANGUL_KO
    """
    Numbering for Korean Hangul number as \"&#51068;,&#51060;,&#49340;...\".
    """
    HANGUL_JAMO_KO = NumberingType.HANGUL_JAMO_KO
    """
    Bullet for Korean Hangul Jamo as \"&#12593;,&#12596;,&#12599;...\".
    """
    HANGUL_SYLLABLE_KO = NumberingType.HANGUL_SYLLABLE_KO
    """
    Bullet for Korean Hangul Syllable as \"&#44032;,&#45208;,&#45796;...\".
    """
    HANGUL_CIRCLED_JAMO_KO = NumberingType.HANGUL_CIRCLED_JAMO_KO
    """
    Bullet for Korean Hangul Circled Jamo as \"&#12896;,&#12897;,&#12898;...\".
    """
    HANGUL_CIRCLED_SYLLABLE_KO = NumberingType.HANGUL_CIRCLED_SYLLABLE_KO
    """
    Bullet for Korean Hangul Circled Syllable as \"&#12910;,&#12911;,&#12912;...\".
    """
    CHARS_ARABIC = NumberingType.CHARS_ARABIC
    """
    Numbering in Arabic alphabet letters as \"&#1571;,&#1576;,&#1578;...\".
    
    **since**
    
        OOo 1.1.2
    """
    CHARS_THAI = NumberingType.CHARS_THAI
    """
    Numbering in Thai alphabet letters.
    
    **since**
    
        OOo 1.1.2
    """
    CHARS_HEBREW = NumberingType.CHARS_HEBREW
    """
    Numbering in Hebrew alphabet letters.
    
    **since**
    
        OOo 2.0
    """
    CHARS_NEPALI = NumberingType.CHARS_NEPALI
    """
    Numbering in Nepali alphabet letters.
    
    **since**
    
        OOo 2.0.1
    """
    CHARS_KHMER = NumberingType.CHARS_KHMER
    """
    Numbering in Khmer alphabet letters.
    
    **since**
    
        OOo 2.0.1
    """
    CHARS_LAO = NumberingType.CHARS_LAO
    """
    Numbering in Lao alphabet letters.
    
    **since**
    
        OOo 2.0.1
    """
    CHARS_TIBETAN = NumberingType.CHARS_TIBETAN
    """
    Numbering in Tibetan/Dzongkha alphabet letters.
    
    **since**
    
        OOo 2.0.3
    """
    CHARS_CYRILLIC_UPPER_LETTER_BG = NumberingType.CHARS_CYRILLIC_UPPER_LETTER_BG
    """
    Numbering in Cyrillic alphabet upper case letters as \"&#1040;, &#1041;,  &#1042;, &#1043;, ..., &#1070;, &#1071;, &#1040;&#1074;, &#1040;&#1072;, &#1040;&#1074;, ... &#1040;&#1072;&#1072;, &#1040;&#1072;&#1073;\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_LOWER_LETTER_BG = NumberingType.CHARS_CYRILLIC_LOWER_LETTER_BG
    """
    Numbering in Cyrillic alphabet lower case letters as \"&#1072;, &#1073;, &#1074;, &#1075;, ..., &#1102;, &#1103;, &#1072; &#1072;,  &#1072;&#1073;, &#1072;&#1074;, ...  &#1072; &#1072; &#1072;,  &#1072; &#1072;&#1073;\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_UPPER_LETTER_N_BG = NumberingType.CHARS_CYRILLIC_UPPER_LETTER_N_BG
    """
    Numbering in Cyrillic alphabet upper case letters as \"&#1040;, &#1041;, ..., &#1070;, &#1071;, &#1040;&#1072;, &#1041;&#1073;, &#1042;&#1074;, ... &#1040;&#1072;&#1072;, ...\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_LOWER_LETTER_N_BG = NumberingType.CHARS_CYRILLIC_LOWER_LETTER_N_BG
    """
    Numbering in Cyrillic alphabet upper case letters as \"&#1072;, &#1073;, ..., &#1102;, &#1103;, &#1072;&#1072;, &#1073;&#1073;, &#1074;&#1074;, ... &#1072;&#1072;&#1072;, ...\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_UPPER_LETTER_RU = NumberingType.CHARS_CYRILLIC_UPPER_LETTER_RU
    """
    Numbering in Russian Cyrillic alphabet upper case letters as \"&#1040;, &#1041;, &#1042;, &#1043;, ..., &#1070;, &#1071;, &#1040;&#1072;, &#1040;&#1073;, &#1040;&#1074;, ... &#1040;&#1072;&#1072;, &#1040;&#1072;&#1073;\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_LOWER_LETTER_RU = NumberingType.CHARS_CYRILLIC_LOWER_LETTER_RU
    """
    Numbering in Russian Cyrillic alphabet lower case letters as \"&#1072;, &#1073;, &#1074;, &#1075;, ..., &#1102;, &#1103;, &#1072;&#1072;, &#1072;&#1073;, &#1072;&#1074;, ... &#1072;&#1072;&#1072;, &#1072;&#1072;&#1073;\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_UPPER_LETTER_N_RU = NumberingType.CHARS_CYRILLIC_UPPER_LETTER_N_RU
    """
    Numbering in Russian Cyrillic alphabet upper case letters as \"&#1040;, &#1041;, ..., &#1070;, &#1071;, &#1040;&#1072;, &#1041;&#1073;, &#1042;&#1074;, ... &#1040;&#1072;&#1072;, ...\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_LOWER_LETTER_N_RU = NumberingType.CHARS_CYRILLIC_LOWER_LETTER_N_RU
    """
    Numbering in Russian Cyrillic alphabet upper case letters as \"&#1072;, &#1073;, ..., &#1102;, &#1103;, &#1072;&#1072;, &#1073;&#1073;, &#1074;&#1074;, ... &#1072;&#1072;&#1072;, ...\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_PERSIAN = NumberingType.CHARS_PERSIAN
    """
    Numbering in Persian alphabet letters (aa, be, pe, te, ...)
    
    **since**
    
        OOo 2.4
    """
    CHARS_MYANMAR = NumberingType.CHARS_MYANMAR
    """
    Numbering in Myanmar alphabet letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_CYRILLIC_UPPER_LETTER_SR = NumberingType.CHARS_CYRILLIC_UPPER_LETTER_SR
    """
    Numbering in Serbian Cyrillic alphabet upper case letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_CYRILLIC_LOWER_LETTER_SR = NumberingType.CHARS_CYRILLIC_LOWER_LETTER_SR
    """
    Numbering in Russian Serbian alphabet lower case letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_CYRILLIC_UPPER_LETTER_N_SR = NumberingType.CHARS_CYRILLIC_UPPER_LETTER_N_SR
    """
    Numbering in Serbian Cyrillic alphabet upper case letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_CYRILLIC_LOWER_LETTER_N_SR = NumberingType.CHARS_CYRILLIC_LOWER_LETTER_N_SR
    """
    Numbering in Serbian Cyrillic alphabet upper case letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_GREEK_UPPER_LETTER = NumberingType.CHARS_GREEK_UPPER_LETTER
    """
    Numbering in Greek alphabet upper case letters.
    
    **since**
    
        LibreOffice 3.3
    """
    CHARS_GREEK_LOWER_LETTER = NumberingType.CHARS_GREEK_LOWER_LETTER
    """
    Numbering in Greek alphabet lower case letters.
    
    **since**
    
        LibreOffice 3.3
    """
    CHARS_ARABIC_ABJAD = NumberingType.CHARS_ARABIC_ABJAD
    """
    Numbering in Arabic alphabet using abjad sequence.
    
    **since**
    
        LibreOffice 3.5
    """
    CHARS_PERSIAN_WORD = NumberingType.CHARS_PERSIAN_WORD
    """
    Numbering in Persian words.
    
    **since**
    
        LibreOffice 3.5
    """
    NUMBER_HEBREW = NumberingType.NUMBER_HEBREW
    """
    Numbering in Hebrew numerals.
    
    **since**
    
        LibreOffice 5.4
    """
    NUMBER_ARABIC_INDIC = NumberingType.NUMBER_ARABIC_INDIC
    """
    Numbering in Arabic-Indic numerals.
    
    **since**
    
        LibreOffice 6.1
    """
    NUMBER_EAST_ARABIC_INDIC = NumberingType.NUMBER_EAST_ARABIC_INDIC
    """
    Numbering in East Arabic-Indic numerals.
    
    **since**
    
        LibreOffice 6.1
    """
    NUMBER_INDIC_DEVANAGARI = NumberingType.NUMBER_INDIC_DEVANAGARI
    """
    Numbering in Indic Devanagari numerals.
    
    **since**
    
        LibreOffice 6.1
    """
    TEXT_NUMBER = NumberingType.TEXT_NUMBER
    """
    Numbering in ordinal numbers of the language of the text node for example, 1st, 2nd, 3rd...
    
    in English
    
    **since**
    
        LibreOffice 6.1
    """
    TEXT_CARDINAL = NumberingType.TEXT_CARDINAL
    """
    Numbering in cardinal numbers of the language of the text node for example, One, Two, Three...
    
    in English
    
    **since**
    
        LibreOffice 6.1
    """
    TEXT_ORDINAL = NumberingType.TEXT_ORDINAL
    """
    Numbering in ordinal numbers of the language of the text node for example, First, Second, Third...
    
    in English
    
    **since**
    
        LibreOffice 6.1
    """
    SYMBOL_CHICAGO = NumberingType.SYMBOL_CHICAGO
    """
    Footnoting symbols according the University of Chicago style: *, &#2020;, &#2021;, &#00a7;, **, &#2020;&#2020; etc.
    
    **since**
    
        LibreOffice 6.4
    """
    ARABIC_ZERO = NumberingType.ARABIC_ZERO
    """
    Numbering is in Arabic numbers, padded with zero to have a length of at least two, as \"01,
    02, ..., 10, 11, ...\".
    
    **since**
    
        LibreOffice 7.0
    """
    ARABIC_ZERO3 = NumberingType.ARABIC_ZERO3
    """
    Numbering is in Arabic numbers, padded with zero to have a length of at least three, as \"001, 002, ..., 100, 101, ...\".
    
    **since**
    
        LibreOffice 7.0
    """
    ARABIC_ZERO4 = NumberingType.ARABIC_ZERO4
    """
    Numbering is in Arabic numbers, padded with zero to have a length of at least four, as \"0001, 0002, ..., 1000, 1001, ...\".
    
    **since**
    
        LibreOffice 7.0
    """
    ARABIC_ZERO5 = NumberingType.ARABIC_ZERO5
    """
    Numbering is in Arabic numbers, padded with zero to have a length of at least five, as \"00001, 00002, ..., 10000, 10001, ...\".
    
    **since**
    
        LibreOffice 7.0
    """
    SZEKELY_ROVAS = NumberingType.SZEKELY_ROVAS
    """
    Numbering is in Szekely rovas (Old Hungarian) numerals.
    
    **since**
    
        LibreOffice 7.1
    """

__all__ = ['NumberingType', 'NumberingTypeEnum']
