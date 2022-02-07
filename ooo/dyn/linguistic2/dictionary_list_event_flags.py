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
# Namespace: com.sun.star.linguistic2
from enum import IntFlag
from ...lo.linguistic2.dictionary_list_event_flags import DictionaryListEventFlags as DictionaryListEventFlags


class DictionaryListEventFlagsEnum(IntFlag):
    """
    Enum of Const Class DictionaryListEventFlags

    constants representing a single dictionary-list event.
    
    These flags define the possible types for a dictionary-list event.
    """
    ADD_POS_ENTRY = DictionaryListEventFlags.ADD_POS_ENTRY
    """
    A positive entry was added to a dictionary from the dictionary list.
    """
    DEL_POS_ENTRY = DictionaryListEventFlags.DEL_POS_ENTRY
    """
    A positive entry was deleted from a dictionary of the dictionary-list or a dictionary with positive entries was cleared.
    """
    ADD_NEG_ENTRY = DictionaryListEventFlags.ADD_NEG_ENTRY
    """
    A negative entry was added to a dictionary from the dictionary-list.
    """
    DEL_NEG_ENTRY = DictionaryListEventFlags.DEL_NEG_ENTRY
    """
    A negative entry was deleted from a dictionary of the dictionary-list or a dictionary with negative entries was cleared.
    """
    ACTIVATE_POS_DIC = DictionaryListEventFlags.ACTIVATE_POS_DIC
    """
    A dictionary with positive entries was activated or has changed its language.
    """
    DEACTIVATE_POS_DIC = DictionaryListEventFlags.DEACTIVATE_POS_DIC
    """
    A dictionary with positive entries was deactivated or has changed its language.
    """
    ACTIVATE_NEG_DIC = DictionaryListEventFlags.ACTIVATE_NEG_DIC
    """
    A dictionary with negative entries was activated or has changed its language.
    """
    DEACTIVATE_NEG_DIC = DictionaryListEventFlags.DEACTIVATE_NEG_DIC
    """
    A dictionary with negative entries was deactivated or has changed its language.
    """

__all__ = ['DictionaryListEventFlags', 'DictionaryListEventFlagsEnum']
