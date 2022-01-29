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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class LineBreakUserOptions(object):
    """
    Struct Class

    Line break options passed in calls to XBreakIterator.getLineBreak().

    See Also:
        `API LineBreakUserOptions <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LineBreakUserOptions.html>`_


    Note:
        | At runtime LineBreakUserOptions will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | LineBreakUserOptions is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, allowHyphenateEnglish: typing.Optional[bool] = None, allowPunctuationOutsideMargin: typing.Optional[bool] = None, applyForbiddenRules: typing.Optional[bool] = None, forbiddenBeginCharacters: typing.Optional[str] = None, forbiddenEndCharacters: typing.Optional[str] = None):
        self._allow_hyphenate_english = allowHyphenateEnglish
        self._allow_punctuation_outside_margin = allowPunctuationOutsideMargin
        self._apply_forbidden_rules = applyForbiddenRules
        self._forbidden_begin_characters = forbiddenBeginCharacters
        self._forbidden_end_characters = forbiddenEndCharacters

    @property
    def allowHyphenateEnglish(self) -> bool:
        """
        Allow English hyphenation.
        """
        return self._allow_hyphenate_english
    
    @allowHyphenateEnglish.setter
    def allowHyphenateEnglish(self, value: bool) -> None:
        self._allow_hyphenate_english = value

    @property
    def allowPunctuationOutsideMargin(self) -> bool:
        """
        If punctuation characters are allowed at the end of the line if outside of the margins, resulting in a line not being wrapped if only the punctuation would wrap.
        """
        return self._allow_punctuation_outside_margin
    
    @allowPunctuationOutsideMargin.setter
    def allowPunctuationOutsideMargin(self, value: bool) -> None:
        self._allow_punctuation_outside_margin = value

    @property
    def applyForbiddenRules(self) -> bool:
        """
        If the forbidden characters rules are to be applied or not.
        """
        return self._apply_forbidden_rules
    
    @applyForbiddenRules.setter
    def applyForbiddenRules(self, value: bool) -> None:
        self._apply_forbidden_rules = value

    @property
    def forbiddenBeginCharacters(self) -> str:
        """
        Characters not allowed at the beginning of a line.
        """
        return self._forbidden_begin_characters
    
    @forbiddenBeginCharacters.setter
    def forbiddenBeginCharacters(self, value: str) -> None:
        self._forbidden_begin_characters = value

    @property
    def forbiddenEndCharacters(self) -> str:
        """
        Characters not allowed at the end of a line.
        """
        return self._forbidden_end_characters
    
    @forbiddenEndCharacters.setter
    def forbiddenEndCharacters(self, value: str) -> None:
        self._forbidden_end_characters = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global LineBreakUserOptions
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('allowHyphenateEnglish', 'allowPunctuationOutsideMargin', 'applyForbiddenRules', 'forbiddenBeginCharacters', 'forbiddenEndCharacters')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.i18n.LineBreakUserOptions')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        LineBreakUserOptions = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['LineBreakUserOptions']
