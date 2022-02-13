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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.embed
import typing
from abc import abstractmethod
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_actions_approval import XActionsApproval as XActionsApproval_ed4b0d73
    from ..uno.x_interface import XInterface as XInterface_8f010a43

class InstanceLocker(XComponent_98dc0ab5):
    """
    Service Class

    The main task of this service is to prevent closing, terminating and/or etc.
    
    of controlled object.
    
    After creation the service adds a listener of requested type ( close, terminate and/or etc. ) to the controlled object and let the listener throw related veto exception until the service is disposed.

    See Also:
        `API InstanceLocker <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1embed_1_1InstanceLocker.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.InstanceLocker'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def InstanceLockerCtor1(self, xInstance: 'XInterface_8f010a43', nActions: int) -> None:
        """
        is used to initialize the object on it's creation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.frame.DoubleInitializationException: ``DoubleInitializationException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def InstanceLockerCtor2(self, xInstance: 'XInterface_8f010a43', nActions: int, xApprove: 'XActionsApproval_ed4b0d73') -> None:
        """
        is used to initialize the object on it's creation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.frame.DoubleInitializationException: ``DoubleInitializationException``
            com.sun.star.uno.Exception: ``Exception``
        """


__all__ = ['InstanceLocker']

