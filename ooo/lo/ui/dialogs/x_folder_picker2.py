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
# Namespace: com.sun.star.ui.dialogs
from __future__ import annotations
from .x_folder_picker import XFolderPicker as XFolderPicker_86a0e09
from ...util.x_cancellable import XCancellable as XCancellable_afc30b64

class XFolderPicker2(XFolderPicker_86a0e09, XCancellable_afc30b64):
    """
    Provides a unified interface for the new-style FolderPicker service to implement.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XFolderPicker2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFolderPicker2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XFolderPicker2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XFolderPicker2'


__all__ = ['XFolderPicker2']

