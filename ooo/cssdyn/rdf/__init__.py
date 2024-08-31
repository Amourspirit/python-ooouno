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
    from ...dyn.rdf.blank_node import BlankNode as BlankNode
with suppress(ImportError):
    from ...dyn.rdf.file_format import FileFormat as FileFormat
with suppress(ImportError):
    from ...dyn.rdf.file_format import FileFormatEnum as FileFormatEnum
with suppress(ImportError):
    from ...dyn.rdf.literal import Literal as Literal
with suppress(ImportError):
    from ...dyn.rdf.parse_exception import ParseException as ParseException
with suppress(ImportError):
    from ...dyn.rdf.query_exception import QueryException as QueryException
with suppress(ImportError):
    from ...dyn.rdf.repository import Repository as Repository
with suppress(ImportError):
    from ...dyn.rdf.repository_exception import RepositoryException as RepositoryException
with suppress(ImportError):
    from ...dyn.rdf.statement import Statement as Statement
with suppress(ImportError):
    from ...dyn.rdf.uri import URI as URI
with suppress(ImportError):
    from ...dyn.rdf.ur_is import URIs as URIs
with suppress(ImportError):
    from ...dyn.rdf.ur_is import URIsEnum as URIsEnum
with suppress(ImportError):
    from ...dyn.rdf.x_blank_node import XBlankNode as XBlankNode
with suppress(ImportError):
    from ...dyn.rdf.x_document_metadata_access import XDocumentMetadataAccess as XDocumentMetadataAccess
with suppress(ImportError):
    from ...dyn.rdf.x_document_repository import XDocumentRepository as XDocumentRepository
with suppress(ImportError):
    from ...dyn.rdf.x_literal import XLiteral as XLiteral
with suppress(ImportError):
    from ...dyn.rdf.x_metadatable import XMetadatable as XMetadatable
with suppress(ImportError):
    from ...dyn.rdf.x_named_graph import XNamedGraph as XNamedGraph
with suppress(ImportError):
    from ...dyn.rdf.x_node import XNode as XNode
with suppress(ImportError):
    from ...dyn.rdf.x_query_select_result import XQuerySelectResult as XQuerySelectResult
with suppress(ImportError):
    from ...dyn.rdf.x_reified_statement import XReifiedStatement as XReifiedStatement
with suppress(ImportError):
    from ...dyn.rdf.x_repository import XRepository as XRepository
with suppress(ImportError):
    from ...dyn.rdf.x_repository_supplier import XRepositorySupplier as XRepositorySupplier
with suppress(ImportError):
    from ...dyn.rdf.x_resource import XResource as XResource
with suppress(ImportError):
    from ...dyn.rdf.xuri import XURI as XURI
