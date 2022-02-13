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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.task
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class UserRecord(object):
    """
    Struct Class


    See Also:
        `API UserRecord <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1task_1_1UserRecord.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.UserRecord'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.task.UserRecord'
    """Literal Constant ``com.sun.star.task.UserRecord``"""

    def __init__(self, Passwords: typing.Tuple[str, ...] = UNO_NONE, UserName: str = '') -> None:
        """
        Constructor

        Other Arguments:
            ``Passwords`` can be another ``UserRecord`` instance,
                in which case other named args are ignored.

        Arguments:
            Passwords (Tuple[str, ...], optional): Passwords value
            UserName (str, optional): UserName value
        """
        if isinstance(Passwords, UserRecord):
            oth: UserRecord = Passwords
            self._passwords = oth.Passwords
            self._user_name = oth.UserName
            return
        else:
            if Passwords is UNO_NONE:
                self._passwords = None
            else:
                self._passwords = Passwords
            self._user_name = UserName



    @property
    def Passwords(self) -> typing.Tuple[str, ...]:
        """
        specifies the passwords for the given user.
        """
        return self._passwords
    
    @Passwords.setter
    def Passwords(self, value: typing.Tuple[str, ...]) -> None:
        self._passwords = value

    @property
    def UserName(self) -> str:
        """
        specifies the user name.
        """
        return self._user_name
    
    @UserName.setter
    def UserName(self, value: str) -> None:
        self._user_name = value


__all__ = ['UserRecord']
