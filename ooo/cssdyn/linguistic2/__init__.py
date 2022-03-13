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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ...dyn.linguistic2.conversion_dictionary import ConversionDictionary as ConversionDictionary
except ImportError:
    pass
try:
    from ...dyn.linguistic2.conversion_dictionary_list import ConversionDictionaryList as ConversionDictionaryList
except ImportError:
    pass
try:
    from ...dyn.linguistic2.conversion_dictionary_type import ConversionDictionaryType as ConversionDictionaryType
except ImportError:
    pass
try:
    from ...dyn.linguistic2.conversion_dictionary_type import ConversionDictionaryTypeEnum as ConversionDictionaryTypeEnum
except ImportError:
    pass
try:
    from ...dyn.linguistic2.conversion_direction import ConversionDirection as ConversionDirection
except ImportError:
    pass
try:
    from ...dyn.linguistic2.conversion_property_type import ConversionPropertyType as ConversionPropertyType
except ImportError:
    pass
try:
    from ...dyn.linguistic2.conversion_property_type import ConversionPropertyTypeEnum as ConversionPropertyTypeEnum
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary import Dictionary as Dictionary
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary_event import DictionaryEvent as DictionaryEvent
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary_event_flags import DictionaryEventFlags as DictionaryEventFlags
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary_event_flags import DictionaryEventFlagsEnum as DictionaryEventFlagsEnum
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary_list import DictionaryList as DictionaryList
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary_list_event import DictionaryListEvent as DictionaryListEvent
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary_list_event_flags import DictionaryListEventFlags as DictionaryListEventFlags
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary_list_event_flags import DictionaryListEventFlagsEnum as DictionaryListEventFlagsEnum
except ImportError:
    pass
try:
    from ...dyn.linguistic2.dictionary_type import DictionaryType as DictionaryType
except ImportError:
    pass
try:
    from ...dyn.linguistic2.hangul_hanja_conversion_dictionary import HangulHanjaConversionDictionary as HangulHanjaConversionDictionary
except ImportError:
    pass
try:
    from ...dyn.linguistic2.hyphenator import Hyphenator as Hyphenator
except ImportError:
    pass
try:
    from ...dyn.linguistic2.language_guessing import LanguageGuessing as LanguageGuessing
except ImportError:
    pass
try:
    from ...dyn.linguistic2.lingu_properties import LinguProperties as LinguProperties
except ImportError:
    pass
try:
    from ...dyn.linguistic2.lingu_service_event import LinguServiceEvent as LinguServiceEvent
except ImportError:
    pass
try:
    from ...dyn.linguistic2.lingu_service_event_flags import LinguServiceEventFlags as LinguServiceEventFlags
except ImportError:
    pass
try:
    from ...dyn.linguistic2.lingu_service_event_flags import LinguServiceEventFlagsEnum as LinguServiceEventFlagsEnum
except ImportError:
    pass
try:
    from ...dyn.linguistic2.lingu_service_manager import LinguServiceManager as LinguServiceManager
except ImportError:
    pass
try:
    from ...dyn.linguistic2.number_text import NumberText as NumberText
except ImportError:
    pass
try:
    from ...dyn.linguistic2.proofreader import Proofreader as Proofreader
except ImportError:
    pass
try:
    from ...dyn.linguistic2.proofreading_iterator import ProofreadingIterator as ProofreadingIterator
except ImportError:
    pass
try:
    from ...dyn.linguistic2.proofreading_result import ProofreadingResult as ProofreadingResult
except ImportError:
    pass
try:
    from ...dyn.linguistic2.single_proofreading_error import SingleProofreadingError as SingleProofreadingError
except ImportError:
    pass
try:
    from ...dyn.linguistic2.spell_checker import SpellChecker as SpellChecker
except ImportError:
    pass
try:
    from ...dyn.linguistic2.spell_failure import SpellFailure as SpellFailure
except ImportError:
    pass
try:
    from ...dyn.linguistic2.spell_failure import SpellFailureEnum as SpellFailureEnum
except ImportError:
    pass
try:
    from ...dyn.linguistic2.thesaurus import Thesaurus as Thesaurus
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_available_locales import XAvailableLocales as XAvailableLocales
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_conversion_dictionary import XConversionDictionary as XConversionDictionary
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_conversion_dictionary_list import XConversionDictionaryList as XConversionDictionaryList
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_conversion_property_type import XConversionPropertyType as XConversionPropertyType
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_dictionary import XDictionary as XDictionary
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_dictionary1 import XDictionary1 as XDictionary1
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_dictionary_entry import XDictionaryEntry as XDictionaryEntry
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_dictionary_event_listener import XDictionaryEventListener as XDictionaryEventListener
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_dictionary_list import XDictionaryList as XDictionaryList
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_dictionary_list_event_listener import XDictionaryListEventListener as XDictionaryListEventListener
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_hyphenated_word import XHyphenatedWord as XHyphenatedWord
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_hyphenator import XHyphenator as XHyphenator
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_language_guessing import XLanguageGuessing as XLanguageGuessing
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_lingu_properties import XLinguProperties as XLinguProperties
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_lingu_service_event_broadcaster import XLinguServiceEventBroadcaster as XLinguServiceEventBroadcaster
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_lingu_service_event_listener import XLinguServiceEventListener as XLinguServiceEventListener
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_lingu_service_manager import XLinguServiceManager as XLinguServiceManager
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_lingu_service_manager2 import XLinguServiceManager2 as XLinguServiceManager2
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_meaning import XMeaning as XMeaning
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_number_text import XNumberText as XNumberText
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_possible_hyphens import XPossibleHyphens as XPossibleHyphens
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_proofreader import XProofreader as XProofreader
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_proofreading_iterator import XProofreadingIterator as XProofreadingIterator
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_searchable_dictionary import XSearchableDictionary as XSearchableDictionary
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_searchable_dictionary_list import XSearchableDictionaryList as XSearchableDictionaryList
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_set_spell_alternatives import XSetSpellAlternatives as XSetSpellAlternatives
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_spell_alternatives import XSpellAlternatives as XSpellAlternatives
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_spell_checker import XSpellChecker as XSpellChecker
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_spell_checker1 import XSpellChecker1 as XSpellChecker1
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_supported_languages import XSupportedLanguages as XSupportedLanguages
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_supported_locales import XSupportedLocales as XSupportedLocales
except ImportError:
    pass
try:
    from ...dyn.linguistic2.x_thesaurus import XThesaurus as XThesaurus
except ImportError:
    pass
