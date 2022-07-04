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
# Namespace: com.sun.star.awt.tree
import typing
from abc import abstractmethod
from ...lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_tree_data_model_listener import XTreeDataModelListener as XTreeDataModelListener_748210cb
    from .x_tree_node import XTreeNode as XTreeNode_baaf0ba0

class XTreeDataModel(XComponent_98dc0ab5):
    """
    An instance of this interface is used by the TreeControl to retrieve the hierarchical outline data that is displayed in the actual control.
    
    If you implement your own XTreeDataModel you need to notify registered XTreeDataModelListener if your model changes after the control is created. If this is not done correctly the TreeControl will not update the data properly.
    
    If you do not need your own model implementation, you can also use the MutableTreeDataModel.

    See Also:
        `API XTreeDataModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tree_1_1XTreeDataModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tree'
    __ooo_full_ns__: str = 'com.sun.star.awt.tree.XTreeDataModel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.tree.XTreeDataModel'

    @abstractmethod
    def addTreeDataModelListener(self, Listener: 'XTreeDataModelListener_748210cb') -> None:
        """
        Adds a listener for the TreeDataModelEvent posted after the tree changes.
        """
        ...
    @abstractmethod
    def getRoot(self) -> 'XTreeNode_baaf0ba0':
        """
        Returns the root of the tree.
        
        Returns null only if the tree has no nodes.
        """
        ...
    @abstractmethod
    def removeTreeDataModelListener(self, Listener: 'XTreeDataModelListener_748210cb') -> None:
        """
        Removes a listener previously added with addTreeDataModelListener().
        """
        ...

__all__ = ['XTreeDataModel']

