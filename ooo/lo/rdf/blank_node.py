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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.rdf
from abc import abstractmethod
from .x_blank_node import XBlankNode as XBlankNode_8cf40a0a

class BlankNode(XBlankNode_8cf40a0a):
    """
    Service Class

    represents a blank node that may occur in a RDF graph.
    
    **since**
    
        OOo 3.0

    See Also:
        `API BlankNode <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1rdf_1_1BlankNode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rdf'
    __ooo_full_ns__: str = 'com.sun.star.rdf.BlankNode'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self, NodeID: str) -> None:
        """
        create a blank RDF node.
        
        Be careful! With this constructor you can create a node that aliases another node that already exists in some repository. That may or may not be what you want. If you want to create a new blank node that is guaranteed to be unique, use XRepository.createBlankNode() instead.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['BlankNode']

