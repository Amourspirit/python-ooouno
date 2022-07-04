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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XBrowseHistoryRegistry(XInterface_8f010a43):
    """
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XBrowseHistoryRegistry <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XBrowseHistoryRegistry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XBrowseHistoryRegistry'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XBrowseHistoryRegistry'

    @abstractmethod
    def createNewEntry(self, URL: str, Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]', Title: str) -> None:
        """
        """
        ...
    @abstractmethod
    def updateViewData(self, Value: object) -> None:
        """
        """
        ...

__all__ = ['XBrowseHistoryRegistry']

