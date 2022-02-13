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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.i18n
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XIndexEntrySupplier(XInterface_8f010a43):
    """
    supplies information on index entries to generate a \"table of
    alphabetical index\" for a given locale.

    See Also:
        `API XIndexEntrySupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XIndexEntrySupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XIndexEntrySupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XIndexEntrySupplier'

    @abstractmethod
    def getIndexCharacter(self, aIndexEntry: str, aLocale: 'Locale_70d308fa', aSortAlgorithm: str) -> str:
        """
        returns the capital index key for sorting a table of indexes, to a given index entry, to a given com.sun.star.lang.Locale and to a given sort algorithm.
        
        For example, in English locale it returns \"K\" for \"keyboard\"
        """
    @abstractmethod
    def getIndexFollowPageWord(self, bMorePages: bool, aLocale: 'Locale_70d308fa') -> str:
        """
        returns the page number word of an index entry, where one page or more pages are combined to one page number entry, for a given com.sun.star.lang.Locale.
        
        For example, in English locale it returns
        \"p.\" for bMorePages == FALSE
        \"pp.\" for bMorePages == TRUE
        """

__all__ = ['XIndexEntrySupplier']

