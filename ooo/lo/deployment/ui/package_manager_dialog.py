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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.deployment.ui
import typing
from abc import abstractmethod
from ...ui.dialogs.x_asynchronous_executable_dialog import XAsynchronousExecutableDialog as XAsynchronousExecutableDialog_255014ad
if typing.TYPE_CHECKING:
    from ...awt.x_window import XWindow as XWindow_713b0924

class PackageManagerDialog(XAsynchronousExecutableDialog_255014ad):
    """
    Service Class

    The PackageManagerDialog is used to visually manage installed packages of the user and shared installation as well as currently open documents.
    
    **since**
    
        OOo 2.0

    See Also:
        `API PackageManagerDialog <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1deployment_1_1ui_1_1PackageManagerDialog.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.deployment.ui'
    __ooo_full_ns__: str = 'com.sun.star.deployment.ui.PackageManagerDialog'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self, xParent: 'XWindow_713b0924', focusedContext: str) -> None:
        """
        Create a GUI using the specific parent window and focus on the given context.
        """
        ...
    @abstractmethod
    def createAndInstall(self, extensionURL: str) -> None:
        """
        Create a GUI and pass the URL of the extension which shall be installed right away.
        
        This constructor is intended for the case when unopkg is run as result of clicking an extension in a file browser, etc. The extensions will always be installed for the current user.
        """
        ...
    @abstractmethod
    def createDefault(self) -> None:
        """
        Create a default GUI.
        """
        ...

__all__ = ['PackageManagerDialog']

