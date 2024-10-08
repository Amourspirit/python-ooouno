# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import abstractmethod
from .base_index import BaseIndex as BaseIndex_8f0d0a40
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from .x_document_index_mark import XDocumentIndexMark as XDocumentIndexMark_fe490de7

class DocumentIndex(BaseIndex_8f0d0a40):
    """
    Service Class

    specifies service of content indexes within a document.

    See Also:
        `API DocumentIndex <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1DocumentIndex.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.DocumentIndex'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def DocumentIndexMarks(self) -> typing.Tuple[XDocumentIndexMark_fe490de7, ...]:
        """
        contains all index marks that are related to this index.
        """
        ...

    @property
    @abstractmethod
    def IsCaseSensitive(self) -> bool:
        """
        determines if the similarity of index entries is checked case sensitively.
        """
        ...

    @property
    @abstractmethod
    def Locale(self) -> Locale_70d308fa:
        """
        contains the locale of the index.
        """
        ...

    @property
    @abstractmethod
    def MainEntryCharacterStyleName(self) -> str:
        """
        determines the name of the character style that is applied to the number of a page where main index entry is located.
        """
        ...

    @property
    @abstractmethod
    def SortAlgorithm(self) -> str:
        """
        contains the name of the sort algorithm that is used to sort the entries.
        """
        ...

    @property
    @abstractmethod
    def UseAlphabeticalSeparators(self) -> bool:
        """
        determines if alphabetical separators are generated.
        """
        ...

    @property
    @abstractmethod
    def UseCombinedEntries(self) -> bool:
        """
        determines if same entries on different pages are combined into one index entry.
        """
        ...

    @property
    @abstractmethod
    def UseDash(self) -> bool:
        """
        determines if following page numbers are displayed using a dash.
        """
        ...

    @property
    @abstractmethod
    def UseKeyAsEntry(self) -> bool:
        """
        determines if an index entry is generated for each primary/secondary key.
        """
        ...

    @property
    @abstractmethod
    def UsePP(self) -> bool:
        """
        determines if following page numbers are displayed using a \"pp.\".
        """
        ...

    @property
    @abstractmethod
    def UseUpperCase(self) -> bool:
        """
        determines if all entries start with a capital letter.
        """
        ...


__all__ = ['DocumentIndex']

