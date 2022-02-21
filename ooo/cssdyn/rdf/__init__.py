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
    from ...dyn.rdf.blank_node import BlankNode as BlankNode
except ImportError:
    pass
try:
    from ...dyn.rdf.file_format import FileFormat as FileFormat
except ImportError:
    pass
try:
    from ...dyn.rdf.file_format import FileFormatEnum as FileFormatEnum
except ImportError:
    pass
try:
    from ...dyn.rdf.literal import Literal as Literal
except ImportError:
    pass
try:
    from ...dyn.rdf.parse_exception import ParseException as ParseException
except ImportError:
    pass
try:
    from ...dyn.rdf.query_exception import QueryException as QueryException
except ImportError:
    pass
try:
    from ...dyn.rdf.repository import Repository as Repository
except ImportError:
    pass
try:
    from ...dyn.rdf.repository_exception import RepositoryException as RepositoryException
except ImportError:
    pass
try:
    from ...dyn.rdf.statement import Statement as Statement
except ImportError:
    pass
try:
    from ...dyn.rdf.uri import URI as URI
except ImportError:
    pass
try:
    from ...dyn.rdf.ur_is import URIs as URIs
except ImportError:
    pass
try:
    from ...dyn.rdf.ur_is import URIsEnum as URIsEnum
except ImportError:
    pass
try:
    from ...dyn.rdf.x_blank_node import XBlankNode as XBlankNode
except ImportError:
    pass
try:
    from ...dyn.rdf.x_document_metadata_access import XDocumentMetadataAccess as XDocumentMetadataAccess
except ImportError:
    pass
try:
    from ...dyn.rdf.x_document_repository import XDocumentRepository as XDocumentRepository
except ImportError:
    pass
try:
    from ...dyn.rdf.x_literal import XLiteral as XLiteral
except ImportError:
    pass
try:
    from ...dyn.rdf.x_metadatable import XMetadatable as XMetadatable
except ImportError:
    pass
try:
    from ...dyn.rdf.x_named_graph import XNamedGraph as XNamedGraph
except ImportError:
    pass
try:
    from ...dyn.rdf.x_node import XNode as XNode
except ImportError:
    pass
try:
    from ...dyn.rdf.x_query_select_result import XQuerySelectResult as XQuerySelectResult
except ImportError:
    pass
try:
    from ...dyn.rdf.x_reified_statement import XReifiedStatement as XReifiedStatement
except ImportError:
    pass
try:
    from ...dyn.rdf.x_repository import XRepository as XRepository
except ImportError:
    pass
try:
    from ...dyn.rdf.x_repository_supplier import XRepositorySupplier as XRepositorySupplier
except ImportError:
    pass
try:
    from ...dyn.rdf.x_resource import XResource as XResource
except ImportError:
    pass
try:
    from ...dyn.rdf.xuri import XURI as XURI
except ImportError:
    pass
