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
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt.tree
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .tree_expansion_event import TreeExpansionEvent as TreeExpansionEvent_378b0f79

class XTreeExpansionListener(XEventListener_c7230c4a):
    """
    An instance of this interface can get notifications from a TreeControl when nodes are expanded or collapsed.

    See Also:
        `API XTreeExpansionListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tree_1_1XTreeExpansionListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tree'
    __ooo_full_ns__: str = 'com.sun.star.awt.tree.XTreeExpansionListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.tree.XTreeExpansionListener'

    @abstractmethod
    def requestChildNodes(self, Event: 'TreeExpansionEvent_378b0f79') -> None:
        """
        Invoked when a node with children on demand is about to be expanded.
        
        This event is invoked before the treeExpanding() event.
        """
        ...
    @abstractmethod
    def treeCollapsed(self, Event: 'TreeExpansionEvent_378b0f79') -> None:
        """
        Called whenever a node in the tree has been successfully collapsed.
        """
        ...
    @abstractmethod
    def treeCollapsing(self, Event: 'TreeExpansionEvent_378b0f79') -> None:
        """
        Invoked whenever a node in the tree is about to be collapsed.

        Raises:
            ExpandVetoException: ``ExpandVetoException``
        """
        ...
    @abstractmethod
    def treeExpanded(self, Event: 'TreeExpansionEvent_378b0f79') -> None:
        """
        Called whenever a node in the tree has been successfully expanded.
        """
        ...
    @abstractmethod
    def treeExpanding(self, Event: 'TreeExpansionEvent_378b0f79') -> None:
        """
        Invoked whenever a node in the tree is about to be expanded.

        Raises:
            ExpandVetoException: ``ExpandVetoException``
        """
        ...

__all__ = ['XTreeExpansionListener']

