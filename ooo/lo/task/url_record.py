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
import typing
if typing.TYPE_CHECKING:
    from .user_record import UserRecord as UserRecord_9a2e0ab9


class UrlRecord(object):
    """
    Struct Class


    See Also:
        `API UrlRecord <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1task_1_1UrlRecord.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.UrlRecord'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.task.UrlRecord'
    """Literal Constant ``com.sun.star.task.UrlRecord``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``UrlRecord`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``UrlRecord``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Url (str, optional): Url value
            UserList (Tuple[UserRecord, ...], optional): UserList value
        """
        self._url = None
        self._user_list = None

        key_order = ('Url', 'UserList')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], UrlRecord):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("UrlRecord.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Url(self) -> str:
        """
        The URL for which these passwords where given.
        """
        return self._url
    
    @Url.setter
    def Url(self, value: str) -> None:
        self._url = value

    @property
    def UserList(self) -> 'typing.Tuple[UserRecord_9a2e0ab9, ...]':
        return self._user_list
    
    @UserList.setter
    def UserList(self, value: 'typing.Tuple[UserRecord_9a2e0ab9, ...]') -> None:
        self._user_list = value


__all__ = ['UrlRecord']
