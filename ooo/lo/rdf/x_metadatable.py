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
# Namespace: com.sun.star.rdf
import typing
from abc import abstractmethod, abstractproperty
from .xuri import XURI as XURI_5682078c
if typing.TYPE_CHECKING:
    from ..beans.string_pair import StringPair as StringPair_a4bc0b14

class XMetadatable(XURI_5682078c):
    """
    marks an object representing an ODF element that may have RDF meta data attached.
    
    To make using ODF elements as part of RDF statements more convenient, this interface inherits from XURI. The URI is constructed by concatenating the URI of the document, the stream name, a fragment separator, and the XML ID.
    
    Note that using the XURI interface on an instance of XMetadatable may have the side effect of creating a metadata reference for the instance.
    
    **since**
    
        OOo 3.2

    See Also:
        `API XMetadatable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rdf_1_1XMetadatable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rdf'
    __ooo_full_ns__: str = 'com.sun.star.rdf.XMetadatable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rdf.XMetadatable'

    @abstractmethod
    def ensureMetadataReference(self) -> None:
        """
        creates a metadata reference for this object, if necessary.
        
        If this object already has a metadata reference, do nothing; otherwise, create metadata reference with a fresh, unique XML ID and assign it to the MetadataReference attribute.
        """
        ...
    @abstractproperty
    def MetadataReference(self) -> 'StringPair_a4bc0b14':
        """
        a metadata reference, comprising the stream name and the XML ID.
        
        Note that this metadata reference must be unique for the ODF document. This implies that the XML ID part must be unique for every stream. A pair of two empty strings signifies \"no metadata reference\". For example: Pair(\"content.xml\", \"foo-element-1\")
        """
        ...


__all__ = ['XMetadatable']

