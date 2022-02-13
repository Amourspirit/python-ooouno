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
import typing
from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
from ..uno.x_interface import XInterface as XInterface_8f010a43


class PostCommandArgument(object):
    """
    Struct Class

    The argument for the command \"post\".

    See Also:
        `API PostCommandArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1PostCommandArgument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.PostCommandArgument'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.PostCommandArgument'
    """Literal Constant ``com.sun.star.ucb.PostCommandArgument``"""

    def __init__(self, Source: XInputStream_98d40ab4 = None, Sink: XInterface_8f010a43 = None) -> None:
        """
        Constructor

        Other Arguments:
            ``Source`` can be another ``PostCommandArgument`` instance,
                in which case other named args are ignored.

        Arguments:
            Source (XInputStream, optional): Source value
            Sink (XInterface, optional): Sink value
        """
        if isinstance(Source, PostCommandArgument):
            oth: PostCommandArgument = Source
            self._source = oth.Source
            self._sink = oth.Sink
            return
        else:
            self._source = Source
            self._sink = Sink



    @property
    def Source(self) -> XInputStream_98d40ab4:
        """
        The data source containing the data to post.
        """
        return self._source
    
    @Source.setter
    def Source(self, value: XInputStream_98d40ab4) -> None:
        self._source = value

    @property
    def Sink(self) -> XInterface_8f010a43:
        """
        The data sink receiving the returned contents (supporting either com.sun.star.io.XActiveDataSink or com.sun.star.io.XOutputStream).
        """
        return self._sink
    
    @Sink.setter
    def Sink(self, value: XInterface_8f010a43) -> None:
        self._sink = value


__all__ = ['PostCommandArgument']
