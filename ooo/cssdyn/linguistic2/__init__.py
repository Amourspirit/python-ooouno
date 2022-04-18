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
from ...dyn.linguistic2.conversion_dictionary import ConversionDictionary as ConversionDictionary
from ...dyn.linguistic2.conversion_dictionary_list import ConversionDictionaryList as ConversionDictionaryList
from ...dyn.linguistic2.conversion_dictionary_type import ConversionDictionaryType as ConversionDictionaryType
from ...dyn.linguistic2.conversion_dictionary_type import ConversionDictionaryTypeEnum as ConversionDictionaryTypeEnum
from ...dyn.linguistic2.conversion_direction import ConversionDirection as ConversionDirection
from ...dyn.linguistic2.conversion_property_type import ConversionPropertyType as ConversionPropertyType
from ...dyn.linguistic2.conversion_property_type import ConversionPropertyTypeEnum as ConversionPropertyTypeEnum
from ...dyn.linguistic2.dictionary import Dictionary as Dictionary
from ...dyn.linguistic2.dictionary_event import DictionaryEvent as DictionaryEvent
from ...dyn.linguistic2.dictionary_event_flags import DictionaryEventFlags as DictionaryEventFlags
from ...dyn.linguistic2.dictionary_event_flags import DictionaryEventFlagsEnum as DictionaryEventFlagsEnum
from ...dyn.linguistic2.dictionary_list import DictionaryList as DictionaryList
from ...dyn.linguistic2.dictionary_list_event import DictionaryListEvent as DictionaryListEvent
from ...dyn.linguistic2.dictionary_list_event_flags import DictionaryListEventFlags as DictionaryListEventFlags
from ...dyn.linguistic2.dictionary_list_event_flags import DictionaryListEventFlagsEnum as DictionaryListEventFlagsEnum
from ...dyn.linguistic2.dictionary_type import DictionaryType as DictionaryType
from ...dyn.linguistic2.hangul_hanja_conversion_dictionary import HangulHanjaConversionDictionary as HangulHanjaConversionDictionary
from ...dyn.linguistic2.hyphenator import Hyphenator as Hyphenator
from ...dyn.linguistic2.language_guessing import LanguageGuessing as LanguageGuessing
from ...dyn.linguistic2.lingu_properties import LinguProperties as LinguProperties
from ...dyn.linguistic2.lingu_service_event import LinguServiceEvent as LinguServiceEvent
from ...dyn.linguistic2.lingu_service_event_flags import LinguServiceEventFlags as LinguServiceEventFlags
from ...dyn.linguistic2.lingu_service_event_flags import LinguServiceEventFlagsEnum as LinguServiceEventFlagsEnum
from ...dyn.linguistic2.lingu_service_manager import LinguServiceManager as LinguServiceManager
from ...dyn.linguistic2.number_text import NumberText as NumberText
from ...dyn.linguistic2.proofreader import Proofreader as Proofreader
from ...dyn.linguistic2.proofreading_iterator import ProofreadingIterator as ProofreadingIterator
from ...dyn.linguistic2.proofreading_result import ProofreadingResult as ProofreadingResult
from ...dyn.linguistic2.single_proofreading_error import SingleProofreadingError as SingleProofreadingError
from ...dyn.linguistic2.spell_checker import SpellChecker as SpellChecker
from ...dyn.linguistic2.spell_failure import SpellFailure as SpellFailure
from ...dyn.linguistic2.spell_failure import SpellFailureEnum as SpellFailureEnum
from ...dyn.linguistic2.thesaurus import Thesaurus as Thesaurus
from ...dyn.linguistic2.x_available_locales import XAvailableLocales as XAvailableLocales
from ...dyn.linguistic2.x_conversion_dictionary import XConversionDictionary as XConversionDictionary
from ...dyn.linguistic2.x_conversion_dictionary_list import XConversionDictionaryList as XConversionDictionaryList
from ...dyn.linguistic2.x_conversion_property_type import XConversionPropertyType as XConversionPropertyType
from ...dyn.linguistic2.x_dictionary import XDictionary as XDictionary
from ...dyn.linguistic2.x_dictionary1 import XDictionary1 as XDictionary1
from ...dyn.linguistic2.x_dictionary_entry import XDictionaryEntry as XDictionaryEntry
from ...dyn.linguistic2.x_dictionary_event_listener import XDictionaryEventListener as XDictionaryEventListener
from ...dyn.linguistic2.x_dictionary_list import XDictionaryList as XDictionaryList
from ...dyn.linguistic2.x_dictionary_list_event_listener import XDictionaryListEventListener as XDictionaryListEventListener
from ...dyn.linguistic2.x_hyphenated_word import XHyphenatedWord as XHyphenatedWord
from ...dyn.linguistic2.x_hyphenator import XHyphenator as XHyphenator
from ...dyn.linguistic2.x_language_guessing import XLanguageGuessing as XLanguageGuessing
from ...dyn.linguistic2.x_lingu_properties import XLinguProperties as XLinguProperties
from ...dyn.linguistic2.x_lingu_service_event_broadcaster import XLinguServiceEventBroadcaster as XLinguServiceEventBroadcaster
from ...dyn.linguistic2.x_lingu_service_event_listener import XLinguServiceEventListener as XLinguServiceEventListener
from ...dyn.linguistic2.x_lingu_service_manager import XLinguServiceManager as XLinguServiceManager
from ...dyn.linguistic2.x_lingu_service_manager2 import XLinguServiceManager2 as XLinguServiceManager2
from ...dyn.linguistic2.x_meaning import XMeaning as XMeaning
from ...dyn.linguistic2.x_number_text import XNumberText as XNumberText
from ...dyn.linguistic2.x_possible_hyphens import XPossibleHyphens as XPossibleHyphens
from ...dyn.linguistic2.x_proofreader import XProofreader as XProofreader
from ...dyn.linguistic2.x_proofreading_iterator import XProofreadingIterator as XProofreadingIterator
from ...dyn.linguistic2.x_searchable_dictionary import XSearchableDictionary as XSearchableDictionary
from ...dyn.linguistic2.x_searchable_dictionary_list import XSearchableDictionaryList as XSearchableDictionaryList
from ...dyn.linguistic2.x_set_spell_alternatives import XSetSpellAlternatives as XSetSpellAlternatives
from ...dyn.linguistic2.x_spell_alternatives import XSpellAlternatives as XSpellAlternatives
from ...dyn.linguistic2.x_spell_checker import XSpellChecker as XSpellChecker
from ...dyn.linguistic2.x_spell_checker1 import XSpellChecker1 as XSpellChecker1
from ...dyn.linguistic2.x_supported_languages import XSupportedLanguages as XSupportedLanguages
from ...dyn.linguistic2.x_supported_locales import XSupportedLocales as XSupportedLocales
from ...dyn.linguistic2.x_thesaurus import XThesaurus as XThesaurus
