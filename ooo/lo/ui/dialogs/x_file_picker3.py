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
# Namespace: com.sun.star.ui.dialogs
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from .x_file_picker2 import XFilePicker2 as XFilePicker2_f99d0d5f
from .x_file_picker_notifier import XFilePickerNotifier as XFilePickerNotifier_6402106d
from .x_file_preview import XFilePreview as XFilePreview_fa400db1
from .x_filter_group_manager import XFilterGroupManager as XFilterGroupManager_65a9107d
from .x_filter_manager import XFilterManager as XFilterManager_16f30e70
from ...util.x_cancellable import XCancellable as XCancellable_afc30b64

class XFilePicker3(XComponent_98dc0ab5, XFilePicker2_f99d0d5f, XFilePickerNotifier_6402106d, XFilePreview_fa400db1, XFilterGroupManager_65a9107d, XFilterManager_16f30e70, XCancellable_afc30b64):
    """
    Provides unified interface for FilePicker service.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XFilePicker3 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFilePicker3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XFilePicker3'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XFilePicker3'



__all__ = ['XFilePicker3']

