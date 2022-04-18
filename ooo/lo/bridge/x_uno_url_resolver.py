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
# Libre Office Version: 7.3
# Namespace: com.sun.star.bridge
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XUnoUrlResolver(XInterface_8f010a43):
    """
    allows to resolve an object using the uno-url.

    See Also:
        `API XUnoUrlResolver <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1bridge_1_1XUnoUrlResolver.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge'
    __ooo_full_ns__: str = 'com.sun.star.bridge.XUnoUrlResolver'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.bridge.XUnoUrlResolver'

    @abstractmethod
    def resolve(self, sUnoUrl: str) -> 'XInterface_8f010a43':
        """
        resolves an object using the given uno-url.

        Raises:
            com.sun.star.connection.NoConnectException: ``NoConnectException``
            com.sun.star.connection.ConnectionSetupException: ``ConnectionSetupException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XUnoUrlResolver']

