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
from ooo.oenv import UNO_NONE
from .post_command_argument import PostCommandArgument as PostCommandArgument_fc590dea
import typing


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

    def __init__(self, MediaType: str = '', Referer: str = '', **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``MediaType`` can be another ``PostCommandArgument2`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            MediaType (str, optional): MediaType value
            Referer (str, optional): Referer value
        """
        super().__init__(**kwargs)
        if isinstance(MediaType, PostCommandArgument2):
            oth: PostCommandArgument2 = MediaType
            self._media_type = oth.MediaType
            self._referer = oth.Referer
            return
        else:
            self._media_type = MediaType
            self._referer = Referer



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