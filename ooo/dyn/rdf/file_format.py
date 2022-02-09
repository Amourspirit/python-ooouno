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
# Namespace: com.sun.star.rdf
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rdf import FileFormat as FileFormat
else:
    from ...lo.rdf.file_format import FileFormat as FileFormat


class FileFormatEnum(IntEnum):
    """
    Enum of Const Class FileFormat

    Constants to specify RDF file formats.
    
    These constants are mainly for use with XRepository.importGraph() and XRepository.exportGraph().
    
    Note that these are integers because UNO IDL does not permit string constants.
    
    **since**
    
        OOo 3.0
    """
    RDF_XML = FileFormat.RDF_XML
    """
    RDF/XML
    """
    N3 = FileFormat.N3
    """
    N3 (Notation-3)
    """
    NTRIPLES = FileFormat.NTRIPLES
    """
    N-Triples
    """
    TRIG = FileFormat.TRIG
    """
    TriG
    """
    TRIX = FileFormat.TRIX
    """
    TriX
    """
    TURTLE = FileFormat.TURTLE
    """
    Turtle
    """

__all__ = ['FileFormat', 'FileFormatEnum']
