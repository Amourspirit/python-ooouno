# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.i18n.am_pm_value import AmPmValue as AmPmValue
with suppress(ImportError):
    from ...dyn.i18n.am_pm_value import AmPmValueEnum as AmPmValueEnum
with suppress(ImportError):
    from ...dyn.i18n.boundary import Boundary as Boundary
with suppress(ImportError):
    from ...dyn.i18n.break_iterator import BreakIterator as BreakIterator
with suppress(ImportError):
    from ...dyn.i18n.break_type import BreakType as BreakType
with suppress(ImportError):
    from ...dyn.i18n.break_type import BreakTypeEnum as BreakTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.ctl_script_type import CTLScriptType as CTLScriptType
with suppress(ImportError):
    from ...dyn.i18n.ctl_script_type import CTLScriptTypeEnum as CTLScriptTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.calendar import Calendar as Calendar
with suppress(ImportError):
    from ...dyn.i18n.calendar2 import Calendar2 as Calendar2
with suppress(ImportError):
    from ...dyn.i18n.calendar_display_code import CalendarDisplayCode as CalendarDisplayCode
with suppress(ImportError):
    from ...dyn.i18n.calendar_display_code import CalendarDisplayCodeEnum as CalendarDisplayCodeEnum
with suppress(ImportError):
    from ...dyn.i18n.calendar_display_index import CalendarDisplayIndex as CalendarDisplayIndex
with suppress(ImportError):
    from ...dyn.i18n.calendar_display_index import CalendarDisplayIndexEnum as CalendarDisplayIndexEnum
with suppress(ImportError):
    from ...dyn.i18n.calendar_field_index import CalendarFieldIndex as CalendarFieldIndex
with suppress(ImportError):
    from ...dyn.i18n.calendar_field_index import CalendarFieldIndexEnum as CalendarFieldIndexEnum
with suppress(ImportError):
    from ...dyn.i18n.calendar_item import CalendarItem as CalendarItem
with suppress(ImportError):
    from ...dyn.i18n.calendar_item2 import CalendarItem2 as CalendarItem2
with suppress(ImportError):
    from ...dyn.i18n.chapter_collator import ChapterCollator as ChapterCollator
with suppress(ImportError):
    from ...dyn.i18n.char_type import CharType as CharType
with suppress(ImportError):
    from ...dyn.i18n.char_type import CharTypeEnum as CharTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.character_classification import CharacterClassification as CharacterClassification
with suppress(ImportError):
    from ...dyn.i18n.character_iterator_mode import CharacterIteratorMode as CharacterIteratorMode
with suppress(ImportError):
    from ...dyn.i18n.character_iterator_mode import CharacterIteratorModeEnum as CharacterIteratorModeEnum
with suppress(ImportError):
    from ...dyn.i18n.collator import Collator as Collator
with suppress(ImportError):
    from ...dyn.i18n.collator_options import CollatorOptions as CollatorOptions
with suppress(ImportError):
    from ...dyn.i18n.collator_options import CollatorOptionsEnum as CollatorOptionsEnum
with suppress(ImportError):
    from ...dyn.i18n.currency import Currency as Currency
with suppress(ImportError):
    from ...dyn.i18n.currency2 import Currency2 as Currency2
with suppress(ImportError):
    from ...dyn.i18n.direction_property import DirectionProperty as DirectionProperty
with suppress(ImportError):
    from ...dyn.i18n.forbidden_characters import ForbiddenCharacters as ForbiddenCharacters
with suppress(ImportError):
    from ...dyn.i18n.format_element import FormatElement as FormatElement
with suppress(ImportError):
    from ...dyn.i18n.implementation import Implementation as Implementation
with suppress(ImportError):
    from ...dyn.i18n.index_entry_supplier import IndexEntrySupplier as IndexEntrySupplier
with suppress(ImportError):
    from ...dyn.i18n.input_sequence_check_mode import InputSequenceCheckMode as InputSequenceCheckMode
with suppress(ImportError):
    from ...dyn.i18n.input_sequence_check_mode import InputSequenceCheckModeEnum as InputSequenceCheckModeEnum
with suppress(ImportError):
    from ...dyn.i18n.input_sequence_checker import InputSequenceChecker as InputSequenceChecker
with suppress(ImportError):
    from ...dyn.i18n.k_character_type import KCharacterType as KCharacterType
with suppress(ImportError):
    from ...dyn.i18n.k_character_type import KCharacterTypeEnum as KCharacterTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.k_number_format_type import KNumberFormatType as KNumberFormatType
with suppress(ImportError):
    from ...dyn.i18n.k_number_format_type import KNumberFormatTypeEnum as KNumberFormatTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.k_number_format_usage import KNumberFormatUsage as KNumberFormatUsage
with suppress(ImportError):
    from ...dyn.i18n.k_number_format_usage import KNumberFormatUsageEnum as KNumberFormatUsageEnum
with suppress(ImportError):
    from ...dyn.i18n.k_parse_tokens import KParseTokens as KParseTokens
with suppress(ImportError):
    from ...dyn.i18n.k_parse_tokens import KParseTokensEnum as KParseTokensEnum
with suppress(ImportError):
    from ...dyn.i18n.k_parse_type import KParseType as KParseType
with suppress(ImportError):
    from ...dyn.i18n.k_parse_type import KParseTypeEnum as KParseTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.language_country_info import LanguageCountryInfo as LanguageCountryInfo
with suppress(ImportError):
    from ...dyn.i18n.line_break_hyphenation_options import LineBreakHyphenationOptions as LineBreakHyphenationOptions
with suppress(ImportError):
    from ...dyn.i18n.line_break_results import LineBreakResults as LineBreakResults
with suppress(ImportError):
    from ...dyn.i18n.line_break_user_options import LineBreakUserOptions as LineBreakUserOptions
with suppress(ImportError):
    from ...dyn.i18n.locale_calendar import LocaleCalendar as LocaleCalendar
with suppress(ImportError):
    from ...dyn.i18n.locale_calendar2 import LocaleCalendar2 as LocaleCalendar2
with suppress(ImportError):
    from ...dyn.i18n.locale_data import LocaleData as LocaleData
with suppress(ImportError):
    from ...dyn.i18n.locale_data2 import LocaleData2 as LocaleData2
with suppress(ImportError):
    from ...dyn.i18n.locale_data_item import LocaleDataItem as LocaleDataItem
with suppress(ImportError):
    from ...dyn.i18n.locale_data_item2 import LocaleDataItem2 as LocaleDataItem2
with suppress(ImportError):
    from ...dyn.i18n.locale_item import LocaleItem as LocaleItem
with suppress(ImportError):
    from ...dyn.i18n.locale_item import LocaleItemEnum as LocaleItemEnum
with suppress(ImportError):
    from ...dyn.i18n.months import Months as Months
with suppress(ImportError):
    from ...dyn.i18n.months import MonthsEnum as MonthsEnum
with suppress(ImportError):
    from ...dyn.i18n.multiple_chars_output_exception import MultipleCharsOutputException as MultipleCharsOutputException
with suppress(ImportError):
    from ...dyn.i18n.native_number_mode import NativeNumberMode as NativeNumberMode
with suppress(ImportError):
    from ...dyn.i18n.native_number_mode import NativeNumberModeEnum as NativeNumberModeEnum
with suppress(ImportError):
    from ...dyn.i18n.native_number_supplier import NativeNumberSupplier as NativeNumberSupplier
with suppress(ImportError):
    from ...dyn.i18n.native_number_supplier2 import NativeNumberSupplier2 as NativeNumberSupplier2
with suppress(ImportError):
    from ...dyn.i18n.native_number_xml_attributes import NativeNumberXmlAttributes as NativeNumberXmlAttributes
with suppress(ImportError):
    from ...dyn.i18n.native_number_xml_attributes2 import NativeNumberXmlAttributes2 as NativeNumberXmlAttributes2
with suppress(ImportError):
    from ...dyn.i18n.number_format_code import NumberFormatCode as NumberFormatCode
with suppress(ImportError):
    from ...dyn.i18n.number_format_index import NumberFormatIndex as NumberFormatIndex
with suppress(ImportError):
    from ...dyn.i18n.number_format_index import NumberFormatIndexEnum as NumberFormatIndexEnum
with suppress(ImportError):
    from ...dyn.i18n.number_format_mapper import NumberFormatMapper as NumberFormatMapper
with suppress(ImportError):
    from ...dyn.i18n.ordinal_suffix import OrdinalSuffix as OrdinalSuffix
with suppress(ImportError):
    from ...dyn.i18n.parse_result import ParseResult as ParseResult
with suppress(ImportError):
    from ...dyn.i18n.script_direction import ScriptDirection as ScriptDirection
with suppress(ImportError):
    from ...dyn.i18n.script_direction import ScriptDirectionEnum as ScriptDirectionEnum
with suppress(ImportError):
    from ...dyn.i18n.script_type import ScriptType as ScriptType
with suppress(ImportError):
    from ...dyn.i18n.script_type import ScriptTypeEnum as ScriptTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.text_conversion import TextConversion as TextConversion
with suppress(ImportError):
    from ...dyn.i18n.text_conversion_option import TextConversionOption as TextConversionOption
with suppress(ImportError):
    from ...dyn.i18n.text_conversion_option import TextConversionOptionEnum as TextConversionOptionEnum
with suppress(ImportError):
    from ...dyn.i18n.text_conversion_result import TextConversionResult as TextConversionResult
with suppress(ImportError):
    from ...dyn.i18n.text_conversion_type import TextConversionType as TextConversionType
with suppress(ImportError):
    from ...dyn.i18n.text_conversion_type import TextConversionTypeEnum as TextConversionTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.transliteration import Transliteration as Transliteration
with suppress(ImportError):
    from ...dyn.i18n.transliteration_modules import TransliterationModules as TransliterationModules
with suppress(ImportError):
    from ...dyn.i18n.transliteration_modules_extra import TransliterationModulesExtra as TransliterationModulesExtra
with suppress(ImportError):
    from ...dyn.i18n.transliteration_modules_extra import TransliterationModulesExtraEnum as TransliterationModulesExtraEnum
with suppress(ImportError):
    from ...dyn.i18n.transliteration_modules_new import TransliterationModulesNew as TransliterationModulesNew
with suppress(ImportError):
    from ...dyn.i18n.transliteration_type import TransliterationType as TransliterationType
with suppress(ImportError):
    from ...dyn.i18n.transliteration_type import TransliterationTypeEnum as TransliterationTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.unicode_script import UnicodeScript as UnicodeScript
with suppress(ImportError):
    from ...dyn.i18n.unicode_type import UnicodeType as UnicodeType
with suppress(ImportError):
    from ...dyn.i18n.unicode_type import UnicodeTypeEnum as UnicodeTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.weekdays import Weekdays as Weekdays
with suppress(ImportError):
    from ...dyn.i18n.weekdays import WeekdaysEnum as WeekdaysEnum
with suppress(ImportError):
    from ...dyn.i18n.word_type import WordType as WordType
with suppress(ImportError):
    from ...dyn.i18n.word_type import WordTypeEnum as WordTypeEnum
with suppress(ImportError):
    from ...dyn.i18n.x_break_iterator import XBreakIterator as XBreakIterator
with suppress(ImportError):
    from ...dyn.i18n.x_calendar import XCalendar as XCalendar
with suppress(ImportError):
    from ...dyn.i18n.x_calendar3 import XCalendar3 as XCalendar3
with suppress(ImportError):
    from ...dyn.i18n.x_calendar4 import XCalendar4 as XCalendar4
with suppress(ImportError):
    from ...dyn.i18n.x_character_classification import XCharacterClassification as XCharacterClassification
with suppress(ImportError):
    from ...dyn.i18n.x_collator import XCollator as XCollator
with suppress(ImportError):
    from ...dyn.i18n.x_extended_calendar import XExtendedCalendar as XExtendedCalendar
with suppress(ImportError):
    from ...dyn.i18n.x_extended_index_entry_supplier import XExtendedIndexEntrySupplier as XExtendedIndexEntrySupplier
with suppress(ImportError):
    from ...dyn.i18n.x_extended_input_sequence_checker import XExtendedInputSequenceChecker as XExtendedInputSequenceChecker
with suppress(ImportError):
    from ...dyn.i18n.x_extended_text_conversion import XExtendedTextConversion as XExtendedTextConversion
with suppress(ImportError):
    from ...dyn.i18n.x_extended_transliteration import XExtendedTransliteration as XExtendedTransliteration
with suppress(ImportError):
    from ...dyn.i18n.x_forbidden_characters import XForbiddenCharacters as XForbiddenCharacters
with suppress(ImportError):
    from ...dyn.i18n.x_index_entry_supplier import XIndexEntrySupplier as XIndexEntrySupplier
with suppress(ImportError):
    from ...dyn.i18n.x_input_sequence_checker import XInputSequenceChecker as XInputSequenceChecker
with suppress(ImportError):
    from ...dyn.i18n.x_locale_data import XLocaleData as XLocaleData
with suppress(ImportError):
    from ...dyn.i18n.x_locale_data2 import XLocaleData2 as XLocaleData2
with suppress(ImportError):
    from ...dyn.i18n.x_locale_data3 import XLocaleData3 as XLocaleData3
with suppress(ImportError):
    from ...dyn.i18n.x_locale_data4 import XLocaleData4 as XLocaleData4
with suppress(ImportError):
    from ...dyn.i18n.x_locale_data5 import XLocaleData5 as XLocaleData5
with suppress(ImportError):
    from ...dyn.i18n.x_native_number_supplier import XNativeNumberSupplier as XNativeNumberSupplier
with suppress(ImportError):
    from ...dyn.i18n.x_native_number_supplier2 import XNativeNumberSupplier2 as XNativeNumberSupplier2
with suppress(ImportError):
    from ...dyn.i18n.x_number_format_code import XNumberFormatCode as XNumberFormatCode
with suppress(ImportError):
    from ...dyn.i18n.x_ordinal_suffix import XOrdinalSuffix as XOrdinalSuffix
with suppress(ImportError):
    from ...dyn.i18n.x_script_type_detector import XScriptTypeDetector as XScriptTypeDetector
with suppress(ImportError):
    from ...dyn.i18n.x_text_conversion import XTextConversion as XTextConversion
with suppress(ImportError):
    from ...dyn.i18n.x_transliteration import XTransliteration as XTransliteration
with suppress(ImportError):
    from ...dyn.i18n.reserved_words import reservedWords as reservedWords
with suppress(ImportError):
    from ...dyn.i18n.reserved_words import reservedWordsEnum as reservedWordsEnum
