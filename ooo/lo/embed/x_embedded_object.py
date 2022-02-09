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
# Namespace: com.sun.star.embed
import typing
from abc import abstractmethod
from ..document.x_event_broadcaster import XEventBroadcaster as XEventBroadcaster_2b120f2b
from .x_classified_object import XClassifiedObject as XClassifiedObject_fa3b0dab
from .x_component_supplier import XComponentSupplier as XComponentSupplier_adb0e64
from .x_state_change_broadcaster import XStateChangeBroadcaster as XStateChangeBroadcaster_539f100e
from .x_visual_object import XVisualObject as XVisualObject_c6c80c28
from ..util.x_closeable import XCloseable as XCloseable_99ee0aa8
if typing.TYPE_CHECKING:
    from .verb_descriptor import VerbDescriptor as VerbDescriptor_d3680cb3
    from .x_embedded_client import XEmbeddedClient as XEmbeddedClient_ddea0cc6

class XEmbeddedObject(XEventBroadcaster_2b120f2b, XClassifiedObject_fa3b0dab, XComponentSupplier_adb0e64, XStateChangeBroadcaster_539f100e, XVisualObject_c6c80c28, XCloseable_99ee0aa8):
    """
    represents common functionality for embedded objects.

    See Also:
        `API XEmbeddedObject <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XEmbeddedObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XEmbeddedObject'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XEmbeddedObject'

    @abstractmethod
    def changeState(self, nNewState: int) -> None:
        """
        changes the state of the object to the requested one.

        Raises:
            com.sun.star.embed.UnreachableStateException: ``UnreachableStateException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def doVerb(self, nVerbID: int) -> None:
        """
        lets object perform an action referenced by nVerbID.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.embed.UnreachableStateException: ``UnreachableStateException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def getClientSite(self) -> 'XEmbeddedClient_ddea0cc6':
        """
        provides access to the internal link to the container client.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
    @abstractmethod
    def getCurrentState(self) -> int:
        """
        returns the current state of the object.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
    @abstractmethod
    def getReachableStates(self) -> 'typing.Tuple[int, ...]':
        """
        returns supported states for the object.

        Raises:
            com.sun.star.embed.NeedsRunningStateException: ``NeedsRunningStateException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
    @abstractmethod
    def getStatus(self, nAspect: int) -> int:
        """
        retrieves the status of the object.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
    @abstractmethod
    def getSupportedVerbs(self) -> 'typing.Tuple[VerbDescriptor_d3680cb3, ...]':
        """
        returns supported verbs for the object.

        Raises:
            com.sun.star.embed.NeedsRunningStateException: ``NeedsRunningStateException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
    @abstractmethod
    def setClientSite(self, xClient: 'XEmbeddedClient_ddea0cc6') -> None:
        """
        sets a connection to the container's client.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
    @abstractmethod
    def setContainerName(self, sName: str) -> None:
        """
        provides object with the name of container document.
        """
    @abstractmethod
    def setUpdateMode(self, nMode: int) -> None:
        """
        specifies how often the object's representation should be updated.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
    @abstractmethod
    def update(self) -> None:
        """
        updates object's representations.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.uno.Exception: ``Exception``
        """


__all__ = ['XEmbeddedObject']

