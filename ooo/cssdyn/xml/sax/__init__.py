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
    from ....dyn.xml.sax.fast_parser import FastParser as FastParser
except ImportError:
    pass
try:
    from ....dyn.xml.sax.fast_shape_context_handler import FastShapeContextHandler as FastShapeContextHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.fast_token import FastToken as FastToken
except ImportError:
    pass
try:
    from ....dyn.xml.sax.fast_token import FastTokenEnum as FastTokenEnum
except ImportError:
    pass
try:
    from ....dyn.xml.sax.fast_token_handler import FastTokenHandler as FastTokenHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.input_source import InputSource as InputSource
except ImportError:
    pass
try:
    from ....dyn.xml.sax.parser import Parser as Parser
except ImportError:
    pass
try:
    from ....dyn.xml.sax.sax_exception import SAXException as SAXException
except ImportError:
    pass
try:
    from ....dyn.xml.sax.sax_invalid_character_exception import SAXInvalidCharacterException as SAXInvalidCharacterException
except ImportError:
    pass
try:
    from ....dyn.xml.sax.sax_parse_exception import SAXParseException as SAXParseException
except ImportError:
    pass
try:
    from ....dyn.xml.sax.writer import Writer as Writer
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_attribute_list import XAttributeList as XAttributeList
except ImportError:
    pass
try:
    from ....dyn.xml.sax.xdtd_handler import XDTDHandler as XDTDHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_document_handler import XDocumentHandler as XDocumentHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_entity_resolver import XEntityResolver as XEntityResolver
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_error_handler import XErrorHandler as XErrorHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_extended_document_handler import XExtendedDocumentHandler as XExtendedDocumentHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_fast_attribute_list import XFastAttributeList as XFastAttributeList
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_fast_context_handler import XFastContextHandler as XFastContextHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_fast_document_handler import XFastDocumentHandler as XFastDocumentHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_fast_namespace_handler import XFastNamespaceHandler as XFastNamespaceHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_fast_parser import XFastParser as XFastParser
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_fast_sax_serializable import XFastSAXSerializable as XFastSAXSerializable
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_fast_shape_context_handler import XFastShapeContextHandler as XFastShapeContextHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_fast_token_handler import XFastTokenHandler as XFastTokenHandler
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_locator import XLocator as XLocator
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_parser import XParser as XParser
except ImportError:
    pass
try:
    from ....dyn.xml.sax.xsax_serializable import XSAXSerializable as XSAXSerializable
except ImportError:
    pass
try:
    from ....dyn.xml.sax.x_writer import XWriter as XWriter
except ImportError:
    pass
