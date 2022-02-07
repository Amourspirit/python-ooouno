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
# Namespace: com.sun.star.smarttags
import typing
from abc import abstractmethod, abstractproperty
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
if typing.TYPE_CHECKING:
    from ..container.x_string_key_map import XStringKeyMap as XStringKeyMap_ffc60de1
    from ..frame.x_controller import XController as XController_b00e0b8f
    from ..lang.locale import Locale as Locale_70d308fa
    from ..text.x_text_range import XTextRange as XTextRange_9a910ab7

class XSmartTagAction(XInitialization_d46c0cca):
    """
    provides access to smart tag actions.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XSmartTagAction <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1smarttags_1_1XSmartTagAction.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.smarttags'
    __ooo_full_ns__: str = 'com.sun.star.smarttags.XSmartTagAction'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.smarttags.XSmartTagAction'

    @abstractmethod
    def getActionCaptionFromID(self, nActionID: int, aApplicationName: str, aLocale: 'Locale_70d308fa', xProperties: 'XStringKeyMap_ffc60de1', aText: str, aXML: str, xController: 'XController_b00e0b8f', xTarget: 'XTextRange_9a910ab7') -> str:
        """
        obtains a caption for a specified action for use in user interfaces.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getActionCount(self, aSmartTagName: str, xController: 'XController_b00e0b8f', xProperties: 'XStringKeyMap_ffc60de1') -> int:
        """
        obtains the number of actions provided for a specified smart tag type.
        """
    @abstractmethod
    def getActionID(self, aSmartTagName: str, nActionIndex: int, xController: 'XController_b00e0b8f') -> int:
        """
        obtains a unique integer identifier for an action.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getActionNameFromID(self, nActionID: int, xController: 'XController_b00e0b8f') -> str:
        """
        obtains a language independent name of an action.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getDescription(self, aLocale: 'Locale_70d308fa') -> str:
        """
        obtains a detailed description of this action component.
        """
    @abstractmethod
    def getName(self, aLocale: 'Locale_70d308fa') -> str:
        """
        obtains a name that describes this action component.
        """
    @abstractmethod
    def getSmartTagCaption(self, nSmartTagIndex: int, aLocale: 'Locale_70d308fa') -> str:
        """
        obtains the caption of the smart tag type for using in user interfaces.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getSmartTagName(self, nSmartTagIndex: int) -> str:
        """
        obtains the name of one specific smart tag type supported by this action component.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def invokeAction(self, nActionID: int, aApplicationName: str, xController: 'XController_b00e0b8f', xTarget: 'XTextRange_9a910ab7', xProperties: 'XStringKeyMap_ffc60de1', aText: str, aXML: str, aLocale: 'Locale_70d308fa') -> None:
        """
        invokes an action.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def isCaptionDynamic(self, nActionID: int, aApplicationName: str, xController: 'XController_b00e0b8f', aLocale: 'Locale_70d308fa') -> bool:
        """
        determines whether a caption is dynamic.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def isShowSmartTagIndicator(self, nActionID: int, aApplicationName: str, xController: 'XController_b00e0b8f', aLocale: 'Locale_70d308fa') -> bool:
        """
        determines whether the smart tag indicator should be visible.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractproperty
    def SmartTagCount(self) -> int:
        """
        the number of smart tag types supported by this action component.
        """

__all__ = ['XSmartTagAction']

