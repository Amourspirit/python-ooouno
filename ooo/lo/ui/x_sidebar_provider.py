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
# Namespace: com.sun.star.ui
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..frame.x_frame import XFrame as XFrame_7a570956
    from .x_decks import XDecks as XDecks_5e8b0828
    from .x_sidebar import XSidebar as XSidebar_704a08f8

class XSidebarProvider(XInterface_8f010a43):
    """
    Interface of the sidebar.
    
    **since**
    
        LibreOffice 5.1

    See Also:
        `API XSidebarProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XSidebarProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XSidebarProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XSidebarProvider'

    @abstractmethod
    def getDecks(self) -> 'XDecks_5e8b0828':
        """
        """
    @abstractmethod
    def getFrame(self) -> 'XFrame_7a570956':
        """
        Get the XFrame owner.
        """
    @abstractmethod
    def getSidebar(self) -> 'XSidebar_704a08f8':
        """
        Returns the sidebar object.
        """
    @abstractmethod
    def isVisible(self) -> bool:
        """
        Is the sidebar visible.
        """
    @abstractmethod
    def setVisible(self, bVisible: bool) -> None:
        """
        Display the sidebar.
        """
    @abstractmethod
    def showDecks(self, bVisible: bool) -> None:
        """
        Decks container visibility.
        """

__all__ = ['XSidebarProvider']

