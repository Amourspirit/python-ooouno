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
# Namespace: com.sun.star.datatransfer
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .data_flavor import DataFlavor as DataFlavor_ffd30deb

class XTransferDataAccess(XInterface_8f010a43):
    """
    This interface provides direct access to the data in all data flavors.
    
    It can be used by the clipboard implementation to optimize data transport on flush operations.

    See Also:
        `API XTransferDataAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XTransferDataAccess.html>`_
    """

    @abstractmethod
    def getData(self, aFlavorList: 'typing.List[DataFlavor_ffd30deb]') -> 'typing.List[object]':
        """
        To get all the data of a sequence of DataFlavor.
        
        An unsupported DataFlavor will be ignored.
        
        For unsupported DataFlavor an empty any will be returned.
        """
    @abstractmethod
    def queryDataSize(self, aFlavorList: 'typing.List[DataFlavor_ffd30deb]') -> int:
        """
        To query for the summarized data size in bytes of a sequence of DataFlavor.
        
        An unsupported DataFlavor will be ignored.
        """

__all__ = ['XTransferDataAccess']

