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
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui.dialogs
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .dialog_closed_event import DialogClosedEvent as DialogClosedEvent_444e0fa3

class XDialogClosedListener(XEventListener_c7230c4a):
    """
    Used to notify listeners about dialog-closed events.
    
    Registered listeners will be notified with a DialogClosedEvent when a XAsynchronousExecutableDialog is closed.

    See Also:
        `API XDialogClosedListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XDialogClosedListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XDialogClosedListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XDialogClosedListener'

    @abstractmethod
    def dialogClosed(self, aEvent: 'DialogClosedEvent_444e0fa3') -> None:
        """
        A client receives this event if a dialog is closed.
        """
        ...

__all__ = ['XDialogClosedListener']

