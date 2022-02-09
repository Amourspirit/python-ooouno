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
from abc import abstractmethod, abstractproperty
from ..container.x_container import XContainer as XContainer_d6fb0cc6

class XAnimatedImages(XContainer_d6fb0cc6):
    """
    allows administrating a set of images, to be displayed as animated seres.
    
    Components implementing this interface maintain a variable number of image sets. Components displaying those images will choose the best-fitting image set depending on the available space, and possibly other restrictions.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XAnimatedImages <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XAnimatedImages.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XAnimatedImages'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XAnimatedImages'

    @abstractmethod
    def getImageSet(self, iIndex: int) -> 'typing.Tuple[str, ...]':
        """
        returns the URLs of the image set with the given index

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getImageSetCount(self) -> int:
        """
        returns the number of images sets maintained by the component.
        """
    @abstractmethod
    def insertImageSet(self, iIndex: int, iImageURLs: 'typing.Tuple[str, ...]') -> None:
        """
        sets the URLs of the image set with the given index

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def removeImageSet(self, iIndex: int) -> None:
        """
        removes the image set with the given index

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def replaceImageSet(self, iIndex: int, iImageURLs: 'typing.Tuple[str, ...]') -> None:
        """
        replaces the image set given by index with a new one

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractproperty
    def AutoRepeat(self) -> bool:
        """
        specifies whether the animation should start over with the first image of the image series when the last image has been played.
        
        The default value for this attribute is TRUE.
        """
    @abstractproperty
    def ScaleMode(self) -> int:
        """
        controls the way the images are scaled up or down, when the available space is larger or smaller than what is needed for them.
        
        Allowed values are those from the ImageScaleMode constants group.
        """
    @abstractproperty
    def StepTime(self) -> int:
        """
        specifies the time in milliseconds between two animation steps.
        
        This is the minimum time, the actual value might be longer due to system load. The default value will be 100 ms.
        """


__all__ = ['XAnimatedImages']

