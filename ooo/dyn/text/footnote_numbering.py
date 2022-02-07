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
# Namespace: com.sun.star.text
from enum import IntEnum
from ...lo.text.footnote_numbering import FootnoteNumbering as FootnoteNumbering


class FootnoteNumberingEnum(IntEnum):
    """
    Enum of Const Class FootnoteNumbering

    These constants are used to specify the footnote numbering.
    """
    PER_PAGE = FootnoteNumbering.PER_PAGE
    """
    The counter of the automatic footnote numbering restarts each page.
    """
    PER_CHAPTER = FootnoteNumbering.PER_CHAPTER
    """
    The counter of the automatic footnote numbering restarts each chapter.
    """
    PER_DOCUMENT = FootnoteNumbering.PER_DOCUMENT
    """
    The counter of the automatic footnote numbering does not restart.
    """

__all__ = ['FootnoteNumbering', 'FootnoteNumberingEnum']
