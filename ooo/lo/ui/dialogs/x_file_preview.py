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
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...util.color import Color as Color_68e908c5

class XFilePreview(XInterface_8f010a43):
    """
    FilePicker that support the preview of various file formats should implement this interface.

    See Also:
        `API XFilePreview <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFilePreview.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XFilePreview'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XFilePreview'

    @abstractmethod
    def getAvailableHeight(self) -> int:
        """
        The method returns the available height of the preview window even if the window is invisible or could not be created.
        
        If a service implementation doesn't support a file preview 0 will be returned.
        """
    @abstractmethod
    def getAvailableWidth(self) -> int:
        """
        The method returns the available width of the preview window even if the window is invisible or could not be created.
        
        If a service implementation doesn't support a file preview 0 will be returned.
        """
    @abstractmethod
    def getShowState(self) -> bool:
        """
        Returns the current show state of the preview.
        
        A value of FALSE if the preview window is invisible.
        """
    @abstractmethod
    def getSupportedImageFormats(self) -> 'typing.Tuple[int, ...]':
        """
        The method returns all image formats that the preview supports.
        """
    @abstractmethod
    def getTargetColorDepth(self) -> 'Color_68e908c5':
        """
        The method returns the supported color depth of the target device.
        """
    @abstractmethod
    def setImage(self, aImageFormat: int, aImage: object) -> None:
        """
        Sets a new image.
        
        If the preview is currently hidden the image will be ignored. An empty any will clear the preview window.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def setShowState(self, bShowState: bool) -> bool:
        """
        Optionally sets the current show state of the preview.
        
        It is possible that the preview implementation doesn't support hiding the preview.
        
        A value of FALSE hides the preview window.
        
        A value of FALSE if the operation fails for any reason or the preview implementation doesn't support hiding the preview.
        """


__all__ = ['XFilePreview']

