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
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_remote_content_provider_change_listener import XRemoteContentProviderChangeListener as XRemoteContentProviderChangeListener_24d814b8

class XRemoteContentProviderChangeNotifier(XInterface_8f010a43):
    """
    Notify about changes to a XRemoteContentProviderSupplier.

    See Also:
        `API XRemoteContentProviderChangeNotifier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XRemoteContentProviderChangeNotifier.html>`_
    """

    @abstractmethod
    def addRemoteContentProviderChangeListener(self, Listener: 'XRemoteContentProviderChangeListener_24d814b8') -> None:
        """
        Add a listener.
        """
    @abstractmethod
    def removeRemoteContentProviderChangeListener(self, Listener: 'XRemoteContentProviderChangeListener_24d814b8') -> None:
        """
        Remove a listener.
        """

__all__ = ['XRemoteContentProviderChangeNotifier']

