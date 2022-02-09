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
# Namespace: com.sun.star.auth
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSSOPasswordCache(XInterface_8f010a43):
    """
    supports password caching for security mechanisms which use passwords as credentials or as an input to credential creation but don't have an external method to cache these passwords.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XSSOPasswordCache <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1auth_1_1XSSOPasswordCache.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.auth'
    __ooo_full_ns__: str = 'com.sun.star.auth.XSSOPasswordCache'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.auth.XSSOPasswordCache'

    @abstractmethod
    def addPassword(self, UserName: str, Password: str, Persist: bool) -> None:
        """
        adds a username/password combination to the cache.
        
        If an entry for the specified username already exists in the cache, it will be overwritten.

        Raises:
            InvalidArgumentException: ``InvalidArgumentException``
            PersistenceFailureException: ``PersistenceFailureException``
        """
    @abstractmethod
    def getPassword(self, UserName: str, Persist: bool) -> str:
        """
        retrieves a password for a given user from the cache.
        
        Non persistent cache is searched first, followed by the persistent cache ( if it exists ).

        * ``Persist`` is an out direction argument.

        Raises:
            InvalidArgumentException: ``InvalidArgumentException``
            PersistenceFailureException: ``PersistenceFailureException``
        """
    @abstractmethod
    def removePassword(self, UserName: str, RemovePersist: bool) -> None:
        """
        removes a password from the cache

        Raises:
            InvalidArgumentException: ``InvalidArgumentException``
            PersistenceFailureException: ``PersistenceFailureException``
        """


__all__ = ['XSSOPasswordCache']

