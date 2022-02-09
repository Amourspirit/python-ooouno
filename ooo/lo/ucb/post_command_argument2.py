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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from .post_command_argument import PostCommandArgument as PostCommandArgument_fc590dea


class PostCommandArgument2(PostCommandArgument_fc590dea):
    """
    Struct Class

    The argument for the command \"post\".

    See Also:
        `API PostCommandArgument2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1PostCommandArgument2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.PostCommandArgument2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.PostCommandArgument2'
    """Literal Constant ``com.sun.star.ucb.PostCommandArgument2``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``PostCommandArgument2`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``PostCommandArgument2``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            MediaType (str, optional): MediaType value
            Referer (str, optional): Referer value
        """
        self._media_type = None
        self._referer = None

        key_order = ('MediaType', 'Referer')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], PostCommandArgument2):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("PostCommandArgument2.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def MediaType(self) -> str:
        """
        The media type (mime type) for the data to post.
        """
        return self._media_type
    
    @MediaType.setter
    def MediaType(self, value: str) -> None:
        self._media_type = value

    @property
    def Referer(self) -> str:
        """
        The URL of the referrer.
        """
        return self._referer
    
    @Referer.setter
    def Referer(self, value: str) -> None:
        self._referer = value


__all__ = ['PostCommandArgument2']
