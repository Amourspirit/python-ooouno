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
# Namespace: com.sun.star.accessibility
from abc import abstractmethod
from ..lang.x_component import XComponent as XComponent_98dc0ab5

class XMSAAService(XComponent_98dc0ab5):
    """
    The interface must be implemented for a server that can support MSAA com objects and send win32 accessible events.

    See Also:
        `API XMSAAService <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XMSAAService.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XMSAAService'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XMSAAService'

    @abstractmethod
    def getAccObjectPtr(self, hWnd: int, lParam: int, wParam: int) -> int:
        """
        Return com object pointer.
        """
    @abstractmethod
    def handleWindowOpened(self, i: int) -> None:
        """
        """

__all__ = ['XMSAAService']

