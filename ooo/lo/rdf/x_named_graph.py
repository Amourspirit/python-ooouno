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
# Namespace: com.sun.star.rdf
from __future__ import annotations
import typing
from abc import abstractmethod
from .xuri import XURI as XURI_5682078c
if typing.TYPE_CHECKING:
    from ..container.x_enumeration import XEnumeration as XEnumeration_f2180daa
    from .x_node import XNode as XNode_5ee40822
    from .x_resource import XResource as XResource_842709e4

class XNamedGraph(XURI_5682078c):
    """
    represents an RDF named graph that is stored in an RDF Repository.
    
    Note that this interface inherits from XResource: the name of the graph is the string value of the RDF node. This is so that you can easily make RDF statements about named graphs.
    
    Note that instances may be destroyed via XRepository.destroyGraph(). If a graph is destroyed, subsequent calls to addStatement(), removeStatements() will fail with an com.sun.star.container.NoSuchElementException.
    
    **since**
    
        OOo 3.2

    See Also:
        `API XNamedGraph <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rdf_1_1XNamedGraph.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rdf'
    __ooo_full_ns__: str = 'com.sun.star.rdf.XNamedGraph'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rdf.XNamedGraph'

    @abstractmethod
    def addStatement(self, Subject: XResource_842709e4, Predicate: XURI_5682078c, Object: XNode_5ee40822) -> None:
        """
        adds a RDF statement to the graph.
        
        Note that the ODF elements that can have metadata attached all implement the interface XMetadatable, which inherits from XResource, meaning that you can simply pass them in as arguments here, and it will magically work.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            RepositoryException: ``RepositoryException``
        """
        ...
    @abstractmethod
    def clear(self) -> None:
        """
        removes all statements from the graph.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            RepositoryException: ``RepositoryException``
        """
        ...
    @abstractmethod
    def getName(self) -> XURI_5682078c:
        """
        returns the name of the graph.
        
        The name is unique within the repository.
        """
        ...
    @abstractmethod
    def getStatements(self, Subject: XResource_842709e4, Predicate: XURI_5682078c, Object: XNode_5ee40822) -> XEnumeration_f2180daa:
        """
        gets matching RDF statements from a graph.
        
        Note that the ODF elements that can have metadata attached all implement the interface XMetadatable, which inherits from XResource, meaning that you can simply pass them in as arguments here, and it will magically work.
        
        Any parameter may be NULL, which acts as a wildcard. For example, to get all statements about myURI: getStatements(myURI, null, null)

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            RepositoryException: ``RepositoryException``
        """
        ...
    @abstractmethod
    def removeStatements(self, Subject: XResource_842709e4, Predicate: XURI_5682078c, Object: XNode_5ee40822) -> None:
        """
        removes matching RDF statements from the graph.
        
        Note that the ODF elements that can have metadata attached all implement the interface XMetadatable, which inherits from XResource, meaning that you can simply pass them in as arguments here, and it will magically work.
        
        Any parameter may be NULL, which acts as a wildcard. For example, to remove all statements about myURI: removeStatement(myURI, null, null)

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            RepositoryException: ``RepositoryException``
        """
        ...

__all__ = ['XNamedGraph']

