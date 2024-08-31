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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ....dyn.xml.dom.dom_exception import DOMException as DOMException
with suppress(ImportError):
    from ....dyn.xml.dom.dom_exception_type import DOMExceptionType as DOMExceptionType
with suppress(ImportError):
    from ....dyn.xml.dom.document_builder import DocumentBuilder as DocumentBuilder
with suppress(ImportError):
    from ....dyn.xml.dom.node_type import NodeType as NodeType
with suppress(ImportError):
    from ....dyn.xml.dom.sax_document_builder import SAXDocumentBuilder as SAXDocumentBuilder
with suppress(ImportError):
    from ....dyn.xml.dom.sax_document_builder_state import SAXDocumentBuilderState as SAXDocumentBuilderState
with suppress(ImportError):
    from ....dyn.xml.dom.x_attr import XAttr as XAttr
with suppress(ImportError):
    from ....dyn.xml.dom.xcdata_section import XCDATASection as XCDATASection
with suppress(ImportError):
    from ....dyn.xml.dom.x_character_data import XCharacterData as XCharacterData
with suppress(ImportError):
    from ....dyn.xml.dom.x_comment import XComment as XComment
with suppress(ImportError):
    from ....dyn.xml.dom.xdom_implementation import XDOMImplementation as XDOMImplementation
with suppress(ImportError):
    from ....dyn.xml.dom.x_document import XDocument as XDocument
with suppress(ImportError):
    from ....dyn.xml.dom.x_document_builder import XDocumentBuilder as XDocumentBuilder
with suppress(ImportError):
    from ....dyn.xml.dom.x_document_fragment import XDocumentFragment as XDocumentFragment
with suppress(ImportError):
    from ....dyn.xml.dom.x_document_type import XDocumentType as XDocumentType
with suppress(ImportError):
    from ....dyn.xml.dom.x_element import XElement as XElement
with suppress(ImportError):
    from ....dyn.xml.dom.x_entity import XEntity as XEntity
with suppress(ImportError):
    from ....dyn.xml.dom.x_entity_reference import XEntityReference as XEntityReference
with suppress(ImportError):
    from ....dyn.xml.dom.x_named_node_map import XNamedNodeMap as XNamedNodeMap
with suppress(ImportError):
    from ....dyn.xml.dom.x_node import XNode as XNode
with suppress(ImportError):
    from ....dyn.xml.dom.x_node_list import XNodeList as XNodeList
with suppress(ImportError):
    from ....dyn.xml.dom.x_notation import XNotation as XNotation
with suppress(ImportError):
    from ....dyn.xml.dom.x_processing_instruction import XProcessingInstruction as XProcessingInstruction
with suppress(ImportError):
    from ....dyn.xml.dom.xsax_document_builder import XSAXDocumentBuilder as XSAXDocumentBuilder
with suppress(ImportError):
    from ....dyn.xml.dom.xsax_document_builder2 import XSAXDocumentBuilder2 as XSAXDocumentBuilder2
with suppress(ImportError):
    from ....dyn.xml.dom.x_text import XText as XText
