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
# Namespace: com.sun.star.task
import typing
from abc import abstractmethod
from .x_master_password_handling import XMasterPasswordHandling as XMasterPasswordHandling_49900ff7
if typing.TYPE_CHECKING:
    from .x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class XMasterPasswordHandling2(XMasterPasswordHandling_49900ff7):
    """
    allows to change the master password, or let it be requested and checked.

    See Also:
        `API XMasterPasswordHandling2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XMasterPasswordHandling2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XMasterPasswordHandling2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XMasterPasswordHandling2'

    @abstractmethod
    def isDefaultMasterPasswordUsed(self) -> bool:
        """
        allows to detect whether the default master password is used
        """
    @abstractmethod
    def useDefaultMasterPassword(self, xHandler: 'XInteractionHandler_bf80e51') -> bool:
        """
        allows to let the default password be used
        
        Please use this method with care. Using of default master password let the passwords be stored non-encrypted. If a master password is predefined in the algorithm it is no more an encryption, it is just an encoding.
        """


__all__ = ['XMasterPasswordHandling2']

