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
# Namespace: com.sun.star.awt.tab
import typing
from abc import abstractmethod, abstractproperty, ABC
if typing.TYPE_CHECKING:
    from .x_tab_page import XTabPage as XTabPage_a2060aa5
    from .x_tab_page_container_listener import XTabPageContainerListener as XTabPageContainerListener_940d118e

class XTabPageContainer(ABC):
    """
    An interface to a control that displays tab pages.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XTabPageContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tab_1_1XTabPageContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tab'
    __ooo_full_ns__: str = 'com.sun.star.awt.tab.XTabPageContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.tab.XTabPageContainer'

    @abstractmethod
    def addTabPageContainerListener(self, listener: 'XTabPageContainerListener_940d118e') -> None:
        """
        Adds a listener for the TabPageActivedEvent posted after the tab page was activated.
        """
    @abstractmethod
    def getTabPage(self, tabPageIndex: int) -> 'XTabPage_a2060aa5':
        """
        Returns tab page for the given index.
        """
    @abstractmethod
    def getTabPageByID(self, tabPageID: int) -> 'XTabPage_a2060aa5':
        """
        Returns tab page for the given ID.
        """
    @abstractmethod
    def getTabPageCount(self) -> int:
        """
        Returns the number of tab pages.
        """
    @abstractmethod
    def isTabPageActive(self, tabPageIndex: int) -> bool:
        """
        Checks whether a tab page is activated.
        """
    @abstractmethod
    def removeTabPageContainerListener(self, listener: 'XTabPageContainerListener_940d118e') -> None:
        """
        Removes a listener previously added with addTabPageListener().
        """
    @abstractproperty
    def ActiveTabPageID(self) -> int:
        """
        Specifies the ID of the current active tab page.
        """

__all__ = ['XTabPageContainer']

