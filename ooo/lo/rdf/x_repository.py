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
# Libre Office Version: 7.2
# Namespace: com.sun.star.rdf
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..container.x_enumeration import XEnumeration as XEnumeration_f2180daa
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_output_stream import XOutputStream as XOutputStream_a4e00b35
    from .x_blank_node import XBlankNode as XBlankNode_8cf40a0a
    from .x_named_graph import XNamedGraph as XNamedGraph_97680a73
    from .x_node import XNode as XNode_5ee40822
    from .x_query_select_result import XQuerySelectResult as XQuerySelectResult_eebb0d91
    from .x_resource import XResource as XResource_842709e4
    from .xuri import XURI as XURI_5682078c

class XRepository(ABC):
    """
    provides access to a set of named RDF graphs.
    
    A repository for storing information according to the data model of the Resource Description Framework. This interface may be used e.g. for repositories that correspond to a loaded ODF document, or for repositories that are backed by some kind of database.
    
    The RDF triples are stored as a set of named RDF graphs. Importing and exporting files in the RDF/XML format is supported. Support for other file formats is optional. Support for querying the repository with the SPARQL query language is provided.
    
    **since**
    
        OOo 3.2

    See Also:
        `API XRepository <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rdf_1_1XRepository.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rdf'
    __ooo_full_ns__: str = 'com.sun.star.rdf.XRepository'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rdf.XRepository'

    @abstractmethod
    def createBlankNode(self) -> 'XBlankNode_8cf40a0a':
        """
        creates a fresh unique blank node.
        """
    @abstractmethod
    def createGraph(self, GraphName: 'XURI_5682078c') -> 'XNamedGraph_97680a73':
        """
        creates a graph with the given name.
        
        The name must be unique within the repository.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            RepositoryException: ``RepositoryException``
        """
    @abstractmethod
    def destroyGraph(self, GraphName: 'XURI_5682078c') -> None:
        """
        destroys the graph with the given name, and removes it from the repository.
        
        This invalidates any instances of XNamedGraph for the argument.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            RepositoryException: ``RepositoryException``
        """
    @abstractmethod
    def exportGraph(self, Format: int, OutStream: 'XOutputStream_a4e00b35', GraphName: 'XURI_5682078c', BaseURI: 'XURI_5682078c') -> None:
        """
        exports a named graph from the repository.
        
        Implementations must support RDF/XML format. Support for other RDF formats is optional. If the format is not supported by the implementation, an com.sun.star.datatransfer.UnsupportedFlavorException is raised.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.datatransfer.UnsupportedFlavorException: ``UnsupportedFlavorException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            RepositoryException: ``RepositoryException``
            com.sun.star.io.IOException: ``IOException``
        """
    @abstractmethod
    def getGraph(self, GraphName: 'XURI_5682078c') -> 'XNamedGraph_97680a73':
        """
        gets a graph by its name.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            RepositoryException: ``RepositoryException``
        """
    @abstractmethod
    def getGraphNames(self) -> 'typing.Tuple[XURI_5682078c, ...]':
        """
        gets the names of all the graphs in the repository.

        Raises:
            RepositoryException: ``RepositoryException``
        """
    @abstractmethod
    def getStatements(self, Subject: 'XResource_842709e4', Predicate: 'XURI_5682078c', Object: 'XNode_5ee40822') -> 'XEnumeration_f2180daa':
        """
        gets matching RDF statements from the repository.
        
        Any parameter may be NULL, which acts as a wildcard. For example, to get all statements about myURI: getStatements(myURI, null, null)

        Raises:
            RepositoryException: ``RepositoryException``
        """
    @abstractmethod
    def importGraph(self, Format: int, InStream: 'XInputStream_98d40ab4', GraphName: 'XURI_5682078c', BaseURI: 'XURI_5682078c') -> 'XNamedGraph_97680a73':
        """
        imports a named graph into the repository.
        
        Implementations must support RDF/XML format. Support for other RDF formats is optional. If the format is not supported by the implementation, an com.sun.star.datatransfer.UnsupportedFlavorException is raised. If the format requires use of a BaseURI, but none is given, an com.sun.star.lang.IllegalArgumentException is raised.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.datatransfer.UnsupportedFlavorException: ``UnsupportedFlavorException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            ParseException: ``ParseException``
            RepositoryException: ``RepositoryException``
            com.sun.star.io.IOException: ``IOException``
        """
    @abstractmethod
    def queryAsk(self, Query: str) -> bool:
        """
        executes a SPARQL \"ASK\" query.
        
        This method runs a SPARQL query that computes a boolean, i.e., a query beginning with \"ASK\".

        Raises:
            QueryException: ``QueryException``
            RepositoryException: ``RepositoryException``
        """
    @abstractmethod
    def queryConstruct(self, Query: str) -> 'XEnumeration_f2180daa':
        """
        executes a SPARQL \"CONSTRUCT\" query.
        
        This method runs a SPARQL query that constructs a result graph, i.e., a query beginning with \"CONSTRUCT\".

        Raises:
            QueryException: ``QueryException``
            RepositoryException: ``RepositoryException``
        """
    @abstractmethod
    def querySelect(self, Query: str) -> 'XQuerySelectResult_eebb0d91':
        """
        executes a SPARQL \"SELECT\" query.
        
        This method runs a SPARQL query that returns a list of variable bindings, i.e., a query beginning with \"SELECT\". The result is basically a (rectangular) table with labeled columns, where individual cells may be NULL.

        Raises:
            QueryException: ``QueryException``
            RepositoryException: ``RepositoryException``
        """

__all__ = ['XRepository']

