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
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.text import BibliographyDataField as BibliographyDataField
else:
    from ...lo.text.bibliography_data_field import BibliographyDataField as BibliographyDataField


class BibliographyDataFieldEnum(IntEnum):
    """
    Enum of Const Class BibliographyDataField

    These values define parts of bibliographic data.
    
    They are used to create a bibliography in a text document.
    
    Depending on the type of the data some of the fields will usually be left empty.
    """
    IDENTIFIER = BibliographyDataField.IDENTIFIER
    """
    This field contains a unique identifier for the bibliographic data.
    """
    BIBILIOGRAPHIC_TYPE = BibliographyDataField.BIBILIOGRAPHIC_TYPE
    """
    This field contains the type of the bibliographic reference.
    
    It is of the type BibliographyDataType.
    """
    ADDRESS = BibliographyDataField.ADDRESS
    """
    This field contains the address of the publisher.
    """
    ANNOTE = BibliographyDataField.ANNOTE
    """
    This field contains an annotation.
    """
    AUTHOR = BibliographyDataField.AUTHOR
    """
    This field contains the name(s) of the author(s)
    """
    BOOKTITLE = BibliographyDataField.BOOKTITLE
    """
    This field contains the title of the book.
    """
    CHAPTER = BibliographyDataField.CHAPTER
    """
    This field contains the name or number of the chapter.
    """
    EDITION = BibliographyDataField.EDITION
    """
    This field contains the number or name of the edition.
    """
    EDITOR = BibliographyDataField.EDITOR
    """
    This field contains the name(s) of the editor(s)
    """
    HOWPUBLISHED = BibliographyDataField.HOWPUBLISHED
    """
    This field contains a description of the type of the publishing.
    """
    INSTITUTION = BibliographyDataField.INSTITUTION
    """
    This field contains the name of the institution where the publishing was created.
    """
    JOURNAL = BibliographyDataField.JOURNAL
    """
    This field contains the name of the journal.
    """
    MONTH = BibliographyDataField.MONTH
    """
    This field contains number or name of the month of the publishing.
    """
    NOTE = BibliographyDataField.NOTE
    """
    This field contains a note.
    """
    NUMBER = BibliographyDataField.NUMBER
    """
    This field contains the number of the publishing.
    """
    ORGANIZATIONS = BibliographyDataField.ORGANIZATIONS
    """
    This field contains the name of the organizations where the publishing was created.
    """
    PAGES = BibliographyDataField.PAGES
    """
    This field contains the number(s) of the page(s) of the reference into a publishing.
    """
    PUBLISHER = BibliographyDataField.PUBLISHER
    """
    This field contains the name of the publisher.
    """
    SCHOOL = BibliographyDataField.SCHOOL
    """
    This field contains the name of the university or school where the publishing was created.
    """
    SERIES = BibliographyDataField.SERIES
    """
    This field contains the series of the publishing.
    """
    TITLE = BibliographyDataField.TITLE
    """
    This field contains the title of the publishing.
    """
    REPORT_TYPE = BibliographyDataField.REPORT_TYPE
    """
    This field contains a description of the type of the report.
    """
    VOLUME = BibliographyDataField.VOLUME
    """
    This field contains the volume of the publishing.
    """
    YEAR = BibliographyDataField.YEAR
    """
    This field contains the year when the publishing was created.
    """
    URL = BibliographyDataField.URL
    """
    This field contains URL of the publishing.
    """
    CUSTOM1 = BibliographyDataField.CUSTOM1
    """
    This field contains user defined data.
    """
    CUSTOM2 = BibliographyDataField.CUSTOM2
    """
    This field contains user defined data.
    """
    CUSTOM3 = BibliographyDataField.CUSTOM3
    """
    This field contains user defined data.
    """
    CUSTOM4 = BibliographyDataField.CUSTOM4
    """
    This field contains user defined data.
    """
    CUSTOM5 = BibliographyDataField.CUSTOM5
    """
    This field contains user defined data.
    """
    ISBN = BibliographyDataField.ISBN
    """
    This field contains the ISBN data of the publishing.
    """

__all__ = ['BibliographyDataField', 'BibliographyDataFieldEnum']
