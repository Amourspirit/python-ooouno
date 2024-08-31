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
    from ....dyn.xml.sax.fast_parser import FastParser as FastParser
with suppress(ImportError):
    from ....dyn.xml.sax.fast_token import FastToken as FastToken
with suppress(ImportError):
    from ....dyn.xml.sax.fast_token import FastTokenEnum as FastTokenEnum
with suppress(ImportError):
    from ....dyn.xml.sax.fast_token_handler import FastTokenHandler as FastTokenHandler
with suppress(ImportError):
    from ....dyn.xml.sax.input_source import InputSource as InputSource
with suppress(ImportError):
    from ....dyn.xml.sax.parser import Parser as Parser
with suppress(ImportError):
    from ....dyn.xml.sax.sax_exception import SAXException as SAXException
with suppress(ImportError):
    from ....dyn.xml.sax.sax_invalid_character_exception import SAXInvalidCharacterException as SAXInvalidCharacterException
with suppress(ImportError):
    from ....dyn.xml.sax.sax_parse_exception import SAXParseException as SAXParseException
with suppress(ImportError):
    from ....dyn.xml.sax.writer import Writer as Writer
with suppress(ImportError):
    from ....dyn.xml.sax.x_attribute_list import XAttributeList as XAttributeList
with suppress(ImportError):
    from ....dyn.xml.sax.xdtd_handler import XDTDHandler as XDTDHandler
with suppress(ImportError):
    from ....dyn.xml.sax.x_document_handler import XDocumentHandler as XDocumentHandler
with suppress(ImportError):
    from ....dyn.xml.sax.x_entity_resolver import XEntityResolver as XEntityResolver
with suppress(ImportError):
    from ....dyn.xml.sax.x_error_handler import XErrorHandler as XErrorHandler
with suppress(ImportError):
    from ....dyn.xml.sax.x_extended_document_handler import XExtendedDocumentHandler as XExtendedDocumentHandler
with suppress(ImportError):
    from ....dyn.xml.sax.x_fast_attribute_list import XFastAttributeList as XFastAttributeList
with suppress(ImportError):
    from ....dyn.xml.sax.x_fast_context_handler import XFastContextHandler as XFastContextHandler
with suppress(ImportError):
    from ....dyn.xml.sax.x_fast_document_handler import XFastDocumentHandler as XFastDocumentHandler
with suppress(ImportError):
    from ....dyn.xml.sax.x_fast_namespace_handler import XFastNamespaceHandler as XFastNamespaceHandler
with suppress(ImportError):
    from ....dyn.xml.sax.x_fast_parser import XFastParser as XFastParser
with suppress(ImportError):
    from ....dyn.xml.sax.x_fast_sax_serializable import XFastSAXSerializable as XFastSAXSerializable
with suppress(ImportError):
    from ....dyn.xml.sax.x_fast_token_handler import XFastTokenHandler as XFastTokenHandler
with suppress(ImportError):
    from ....dyn.xml.sax.x_locator import XLocator as XLocator
with suppress(ImportError):
    from ....dyn.xml.sax.x_parser import XParser as XParser
with suppress(ImportError):
    from ....dyn.xml.sax.xsax_serializable import XSAXSerializable as XSAXSerializable
with suppress(ImportError):
    from ....dyn.xml.sax.x_writer import XWriter as XWriter
