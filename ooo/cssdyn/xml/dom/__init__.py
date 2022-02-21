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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ....dyn.xml.dom.dom_exception import DOMException as DOMException
except ImportError:
    pass
try:
    from ....dyn.xml.dom.dom_exception_type import DOMExceptionType as DOMExceptionType
except ImportError:
    pass
try:
    from ....dyn.xml.dom.document_builder import DocumentBuilder as DocumentBuilder
except ImportError:
    pass
try:
    from ....dyn.xml.dom.node_type import NodeType as NodeType
except ImportError:
    pass
try:
    from ....dyn.xml.dom.sax_document_builder import SAXDocumentBuilder as SAXDocumentBuilder
except ImportError:
    pass
try:
    from ....dyn.xml.dom.sax_document_builder_state import SAXDocumentBuilderState as SAXDocumentBuilderState
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_attr import XAttr as XAttr
except ImportError:
    pass
try:
    from ....dyn.xml.dom.xcdata_section import XCDATASection as XCDATASection
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_character_data import XCharacterData as XCharacterData
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_comment import XComment as XComment
except ImportError:
    pass
try:
    from ....dyn.xml.dom.xdom_implementation import XDOMImplementation as XDOMImplementation
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_document import XDocument as XDocument
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_document_builder import XDocumentBuilder as XDocumentBuilder
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_document_fragment import XDocumentFragment as XDocumentFragment
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_document_type import XDocumentType as XDocumentType
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_element import XElement as XElement
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_entity import XEntity as XEntity
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_entity_reference import XEntityReference as XEntityReference
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_named_node_map import XNamedNodeMap as XNamedNodeMap
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_node import XNode as XNode
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_node_list import XNodeList as XNodeList
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_notation import XNotation as XNotation
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_processing_instruction import XProcessingInstruction as XProcessingInstruction
except ImportError:
    pass
try:
    from ....dyn.xml.dom.xsax_document_builder import XSAXDocumentBuilder as XSAXDocumentBuilder
except ImportError:
    pass
try:
    from ....dyn.xml.dom.xsax_document_builder2 import XSAXDocumentBuilder2 as XSAXDocumentBuilder2
except ImportError:
    pass
try:
    from ....dyn.xml.dom.x_text import XText as XText
except ImportError:
    pass
