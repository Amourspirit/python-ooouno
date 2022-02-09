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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XPrinterPropertySet(XPropertySet_bc180bfa):
    """
    represents an extended property set for printer properties.
    
    All properties are vetoable properties. If you change the properties between com.sun.star.awt.XPrinter.startPage() and com.sun.star.awt.XPrinter.endPage(), a com.sun.star.beans.PropertyVetoException is thrown.

    See Also:
        `API XPrinterPropertySet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XPrinterPropertySet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XPrinterPropertySet'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XPrinterPropertySet'

    @abstractmethod
    def getBinarySetup(self) -> 'typing.Tuple[int, ...]':
        """
        returns a binary encoded version of the printer setup.
        """
    @abstractmethod
    def getFormDescriptions(self) -> 'typing.Tuple[str, ...]':
        """
        returns descriptions of all available printer forms.
        """
    @abstractmethod
    def selectForm(self, aFormDescription: str) -> None:
        """
        sets the form that should be used.
        
        Indirectly a printer is selected.

        Raises:
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def setBinarySetup(self, data: 'typing.Tuple[int, ...]') -> None:
        """
        sets the data specific to the printer driver.
        
        Get this data from the info printer and set the data to the printer.

        Raises:
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def setHorizontal(self, bHorizontal: bool) -> None:
        """
        sets the orientation.

        Raises:
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """


__all__ = ['XPrinterPropertySet']

