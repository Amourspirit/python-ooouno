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
from ooo.oenv.env_const import UNO_NONE
from .post_command_argument import PostCommandArgument as PostCommandArgument_fc590dea
from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
from ..uno.x_interface import XInterface as XInterface_8f010a43
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

    def __init__(self, Source: typing.Optional[XInputStream_98d40ab4] = None, Sink: typing.Optional[XInterface_8f010a43] = None, MediaType: typing.Optional[str] = '', Referer: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Source (XInputStream, optional): Source value.
            Sink (XInterface, optional): Sink value.
            MediaType (str, optional): MediaType value.
            Referer (str, optional): Referer value.
        """

        if isinstance(Source, PostCommandArgument2):
            oth: PostCommandArgument2 = Source
            self.Source = oth.Source
            self.Sink = oth.Sink
            self.MediaType = oth.MediaType
            self.Referer = oth.Referer
            return

        kargs = {
            "Source": Source,
            "Sink": Sink,
            "MediaType": MediaType,
            "Referer": Referer,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._media_type = kwargs["MediaType"]
        self._referer = kwargs["Referer"]
        inst_keys = ('MediaType', 'Referer')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


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
