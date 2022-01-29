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
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_modify_listener import XModifyListener as XModifyListener_d5c60ccc

class XModifyBroadcaster(XInterface_8f010a43):
    """
    broadcasts each modification made on the date data of the object which supports this interface.
    
    The modified object must post the modification events immediately after the modification is performed.

    See Also:
        `API XModifyBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XModifyBroadcaster.html>`_
    """

    @abstractmethod
    def addModifyListener(self, aListener: 'XModifyListener_d5c60ccc') -> None:
        """
        adds the specified listener to receive events \"modified.\"
        """
    @abstractmethod
    def removeModifyListener(self, aListener: 'XModifyListener_d5c60ccc') -> None:
        """
        removes the specified listener.
        """

__all__ = ['XModifyBroadcaster']

