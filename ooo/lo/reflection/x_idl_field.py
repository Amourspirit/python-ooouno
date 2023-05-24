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
# Namespace: com.sun.star.reflection
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_idl_member import XIdlMember as XIdlMember_e3400cfc
if typing.TYPE_CHECKING:
    from .x_idl_class import XIdlClass as XIdlClass_d63a0c9a
    from com.sun.star.reflection.FieldAccessMode import FieldAccessModeProto

class XIdlField(XIdlMember_e3400cfc):
    """
    Deprecated.
    
    Use com.sun.star.reflection.XIdlField2 instead.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XIdlField <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XIdlField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.XIdlField'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.reflection.XIdlField'

    @abstractmethod
    def get(self, obj: object) -> object:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getAccessMode(self) -> FieldAccessModeProto:
        """
        """
        ...
    @abstractmethod
    def getType(self) -> XIdlClass_d63a0c9a:
        """
        """
        ...
    @abstractmethod
    def set(self, obj: object, value: object) -> None:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
        ...

__all__ = ['XIdlField']

