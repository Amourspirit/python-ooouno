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
# Namespace: com.sun.star.xml.crypto
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...io.x_input_stream import XInputStream as XInputStream_98d40ab4

class XUriBinding(XInterface_8f010a43):
    """
    Interface of Uri Binding.
    
    This interface is used to dynamically bind a uri with a XInputStream interface.

    See Also:
        `API XUriBinding <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XUriBinding.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.XUriBinding'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.XUriBinding'

    @abstractmethod
    def getUriBinding(self, uri: str) -> 'XInputStream_98d40ab4':
        """
        Gets the XInputStream interface for a uri.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def setUriBinding(self, uri: str, InputStream: 'XInputStream_98d40ab4') -> None:
        """
        Sets the XInputStream interface for a uri.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """


__all__ = ['XUriBinding']

