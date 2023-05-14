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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui.dialogs
import typing
from abc import abstractmethod
from .x_file_picker import XFilePicker as XFilePicker_ec3e0d2d

class XFilePicker2(XFilePicker_ec3e0d2d):
    """
    extends file picker interface to workaround some design problems.

    See Also:
        `API XFilePicker2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFilePicker2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XFilePicker2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XFilePicker2'

    @abstractmethod
    def getSelectedFiles(self) -> 'typing.Tuple[str, ...]':
        """
        Returns a sequence of the selected files including path information in URL format, conforming to Rfc1738.
        
        If the user closed the dialog with cancel an empty sequence will be returned.
        
        If the user closed the dialog with OK a list of all selected files will be returned.
        
        Instead to the method getFiles() of base interface XFilePicker the new method return full qualified URLs for every selected file.
        
        A list of all selected file as complete URLs.
        
        Notes for the implementation of a FileSave dialog:If there exists a checkbox \"Automatic File Extension\" which is checked and a valid filter is currently selected the dialog may automatically add an extension to the selected file name(s).
        """
        ...

__all__ = ['XFilePicker2']

