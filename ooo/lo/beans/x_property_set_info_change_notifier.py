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
# Namespace: com.sun.star.beans
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_property_set_info_change_listener import XPropertySetInfoChangeListener as XPropertySetInfoChangeListener_d5261312

class XPropertySetInfoChangeNotifier(XInterface_8f010a43):
    """
    a notifier for changes of XPropertySetInfos.

    See Also:
        `API XPropertySetInfoChangeNotifier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertySetInfoChangeNotifier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.XPropertySetInfoChangeNotifier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.beans.XPropertySetInfoChangeNotifier'

    @abstractmethod
    def addPropertySetInfoChangeListener(self, Listener: 'XPropertySetInfoChangeListener_d5261312') -> None:
        """
        registers a listener for PropertySetInfoChangeEvents.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
    @abstractmethod
    def removePropertySetInfoChangeListener(self, Listener: 'XPropertySetInfoChangeListener_d5261312') -> None:
        """
        removes a listener for PropertySetInfoChangeEvents.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """

__all__ = ['XPropertySetInfoChangeNotifier']

