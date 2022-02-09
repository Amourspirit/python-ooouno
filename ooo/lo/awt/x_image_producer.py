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
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_image_consumer import XImageConsumer as XImageConsumer_ba790bdb

class XImageProducer(XInterface_8f010a43):
    """
    specifies a source for an image.

    See Also:
        `API XImageProducer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XImageProducer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XImageProducer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XImageProducer'

    @abstractmethod
    def addConsumer(self, xConsumer: 'XImageConsumer_ba790bdb') -> None:
        """
        registers an image consumer with the image producer for accessing the image data during a later reconstruction of the image.
        
        The image producer may, at its discretion, start delivering the image data to the consumer using the XImageConsumer interface immediately, or when the next available image reconstruction is triggered by a call to the startProduction method.
        """
    @abstractmethod
    def removeConsumer(self, xConsumer: 'XImageConsumer_ba790bdb') -> None:
        """
        removes the given com.sun.star.awt.XImageConsumer callback from the list of consumers currently registered to receive image data.
        
        It is not considered an error to remove a consumer that is not currently registered. The image producer should stop sending data to this consumer as soon as it is feasible.
        """
    @abstractmethod
    def startProduction(self) -> None:
        """
        registers the given image consumer as a consumer and starts an immediate reconstruction of the image data.
        
        The image data will then be delivered to this consumer and any other consumer which may have already been registered with the producer. This method differs from the addConsumer method in that a reproduction of the image data should be triggered as soon as possible.
        """


__all__ = ['XImageProducer']

