# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.view
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.view.PaperFormat import A3 as PAPER_FORMAT_A3
    from com.sun.star.view.PaperFormat import A4 as PAPER_FORMAT_A4
    from com.sun.star.view.PaperFormat import A5 as PAPER_FORMAT_A5
    from com.sun.star.view.PaperFormat import B4 as PAPER_FORMAT_B4
    from com.sun.star.view.PaperFormat import B5 as PAPER_FORMAT_B5
    from com.sun.star.view.PaperFormat import LEGAL as PAPER_FORMAT_LEGAL
    from com.sun.star.view.PaperFormat import LETTER as PAPER_FORMAT_LETTER
    from com.sun.star.view.PaperFormat import TABLOID as PAPER_FORMAT_TABLOID
    from com.sun.star.view.PaperFormat import USER as PAPER_FORMAT_USER

    class PaperFormat(uno.Enum):
        """
        Enum Class


        See Also:
            `API PaperFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view.html#a12ab04987d08416f8347a9790c7abf3e>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.view.PaperFormat', value)

        __ooo_ns__: str = 'com.sun.star.view'
        __ooo_full_ns__: str = 'com.sun.star.view.PaperFormat'
        __ooo_type_name__: str = 'enum'

        A3: PaperFormat = PAPER_FORMAT_A3
        """
        specifies the paper format as A3.
        """
        A4: PaperFormat = PAPER_FORMAT_A4
        """
        specifies the paper format as A4.
        """
        A5: PaperFormat = PAPER_FORMAT_A5
        """
        specifies the paper format as A5.
        """
        B4: PaperFormat = PAPER_FORMAT_B4
        """
        specifies the paper format as B4.
        """
        B5: PaperFormat = PAPER_FORMAT_B5
        """
        specifies the paper format as B5.
        """
        LEGAL: PaperFormat = PAPER_FORMAT_LEGAL
        """
        specifies the paper format as Legal.
        """
        LETTER: PaperFormat = PAPER_FORMAT_LETTER
        """
        specifies the paper format as Letter.
        """
        TABLOID: PaperFormat = PAPER_FORMAT_TABLOID
        """
        specifies the paper format as Tabloid.
        """
        USER: PaperFormat = PAPER_FORMAT_USER
        """
        The real paper size is user defined in 100th mm.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class PaperFormat(metaclass=UnoEnumMeta, type_name="com.sun.star.view.PaperFormat", name_space="com.sun.star.view"):
        """Dynamically created class that represents ``com.sun.star.view.PaperFormat`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['PaperFormat']
