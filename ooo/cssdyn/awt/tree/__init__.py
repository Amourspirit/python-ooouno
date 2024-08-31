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
    from ....dyn.awt.tree.expand_veto_exception import ExpandVetoException as ExpandVetoException
with suppress(ImportError):
    from ....dyn.awt.tree.mutable_tree_data_model import MutableTreeDataModel as MutableTreeDataModel
with suppress(ImportError):
    from ....dyn.awt.tree.mutable_tree_node import MutableTreeNode as MutableTreeNode
with suppress(ImportError):
    from ....dyn.awt.tree.tree_control import TreeControl as TreeControl
with suppress(ImportError):
    from ....dyn.awt.tree.tree_control_model import TreeControlModel as TreeControlModel
with suppress(ImportError):
    from ....dyn.awt.tree.tree_data_model_event import TreeDataModelEvent as TreeDataModelEvent
with suppress(ImportError):
    from ....dyn.awt.tree.tree_expansion_event import TreeExpansionEvent as TreeExpansionEvent
with suppress(ImportError):
    from ....dyn.awt.tree.x_mutable_tree_data_model import XMutableTreeDataModel as XMutableTreeDataModel
with suppress(ImportError):
    from ....dyn.awt.tree.x_mutable_tree_node import XMutableTreeNode as XMutableTreeNode
with suppress(ImportError):
    from ....dyn.awt.tree.x_tree_control import XTreeControl as XTreeControl
with suppress(ImportError):
    from ....dyn.awt.tree.x_tree_data_model import XTreeDataModel as XTreeDataModel
with suppress(ImportError):
    from ....dyn.awt.tree.x_tree_data_model_listener import XTreeDataModelListener as XTreeDataModelListener
with suppress(ImportError):
    from ....dyn.awt.tree.x_tree_edit_listener import XTreeEditListener as XTreeEditListener
with suppress(ImportError):
    from ....dyn.awt.tree.x_tree_expansion_listener import XTreeExpansionListener as XTreeExpansionListener
with suppress(ImportError):
    from ....dyn.awt.tree.x_tree_node import XTreeNode as XTreeNode
