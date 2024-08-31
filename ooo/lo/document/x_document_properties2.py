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
# Namespace: com.sun.star.document
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_document_properties import XDocumentProperties as XDocumentProperties_4c31102b

class XDocumentProperties2(XDocumentProperties_4c31102b):
    """
    Extends XDocumentProperties interface to provide additional attributes.
    
    **since**
    
        LibreOffice 24.2

    See Also:
        `API XDocumentProperties2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XDocumentProperties2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XDocumentProperties2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XDocumentProperties2'

    @property
    @abstractmethod
    def Contributor(self) -> typing.Tuple[str, ...]:
        """
        Contributors to the resource (other than the authors).
        """
        ...

    @property
    @abstractmethod
    def Coverage(self) -> str:
        """
        The extent or scope of the resource.
        """
        ...

    @property
    @abstractmethod
    def Identifier(self) -> str:
        """
        Unique identifier of the resource.
        """
        ...

    @property
    @abstractmethod
    def Publisher(self) -> typing.Tuple[str, ...]:
        """
        Entities responsible for making the resource available.
        """
        ...

    @property
    @abstractmethod
    def Relation(self) -> typing.Tuple[str, ...]:
        """
        Relationships to other documents.
        
        Recommended practice is to identify the related resource by means of a URI. If this is not possible or feasible, a string conforming to a formal identification system may be provided.
        """
        ...

    @property
    @abstractmethod
    def Rights(self) -> str:
        """
        Informal rights statement.
        """
        ...

    @property
    @abstractmethod
    def Source(self) -> str:
        """
        Unique identifier of the work from which this resource was derived.
        """
        ...

    @property
    @abstractmethod
    def Type(self) -> str:
        """
        The nature or genre of the resource.
        """
        ...


__all__ = ['XDocumentProperties2']
