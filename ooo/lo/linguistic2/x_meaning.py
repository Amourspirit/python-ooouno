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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.linguistic2
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XMeaning(XInterface_8f010a43):
    """
    one of the possible meanings for a word.
    
    Represents one of the possible meanings that may be returned from a com.sun.star.linguistic2.XThesaurus.queryMeanings() call and allows for retrieval of its synonyms.

    See Also:
        `API XMeaning <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XMeaning.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XMeaning'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XMeaning'

    @abstractmethod
    def getMeaning(self) -> str:
        """
        """
        ...
    @abstractmethod
    def querySynonyms(self) -> typing.Tuple[str, ...]:
        """
        """
        ...

__all__ = ['XMeaning']

