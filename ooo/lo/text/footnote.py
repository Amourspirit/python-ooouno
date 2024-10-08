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
from abc import abstractmethod
from .x_footnote import XFootnote as XFootnote_901e0a73
from .x_text import XText as XText_690408ca

class Footnote(XFootnote_901e0a73, XText_690408ca):
    """
    Service Class

    This service specifies a footnote or an endnote in a TextDocument.

    See Also:
        `API Footnote <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1Footnote.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.Footnote'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def ReferenceId(self) -> int:
        """
        contains an internal identifier for the use as SequenceNumber property in reference fields.
        """
        ...


__all__ = ['Footnote']

