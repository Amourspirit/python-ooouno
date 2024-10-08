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
# Namespace: com.sun.star.auth
from __future__ import annotations
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSSOContext(XInterface_8f010a43):
    """
    Base SSO security context representation.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XSSOContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1auth_1_1XSSOContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.auth'
    __ooo_full_ns__: str = 'com.sun.star.auth.XSSOContext'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.auth.XSSOContext'

    @abstractmethod
    def getMechanism(self) -> str:
        """
        retrieves the mechanism associated with the context.
        """
        ...
    @abstractmethod
    def getMutual(self) -> bool:
        """
        retrieves whether or not the context supports mutual authentication
        """
        ...
    @abstractmethod
    def getSource(self) -> str:
        """
        retrieves the principal name of the source/initiator of the context.
        
        In the case of an acceptor side security context, the source principal name is available only after the initiator has been authenticated.
        """
        ...
    @abstractmethod
    def getTarget(self) -> str:
        """
        retrieves the principal name of the target/acceptor of the context.
        """
        ...

__all__ = ['XSSOContext']

