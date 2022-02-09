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
from abc import abstractmethod
from .x_interaction_password import XInteractionPassword as XInteractionPassword_1ba00ee6

class XInteractionPassword2(XInteractionPassword_1ba00ee6):
    """
    A continuation to get a password from interaction helper, extends XInteractionPassword with possibility to provide password to modify.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XInteractionPassword2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XInteractionPassword2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XInteractionPassword2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XInteractionPassword2'

    @abstractmethod
    def getPasswordToModify(self) -> str:
        """
        gets \"password to modify\" from the continuation.
        """
    @abstractmethod
    def getRecommendReadOnly(self) -> bool:
        """
        gets \"recommend readonly\" from the continuation.
        
        It specifies whether the document should be loaded readonly per default.
        """
    @abstractmethod
    def setPasswordToModify(self, aPasswd: str) -> None:
        """
        stores \"password to modify\" to the continuation.
        """
    @abstractmethod
    def setRecommendReadOnly(self, bReadOnly: bool) -> None:
        """
        stores \"recommend readonly\" to the continuation.
        
        It specifies whether the document should be loaded readonly per default.
        """


__all__ = ['XInteractionPassword2']

