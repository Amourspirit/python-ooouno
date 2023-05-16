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
    from ...dyn.linguistic2.conversion_dictionary import ConversionDictionary as ConversionDictionary
with suppress(ImportError):
    from ...dyn.linguistic2.conversion_dictionary_list import ConversionDictionaryList as ConversionDictionaryList
with suppress(ImportError):
    from ...dyn.linguistic2.conversion_dictionary_type import ConversionDictionaryType as ConversionDictionaryType
with suppress(ImportError):
    from ...dyn.linguistic2.conversion_dictionary_type import ConversionDictionaryTypeEnum as ConversionDictionaryTypeEnum
with suppress(ImportError):
    from ...dyn.linguistic2.conversion_direction import ConversionDirection as ConversionDirection
with suppress(ImportError):
    from ...dyn.linguistic2.conversion_property_type import ConversionPropertyType as ConversionPropertyType
with suppress(ImportError):
    from ...dyn.linguistic2.conversion_property_type import ConversionPropertyTypeEnum as ConversionPropertyTypeEnum
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary import Dictionary as Dictionary
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary_event import DictionaryEvent as DictionaryEvent
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary_event_flags import DictionaryEventFlags as DictionaryEventFlags
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary_event_flags import DictionaryEventFlagsEnum as DictionaryEventFlagsEnum
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary_list import DictionaryList as DictionaryList
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary_list_event import DictionaryListEvent as DictionaryListEvent
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary_list_event_flags import DictionaryListEventFlags as DictionaryListEventFlags
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary_list_event_flags import DictionaryListEventFlagsEnum as DictionaryListEventFlagsEnum
with suppress(ImportError):
    from ...dyn.linguistic2.dictionary_type import DictionaryType as DictionaryType
with suppress(ImportError):
    from ...dyn.linguistic2.hangul_hanja_conversion_dictionary import HangulHanjaConversionDictionary as HangulHanjaConversionDictionary
with suppress(ImportError):
    from ...dyn.linguistic2.hyphenator import Hyphenator as Hyphenator
with suppress(ImportError):
    from ...dyn.linguistic2.language_guessing import LanguageGuessing as LanguageGuessing
with suppress(ImportError):
    from ...dyn.linguistic2.lingu_properties import LinguProperties as LinguProperties
with suppress(ImportError):
    from ...dyn.linguistic2.lingu_service_event import LinguServiceEvent as LinguServiceEvent
with suppress(ImportError):
    from ...dyn.linguistic2.lingu_service_event_flags import LinguServiceEventFlags as LinguServiceEventFlags
with suppress(ImportError):
    from ...dyn.linguistic2.lingu_service_event_flags import LinguServiceEventFlagsEnum as LinguServiceEventFlagsEnum
with suppress(ImportError):
    from ...dyn.linguistic2.lingu_service_manager import LinguServiceManager as LinguServiceManager
with suppress(ImportError):
    from ...dyn.linguistic2.number_text import NumberText as NumberText
with suppress(ImportError):
    from ...dyn.linguistic2.proofreader import Proofreader as Proofreader
with suppress(ImportError):
    from ...dyn.linguistic2.proofreading_iterator import ProofreadingIterator as ProofreadingIterator
with suppress(ImportError):
    from ...dyn.linguistic2.proofreading_result import ProofreadingResult as ProofreadingResult
with suppress(ImportError):
    from ...dyn.linguistic2.single_proofreading_error import SingleProofreadingError as SingleProofreadingError
with suppress(ImportError):
    from ...dyn.linguistic2.spell_checker import SpellChecker as SpellChecker
with suppress(ImportError):
    from ...dyn.linguistic2.spell_failure import SpellFailure as SpellFailure
with suppress(ImportError):
    from ...dyn.linguistic2.spell_failure import SpellFailureEnum as SpellFailureEnum
with suppress(ImportError):
    from ...dyn.linguistic2.thesaurus import Thesaurus as Thesaurus
with suppress(ImportError):
    from ...dyn.linguistic2.x_available_locales import XAvailableLocales as XAvailableLocales
with suppress(ImportError):
    from ...dyn.linguistic2.x_conversion_dictionary import XConversionDictionary as XConversionDictionary
with suppress(ImportError):
    from ...dyn.linguistic2.x_conversion_dictionary_list import XConversionDictionaryList as XConversionDictionaryList
with suppress(ImportError):
    from ...dyn.linguistic2.x_conversion_property_type import XConversionPropertyType as XConversionPropertyType
with suppress(ImportError):
    from ...dyn.linguistic2.x_dictionary import XDictionary as XDictionary
with suppress(ImportError):
    from ...dyn.linguistic2.x_dictionary1 import XDictionary1 as XDictionary1
with suppress(ImportError):
    from ...dyn.linguistic2.x_dictionary_entry import XDictionaryEntry as XDictionaryEntry
with suppress(ImportError):
    from ...dyn.linguistic2.x_dictionary_event_listener import XDictionaryEventListener as XDictionaryEventListener
with suppress(ImportError):
    from ...dyn.linguistic2.x_dictionary_list import XDictionaryList as XDictionaryList
with suppress(ImportError):
    from ...dyn.linguistic2.x_dictionary_list_event_listener import XDictionaryListEventListener as XDictionaryListEventListener
with suppress(ImportError):
    from ...dyn.linguistic2.x_hyphenated_word import XHyphenatedWord as XHyphenatedWord
with suppress(ImportError):
    from ...dyn.linguistic2.x_hyphenator import XHyphenator as XHyphenator
with suppress(ImportError):
    from ...dyn.linguistic2.x_language_guessing import XLanguageGuessing as XLanguageGuessing
with suppress(ImportError):
    from ...dyn.linguistic2.x_lingu_properties import XLinguProperties as XLinguProperties
with suppress(ImportError):
    from ...dyn.linguistic2.x_lingu_service_event_broadcaster import XLinguServiceEventBroadcaster as XLinguServiceEventBroadcaster
with suppress(ImportError):
    from ...dyn.linguistic2.x_lingu_service_event_listener import XLinguServiceEventListener as XLinguServiceEventListener
with suppress(ImportError):
    from ...dyn.linguistic2.x_lingu_service_manager import XLinguServiceManager as XLinguServiceManager
with suppress(ImportError):
    from ...dyn.linguistic2.x_lingu_service_manager2 import XLinguServiceManager2 as XLinguServiceManager2
with suppress(ImportError):
    from ...dyn.linguistic2.x_meaning import XMeaning as XMeaning
with suppress(ImportError):
    from ...dyn.linguistic2.x_number_text import XNumberText as XNumberText
with suppress(ImportError):
    from ...dyn.linguistic2.x_possible_hyphens import XPossibleHyphens as XPossibleHyphens
with suppress(ImportError):
    from ...dyn.linguistic2.x_proofreader import XProofreader as XProofreader
with suppress(ImportError):
    from ...dyn.linguistic2.x_proofreading_iterator import XProofreadingIterator as XProofreadingIterator
with suppress(ImportError):
    from ...dyn.linguistic2.x_searchable_dictionary import XSearchableDictionary as XSearchableDictionary
with suppress(ImportError):
    from ...dyn.linguistic2.x_searchable_dictionary_list import XSearchableDictionaryList as XSearchableDictionaryList
with suppress(ImportError):
    from ...dyn.linguistic2.x_set_spell_alternatives import XSetSpellAlternatives as XSetSpellAlternatives
with suppress(ImportError):
    from ...dyn.linguistic2.x_spell_alternatives import XSpellAlternatives as XSpellAlternatives
with suppress(ImportError):
    from ...dyn.linguistic2.x_spell_checker import XSpellChecker as XSpellChecker
with suppress(ImportError):
    from ...dyn.linguistic2.x_spell_checker1 import XSpellChecker1 as XSpellChecker1
with suppress(ImportError):
    from ...dyn.linguistic2.x_supported_languages import XSupportedLanguages as XSupportedLanguages
with suppress(ImportError):
    from ...dyn.linguistic2.x_supported_locales import XSupportedLocales as XSupportedLocales
with suppress(ImportError):
    from ...dyn.linguistic2.x_thesaurus import XThesaurus as XThesaurus
