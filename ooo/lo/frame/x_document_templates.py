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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_storable import XStorable as XStorable_998f0aa7
    from ..ucb.x_content import XContent as XContent_79db0975

class XDocumentTemplates(XInterface_8f010a43):
    """
    provides a high level API to organize document templates
    
    Template information is saved as links to the original content and organized in groups. This data should be persistent and can be updated by calling special method XDocumentTemplates.update(). A real implementation of this interface can do that on top of a ucb content provider. Method XDocumentTemplates.getContent() force that.

    See Also:
        `API XDocumentTemplates <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDocumentTemplates.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XDocumentTemplates'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XDocumentTemplates'

    @abstractmethod
    def addGroup(self, GroupName: str) -> bool:
        """
        creates a new group
        """
        ...
    @abstractmethod
    def addTemplate(self, GroupName: str, TemplateName: str, SourceURL: str) -> bool:
        """
        creates the template with the given name in the given group using the given URL
        """
        ...
    @abstractmethod
    def getContent(self) -> XContent_79db0975:
        """
        provides access to the root of internal used hierarchy
        
        This content can be used for accessing the groups directly.
        """
        ...
    @abstractmethod
    def removeGroup(self, GroupName: str) -> bool:
        """
        remove an existing group
        """
        ...
    @abstractmethod
    def removeTemplate(self, GroupName: str, TemplateName: str) -> bool:
        """
        remove a template from specified group
        """
        ...
    @abstractmethod
    def renameGroup(self, OldGroupName: str, NewGroupName: str) -> bool:
        """
        rename an existing group
        """
        ...
    @abstractmethod
    def renameTemplate(self, GroupName: str, OldTemplateName: str, NewTemplateName: str) -> bool:
        """
        rename a template inside specified group
        """
        ...
    @abstractmethod
    def storeTemplate(self, GroupName: str, TemplateName: str, Storable: XStorable_998f0aa7) -> bool:
        """
        creates the template with the given name in the given group using the data from the storable
        """
        ...
    @abstractmethod
    def update(self) -> None:
        """
        force an update for internal structures
        
        Because the templates are well known by links and not as direct content they can be outdated. An update force actualization of that to find wrong links.
        """
        ...

__all__ = ['XDocumentTemplates']

