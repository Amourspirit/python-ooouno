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
# Namespace: com.sun.star.ui
from __future__ import annotations
import typing
from abc import abstractmethod
from .dialogs.x_executable_dialog import XExecutableDialog as XExecutableDialog_450f0fa1
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class AddressBookSourceDialog(XExecutableDialog_450f0fa1):
    """
    Service Class

    This interface could be incomplete since I derived it from its places of use.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API AddressBookSourceDialog <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1AddressBookSourceDialog.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.AddressBookSourceDialog'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithDataSource(self, ParentWindow: XWindow_713b0924, DataSource: XPropertySet_bc180bfa, DataSourceName: str, Command: str, Title: str) -> None:
        """
        """
        ...

__all__ = ['AddressBookSourceDialog']

