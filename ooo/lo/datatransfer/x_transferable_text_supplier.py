# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.datatransfer
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_transferable import XTransferable as XTransferable_2d800f38
    from ..text.x_text_range import XTextRange as XTextRange_9a910ab7

class XTransferableTextSupplier(ABC):
    """
    
    **since**
    
        LibreOffice 7.2

    See Also:
        `API XTransferableTextSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XTransferableTextSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.XTransferableTextSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.XTransferableTextSupplier'

    @abstractmethod
    def getTransferableForTextRange(self, xRange: XTextRange_9a910ab7) -> XTransferable_2d800f38:
        """
        Provide access to a transferable representation of a given text range.
        """
        ...

__all__ = ['XTransferableTextSupplier']

