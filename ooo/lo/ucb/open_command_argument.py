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
from ..beans.property import Property as Property_8f4e0a76
from ..uno.x_interface import XInterface as XInterface_8f010a43


class OpenCommandArgument(object):
    """
    Struct Class

    The argument for commands like \"open\", \"update\", and \"synchronize\".

    See Also:
        `API OpenCommandArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1OpenCommandArgument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.OpenCommandArgument'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.OpenCommandArgument'
    """Literal Constant ``com.sun.star.ucb.OpenCommandArgument``"""

    def __init__(self, Properties: typing.Tuple[Property_8f4e0a76, ...] = UNO_NONE, Mode: int = 0, Priority: int = 0, Sink: XInterface_8f010a43 = None) -> None:
        """
        Constructor

        Other Arguments:
            ``Properties`` can be another ``OpenCommandArgument`` instance,
                in which case other named args are ignored.

        Arguments:
            Properties (Tuple[Property, ...], optional): Properties value
            Mode (int, optional): Mode value
            Priority (int, optional): Priority value
            Sink (XInterface, optional): Sink value
        """
        if isinstance(Properties, OpenCommandArgument):
            oth: OpenCommandArgument = Properties
            self._properties = oth.Properties
            self._mode = oth.Mode
            self._priority = oth.Priority
            self._sink = oth.Sink
            return
        else:
            if Properties is UNO_NONE:
                self._properties = None
            else:
                self._properties = Properties
            self._mode = Mode
            self._priority = Priority
            self._sink = Sink



    @property
    def Properties(self) -> typing.Tuple[Property_8f4e0a76, ...]:
        """
        The properties, for that the values shall be provided by the DynamicResultSet returned by the command).
        """
        return self._properties
    
    @Properties.setter
    def Properties(self, value: typing.Tuple[Property_8f4e0a76, ...]) -> None:
        self._properties = value

    @property
    def Mode(self) -> int:
        """
        A mode.
        
        The value can be one of the OpenMode constants.
        """
        return self._mode
    
    @Mode.setter
    def Mode(self, value: int) -> None:
        self._mode = value

    @property
    def Priority(self) -> int:
        """
        The command's priority, in the range 0 (highest) to 65535 (lowest).
        """
        return self._priority
    
    @Priority.setter
    def Priority(self, value: int) -> None:
        self._priority = value

    @property
    def Sink(self) -> XInterface_8f010a43:
        """
        The data sink to write the contents into (supporting either com.sun.star.io.XActiveDataSink, com.sun.star.io.XOutputStream or com.sun.star.io.XActiveDataStreamer).
        
        XActiveDataSink and XOutputStream give the caller read-only access to the contents. XActiveDataStreamer offers both read and write access to the contents.
        
        If an XActiveDataSink is supplied, the implementation of the command needs to provide an implementation of an object implementing the interface com.sun.star.io.XInputStream. It is highly recommended that this object also implements the interface com.sun.star.io.XSeekable, if this can be done without wasting resources (i.e. allocating huge memory buffers). The implementation object has to be supplied to the data sink.
        """
        return self._sink
    
    @Sink.setter
    def Sink(self, value: XInterface_8f010a43) -> None:
        self._sink = value


__all__ = ['OpenCommandArgument']