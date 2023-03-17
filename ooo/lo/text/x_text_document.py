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
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
import typing
from abc import abstractmethod
from ..frame.x_model import XModel as XModel_7a6e095c
if typing.TYPE_CHECKING:
    from .x_text import XText as XText_690408ca

class XTextDocument(XModel_7a6e095c):
    """
    is the main interface of a text document.

    See Also:
        `API XTextDocument <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XTextDocument'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XTextDocument'

    @abstractmethod
    def getText(self) -> 'XText_690408ca':
        """
        This text does not contain texts in TextFrames, or cells of TextTables etc. directly. These are accessible from the contents via X...Supplier (e.g. XTextTablesSupplier).
        """
        ...
    @abstractmethod
    def reformat(self) -> None:
        """
        reformats the contents of the document.
        """
        ...

__all__ = ['XTextDocument']

