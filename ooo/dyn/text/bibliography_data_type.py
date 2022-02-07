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
from ...lo.text.bibliography_data_type import BibliographyDataType as BibliographyDataType


class BibliographyDataTypeEnum(IntEnum):
    """
    Enum of Const Class BibliographyDataType

    These values define the type of bibliographic data like book, journal, magazine, etc.
    """
    ARTICLE = BibliographyDataType.ARTICLE
    """
    An article from a journal or magazine.
    """
    BOOK = BibliographyDataType.BOOK
    """
    A book with an explicit publisher.
    """
    BOOKLET = BibliographyDataType.BOOKLET
    """
    A work that is printed and bound, but without a named publisher or sponsoring institution.
    """
    CONFERENCE = BibliographyDataType.CONFERENCE
    """
    An article in the proceedings of a conference.
    
    This entry is identical to the \"inproceedings\" entry and is included for compatibility with BiBTex.
    """
    INBOOK = BibliographyDataType.INBOOK
    """
    A part of a book, which may be a chapter and/or a range of pages.
    """
    INCOLLECTION = BibliographyDataType.INCOLLECTION
    """
    A part of a book with its own title.
    """
    INPROCEEDINGS = BibliographyDataType.INPROCEEDINGS
    """
    An article in the proceedings of a conference.
    """
    JOURNAL = BibliographyDataType.JOURNAL
    """
    A journal or magazine.
    """
    MANUAL = BibliographyDataType.MANUAL
    """
    Technical documentation.
    """
    MASTERSTHESIS = BibliographyDataType.MASTERSTHESIS
    """
    A Master's thesis.
    """
    MISC = BibliographyDataType.MISC
    """
    This type is used when nothing else seems appropriate.
    """
    PHDTHESIS = BibliographyDataType.PHDTHESIS
    """
    A PhD thesis.
    """
    PROCEEDINGS = BibliographyDataType.PROCEEDINGS
    """
    The proceedings of a conference.
    """
    TECHREPORT = BibliographyDataType.TECHREPORT
    """
    A report published by a school or other institution, usually numbered within a series.
    """
    UNPUBLISHED = BibliographyDataType.UNPUBLISHED
    """
    A document with an author and title, but not formally published.
    """
    EMAIL = BibliographyDataType.EMAIL
    """
    An eMail document.
    """
    WWW = BibliographyDataType.WWW
    """
    A Web document.
    """
    CUSTOM1 = BibliographyDataType.CUSTOM1
    """
    A user defined document type.
    """
    CUSTOM2 = BibliographyDataType.CUSTOM2
    """
    A user defined document type.
    """
    CUSTOM3 = BibliographyDataType.CUSTOM3
    """
    A user defined document type.
    """
    CUSTOM4 = BibliographyDataType.CUSTOM4
    """
    A user defined document type.
    """
    CUSTOM5 = BibliographyDataType.CUSTOM5
    """
    A user defined document type.
    """

__all__ = ['BibliographyDataType', 'BibliographyDataTypeEnum']
