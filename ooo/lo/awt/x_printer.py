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
from .x_printer_property_set import XPrinterPropertySet as XPrinterPropertySet_ff190e21
if typing.TYPE_CHECKING:
    from .x_device import XDevice as XDevice_70ba08fc

class XPrinter(XPrinterPropertySet_ff190e21):
    """
    represents a virtual printer.
    
    All properties are vetoable properties. If you change the properties between a call to com.sun.star.awt.XPrinter.startPage() and a call to com.sun.star.awt.XPrinter.endPage(), a com.sun.star.beans.PropertyVetoException is thrown.

    See Also:
        `API XPrinter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XPrinter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XPrinter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XPrinter'

    @abstractmethod
    def end(self) -> None:
        """
        notifies the printer spooler that the job is done and printing starts.

        Raises:
            com.sun.star.awt.PrinterException: ``PrinterException``
        """
    @abstractmethod
    def endPage(self) -> None:
        """
        ends the current page.

        Raises:
            com.sun.star.awt.PrinterException: ``PrinterException``
        """
    @abstractmethod
    def start(self, nJobName: str, nCopies: int, nCollate: bool) -> bool:
        """
        puts the job into the printer spooler.
        
        This call may block the thread. So release all resources (mutex, semaphore, etc.) before this call.

        Raises:
            com.sun.star.awt.PrinterException: ``PrinterException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def startPage(self) -> 'XDevice_70ba08fc':
        """
        begins with a new page.

        Raises:
            com.sun.star.awt.PrinterException: ``PrinterException``
        """
    @abstractmethod
    def terminate(self) -> None:
        """
        stops the current print job.
        
        If the method com.sun.star.awt.XPrinter.end() is called beforehand, then this call does nothing. If you call com.sun.star.awt.XPrinter.terminate() in or before the call to com.sun.star.awt.XPrinter.start(), com.sun.star.awt.XPrinter.terminate() returns FALSE. This call must not block the thread.
        """

__all__ = ['XPrinter']
