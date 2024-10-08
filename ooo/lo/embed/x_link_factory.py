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
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_storage import XStorage as XStorage_8e460a32

class XLinkFactory(XInterface_8f010a43):
    """
    allows to create and initialize a new link of specified type.

    See Also:
        `API XLinkFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XLinkFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XLinkFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XLinkFactory'

    @abstractmethod
    def createInstanceLinkUserInit(self, aClassID: typing.Tuple[int, ...], ClassName: str, xStorage: XStorage_8e460a32, sEntryName: str, aArgs: typing.Tuple[PropertyValue_c9610c73, ...], aObjectArgs: typing.Tuple[PropertyValue_c9610c73, ...]) -> XInterface_8f010a43:
        """
        creates a new link and transport parameters for persistent initialization.
        
        This method can be used to have a full control over persistence initialization of a link.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XLinkFactory']

