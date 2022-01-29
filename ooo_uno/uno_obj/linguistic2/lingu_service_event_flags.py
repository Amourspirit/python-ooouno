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
from ooo_uno.base.const import ConstIntBase


class LinguServiceEventFlags(ConstIntBase):
    """
    to be used in lingu-service events.
    
    These values define the flags which may be logically combined to build the event type of a com.sun.star.linguistic2.LinguServiceEvent
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API LinguServiceEventFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1linguistic2_1_1LinguServiceEventFlags.html>`_
    """
    SPELL_CORRECT_WORDS_AGAIN = 1
    """
    The spelling of previously correct words should be checked again.
    """
    SPELL_WRONG_WORDS_AGAIN = 2
    """
    The spelling of previously misspelled words should be checked again.
    """
    HYPHENATE_AGAIN = 4
    """
    The hyphenation of words may have changed.
    """
    PROOFREAD_AGAIN = 8
    """
    Request new proofreading of the document.
    
    **since**
    
        OOo 3.0.1
    """

