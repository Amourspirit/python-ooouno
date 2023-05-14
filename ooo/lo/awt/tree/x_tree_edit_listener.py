# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt.tree
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .x_tree_node import XTreeNode as XTreeNode_baaf0ba0

class XTreeEditListener(XEventListener_c7230c4a):
    """
    You can implement this interface and register with XTreeControl.addTreeEditListener() to get notifications when editing of a node starts and ends.
    
    You have to set the TreeControlModel.Editable property to TRUE before a tree supports editing.

    See Also:
        `API XTreeEditListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tree_1_1XTreeEditListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tree'
    __ooo_full_ns__: str = 'com.sun.star.awt.tree.XTreeEditListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.tree.XTreeEditListener'

    @abstractmethod
    def nodeEdited(self, Node: 'XTreeNode_baaf0ba0', NewText: str) -> None:
        """
        This method is called from the TreeControl implementation when editing of Node is finished and was not canceled.
        
        Implementations that register a XTreeEditListener must update the display value at the Node.
        """
        ...
    @abstractmethod
    def nodeEditing(self, Node: 'XTreeNode_baaf0ba0') -> None:
        """
        This method is called from the TreeControl implementation when editing of Node is requested by calling XTreeControl.startEditingAtNode().

        Raises:
            com.sun.star.util.VetoException: ``VetoException``
        """
        ...

__all__ = ['XTreeEditListener']

