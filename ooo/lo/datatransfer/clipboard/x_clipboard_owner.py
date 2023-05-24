# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.datatransfer.clipboard
from __future__ import annotations
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..x_transferable import XTransferable as XTransferable_2d800f38
    from .x_clipboard import XClipboard as XClipboard_a18a11cd

class XClipboardOwner(XInterface_8f010a43):
    """
    The owner of a transferable object may pass this interface to the clipboard instance.

    See Also:
        `API XClipboardOwner <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1clipboard_1_1XClipboardOwner.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.clipboard'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.clipboard.XClipboardOwner'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.clipboard.XClipboardOwner'

    @abstractmethod
    def lostOwnership(self, xClipboard: XClipboard_a18a11cd, xTrans: XTransferable_2d800f38) -> None:
        """
        Notifies the transferable object source that it is no longer the owner of the clipboard.
        """
        ...

__all__ = ['XClipboardOwner']

