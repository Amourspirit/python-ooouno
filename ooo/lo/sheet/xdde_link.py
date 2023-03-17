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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XDDELink(XInterface_8f010a43):
    """
    provides methods to change the settings of a DDE link.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XDDELink <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XDDELink.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XDDELink'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XDDELink'

    @abstractmethod
    def getApplication(self) -> str:
        """
        returns the application from which data are requested (the DDE server application).
        """
        ...
    @abstractmethod
    def getItem(self) -> str:
        """
        returns the DDE item from which data are requested.
        """
        ...
    @abstractmethod
    def getTopic(self) -> str:
        """
        returns the DDE topic from which data are requested.
        """
        ...

__all__ = ['XDDELink']

