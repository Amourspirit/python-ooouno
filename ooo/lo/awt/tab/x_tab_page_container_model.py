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
# Namespace: com.sun.star.awt.tab
from __future__ import annotations
import typing
from abc import abstractmethod
from ...container.x_container import XContainer as XContainer_d6fb0cc6
from ...container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
if typing.TYPE_CHECKING:
    from .x_tab_page_model import XTabPageModel as XTabPageModel_dcde0c96

class XTabPageContainerModel(XContainer_d6fb0cc6, XIndexContainer_1c040ebe):
    """
    specifies an interface for a UnoControlTabPageContainerModel.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XTabPageContainerModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tab_1_1XTabPageContainerModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tab'
    __ooo_full_ns__: str = 'com.sun.star.awt.tab.XTabPageContainerModel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.tab.XTabPageContainerModel'

    @abstractmethod
    def createTabPage(self, TabPageID: int) -> XTabPageModel_dcde0c96:
        """
        creates a TabPageModel which can be inserted into the container.
        """
        ...
    @abstractmethod
    def loadTabPage(self, TabPageID: int, ResourceURL: str) -> XTabPageModel_dcde0c96:
        """
        creates a TabPageModel which can be inserted into the container, by loading it from a user interface resource file.
        """
        ...

__all__ = ['XTabPageContainerModel']

