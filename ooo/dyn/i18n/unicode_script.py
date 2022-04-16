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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import uno_enum_class_new
    from com.sun.star.i18n.UnicodeScript import (kAlphabeticPresentation, kArabic, kArabicPresentationA, kArabicPresentationB, kArmenian, kArrow, kBasicLatin, kBengali, kBlockElement, kBopomofo, kBopomofoExtended, kBoxDrawing, kBraillePatterns, kCJKCompatibility, kCJKCompatibilityForm, kCJKCompatibilityIdeograph, kCJKRadicalsSupplement, kCJKSymbolPunctuation, kCJKUnifiedIdeograph, kCJKUnifiedIdeographsExtensionA, kCherokee, kCombiningDiacritical, kCombiningHalfMark, kControlPicture, kCurrencySymbolScript, kCyrillic, kDevanagari, kDingbat, kEnclosedAlphanumeric, kEnclosedCJKLetterMonth, kEthiopic, kGeneralPunctuation, kGeometricShape, kGeorgian, kGreek, kGreekExtended, kGujarati, kGurmukhi, kHalfwidthFullwidthForm, kHangulCompatibilityJamo, kHangulJamo, kHangulSyllable, kHebrew, kHighPrivateUseSurrogate, kHighSurrogate, kHiragana, kIPAExtension, kIdeographicDescriptionCharacters, kKanbun, kKangxiRadicals, kKannada, kKatakana, kKhmer, kLao, kLatin1Supplement, kLatinExtendedA, kLatinExtendedAdditional, kLatinExtendedB, kLetterlikeSymbol, kLowSurrogate, kMalayalam, kMathOperator, kMiscSymbol, kMiscTechnical, kMongolian, kMyanmar, kNoScript, kNumberForm, kOgham, kOpticalCharacter, kOriya, kPrivateUse, kRunic, kScriptCount, kSinhala, kSmallFormVariant, kSpacingModifier, kSuperSubScript, kSymbolCombiningMark, kSyriac, kTamil, kTelugu, kThaana, kThai, kTibetan, kUnifiedCanadianAboriginalSyllabics, kYiRadicals, kYiSyllables)

    def _get_enum():
        # Dynamically create class that actually contains UNO enum instances
        _dict = {
            "__doc__": "Dynamically created class that represents com.sun.star.i18n.UnicodeScript Enum. Class loosly mimics Enum",
            "__new__": uno_enum_class_new,
            "__ooo_ns__": "com.sun.star.i18n",
            "__ooo_full_ns__": "com.sun.star.i18n.UnicodeScript",
            "__ooo_type_name__": "enum",
            "kAlphabeticPresentation": kAlphabeticPresentation,
            "kArabic": kArabic,
            "kArabicPresentationA": kArabicPresentationA,
            "kArabicPresentationB": kArabicPresentationB,
            "kArmenian": kArmenian,
            "kArrow": kArrow,
            "kBasicLatin": kBasicLatin,
            "kBengali": kBengali,
            "kBlockElement": kBlockElement,
            "kBopomofo": kBopomofo,
            "kBopomofoExtended": kBopomofoExtended,
            "kBoxDrawing": kBoxDrawing,
            "kBraillePatterns": kBraillePatterns,
            "kCJKCompatibility": kCJKCompatibility,
            "kCJKCompatibilityForm": kCJKCompatibilityForm,
            "kCJKCompatibilityIdeograph": kCJKCompatibilityIdeograph,
            "kCJKRadicalsSupplement": kCJKRadicalsSupplement,
            "kCJKSymbolPunctuation": kCJKSymbolPunctuation,
            "kCJKUnifiedIdeograph": kCJKUnifiedIdeograph,
            "kCJKUnifiedIdeographsExtensionA": kCJKUnifiedIdeographsExtensionA,
            "kCherokee": kCherokee,
            "kCombiningDiacritical": kCombiningDiacritical,
            "kCombiningHalfMark": kCombiningHalfMark,
            "kControlPicture": kControlPicture,
            "kCurrencySymbolScript": kCurrencySymbolScript,
            "kCyrillic": kCyrillic,
            "kDevanagari": kDevanagari,
            "kDingbat": kDingbat,
            "kEnclosedAlphanumeric": kEnclosedAlphanumeric,
            "kEnclosedCJKLetterMonth": kEnclosedCJKLetterMonth,
            "kEthiopic": kEthiopic,
            "kGeneralPunctuation": kGeneralPunctuation,
            "kGeometricShape": kGeometricShape,
            "kGeorgian": kGeorgian,
            "kGreek": kGreek,
            "kGreekExtended": kGreekExtended,
            "kGujarati": kGujarati,
            "kGurmukhi": kGurmukhi,
            "kHalfwidthFullwidthForm": kHalfwidthFullwidthForm,
            "kHangulCompatibilityJamo": kHangulCompatibilityJamo,
            "kHangulJamo": kHangulJamo,
            "kHangulSyllable": kHangulSyllable,
            "kHebrew": kHebrew,
            "kHighPrivateUseSurrogate": kHighPrivateUseSurrogate,
            "kHighSurrogate": kHighSurrogate,
            "kHiragana": kHiragana,
            "kIPAExtension": kIPAExtension,
            "kIdeographicDescriptionCharacters": kIdeographicDescriptionCharacters,
            "kKanbun": kKanbun,
            "kKangxiRadicals": kKangxiRadicals,
            "kKannada": kKannada,
            "kKatakana": kKatakana,
            "kKhmer": kKhmer,
            "kLao": kLao,
            "kLatin1Supplement": kLatin1Supplement,
            "kLatinExtendedA": kLatinExtendedA,
            "kLatinExtendedAdditional": kLatinExtendedAdditional,
            "kLatinExtendedB": kLatinExtendedB,
            "kLetterlikeSymbol": kLetterlikeSymbol,
            "kLowSurrogate": kLowSurrogate,
            "kMalayalam": kMalayalam,
            "kMathOperator": kMathOperator,
            "kMiscSymbol": kMiscSymbol,
            "kMiscTechnical": kMiscTechnical,
            "kMongolian": kMongolian,
            "kMyanmar": kMyanmar,
            "kNoScript": kNoScript,
            "kNumberForm": kNumberForm,
            "kOgham": kOgham,
            "kOpticalCharacter": kOpticalCharacter,
            "kOriya": kOriya,
            "kPrivateUse": kPrivateUse,
            "kRunic": kRunic,
            "kScriptCount": kScriptCount,
            "kSinhala": kSinhala,
            "kSmallFormVariant": kSmallFormVariant,
            "kSpacingModifier": kSpacingModifier,
            "kSuperSubScript": kSuperSubScript,
            "kSymbolCombiningMark": kSymbolCombiningMark,
            "kSyriac": kSyriac,
            "kTamil": kTamil,
            "kTelugu": kTelugu,
            "kThaana": kThaana,
            "kThai": kThai,
            "kTibetan": kTibetan,
            "kUnifiedCanadianAboriginalSyllabics": kUnifiedCanadianAboriginalSyllabics,
            "kYiRadicals": kYiRadicals,
            "kYiSyllables": kYiSyllables,
        }
        result = type('UnicodeScript', (object,), _dict)
        return result

    UnicodeScript = _get_enum()
else:
    from ...lo.i18n.unicode_script import UnicodeScript as UnicodeScript

__all__ = ['UnicodeScript']

