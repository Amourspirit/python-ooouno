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
# Namespace: com.sun.star.sdbcx
from __future__ import annotations
from abc import abstractmethod
from .x_authorizable import XAuthorizable as XAuthorizable_c8dd0c5e

class XUser(XAuthorizable_c8dd0c5e):
    """
    allows for changing a users password.

    See Also:
        `API XUser <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XUser.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.XUser'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbcx.XUser'

    @abstractmethod
    def changePassword(self, oldPassword: str, newPassword: str) -> None:
        """
        allows modifying a user password.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...

__all__ = ['XUser']

