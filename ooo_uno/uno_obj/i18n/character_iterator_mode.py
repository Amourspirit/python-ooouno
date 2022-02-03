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
from enum import IntEnum


class CharacterIteratorMode(object):
    """
    Const Class

    Constants to specify the type of character iteration.
    
    Used with XBreakIterator.nextCharacters() and XBreakIterator.previousCharacters()

    See Also:
        `API CharacterIteratorMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1CharacterIteratorMode.html>`_
    """
    SKIPCHARACTER = 0
    """
    skip characters
    """
    SKIPCELL = 1
    """
    skip cells
    """
    SKIPCONTROLCHARACTER = 2
    """
    skip control characters
    """


class CharacterIteratorModeEnum(IntEnum):
    """
    Enum of Const Class CharacterIteratorMode

    Constants to specify the type of character iteration.
    
    Used with XBreakIterator.nextCharacters() and XBreakIterator.previousCharacters()
    """
    SKIPCHARACTER = CharacterIteratorMode.SKIPCHARACTER
    """
    skip characters
    """
    SKIPCELL = CharacterIteratorMode.SKIPCELL
    """
    skip cells
    """
    SKIPCONTROLCHARACTER = CharacterIteratorMode.SKIPCONTROLCHARACTER
    """
    skip control characters
    """

__all__ = ['CharacterIteratorMode', 'CharacterIteratorModeEnum']
