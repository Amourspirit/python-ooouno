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
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_content_provider import XContentProvider as XContentProvider_d4150cc0

class XParameterizedContentProvider(XInterface_8f010a43):
    """
    Register specially adjusted instances of content providers on URL templates and supplementary arguments.

    See Also:
        `API XParameterizedContentProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XParameterizedContentProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XParameterizedContentProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XParameterizedContentProvider'

    @abstractmethod
    def deregisterInstance(self, Template: str, Arguments: str) -> 'XContentProvider_d4150cc0':
        """
        Deregisters a content provider.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def registerInstance(self, Template: str, Arguments: str, ReplaceExisting: bool) -> 'XContentProvider_d4150cc0':
        """
        Register a content provider on a URL template and supplementary arguments.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XParameterizedContentProvider']

