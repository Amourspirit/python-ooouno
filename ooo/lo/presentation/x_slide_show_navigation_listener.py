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
# Namespace: com.sun.star.presentation
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_slide_show_listener import XSlideShowListener as XSlideShowListener_81671154
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e

class XSlideShowNavigationListener(XSlideShowListener_81671154):
    """
    Listener interface with navigation support to receive global slide show events.
    
    **since**
    
        LibreOffice 7.6

    See Also:
        `API XSlideShowNavigationListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XSlideShowNavigationListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.XSlideShowNavigationListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.presentation.XSlideShowNavigationListener'

    @abstractmethod
    def contextMenuShow(self, point: Point_5fb2085e) -> None:
        """
        Notify that the context menu has been requested.
        """
        ...

__all__ = ['XSlideShowNavigationListener']
