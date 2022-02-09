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
# Namespace: com.sun.star.sheet
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSheetConditionalEntry(XInterface_8f010a43):
    """
    provides methods to access the cell style name for a condition in a conditional format.

    See Also:
        `API XSheetConditionalEntry <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetConditionalEntry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetConditionalEntry'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetConditionalEntry'

    @abstractmethod
    def getStyleName(self) -> str:
        """
        returns the name of the cell style that is used when the condition is fulfilled.
        """
    @abstractmethod
    def setStyleName(self, aStyleName: str) -> None:
        """
        sets the name of the cell style that is used when the condition is fulfilled.
        """


__all__ = ['XSheetConditionalEntry']

