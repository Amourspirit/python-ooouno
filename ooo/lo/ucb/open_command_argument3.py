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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from .open_command_argument2 import OpenCommandArgument2 as OpenCommandArgument2_9210e08
from ..beans.property import Property as Property_8f4e0a76
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .numbered_sorting_info import NumberedSortingInfo as NumberedSortingInfo_fd0e0de6
import typing
from ..beans.named_value import NamedValue as NamedValue_a37a0af3


class OpenCommandArgument3(OpenCommandArgument2_9210e08):
    """
    Struct Class

    Extended argument for commands like \"open\".
    
    We're extending OpenCommandArgument even more, to provide some opening flags on to webdav.

    See Also:
        `API OpenCommandArgument3 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1OpenCommandArgument3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.OpenCommandArgument3'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.OpenCommandArgument3'
    """Literal Constant ``com.sun.star.ucb.OpenCommandArgument3``"""

    def __init__(self, Properties: typing.Optional[typing.Tuple[Property_8f4e0a76, ...]] = (), Mode: typing.Optional[int] = 0, Priority: typing.Optional[int] = 0, Sink: typing.Optional[XInterface_8f010a43] = None, SortingInfo: typing.Optional[typing.Tuple[NumberedSortingInfo_fd0e0de6, ...]] = (), OpeningFlags: typing.Optional[typing.Tuple[NamedValue_a37a0af3, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Properties (typing.Tuple[Property, ...], optional): Properties value.
            Mode (int, optional): Mode value.
            Priority (int, optional): Priority value.
            Sink (XInterface, optional): Sink value.
            SortingInfo (typing.Tuple[NumberedSortingInfo, ...], optional): SortingInfo value.
            OpeningFlags (typing.Tuple[NamedValue, ...], optional): OpeningFlags value.
        """

        if isinstance(Properties, OpenCommandArgument3):
            oth: OpenCommandArgument3 = Properties
            self.Properties = oth.Properties
            self.Mode = oth.Mode
            self.Priority = oth.Priority
            self.Sink = oth.Sink
            self.SortingInfo = oth.SortingInfo
            self.OpeningFlags = oth.OpeningFlags
            return

        kargs = {
            "Properties": Properties,
            "Mode": Mode,
            "Priority": Priority,
            "Sink": Sink,
            "SortingInfo": SortingInfo,
            "OpeningFlags": OpeningFlags,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._opening_flags = kwargs["OpeningFlags"]
        inst_keys = ('OpeningFlags',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def OpeningFlags(self) -> typing.Tuple[NamedValue_a37a0af3, ...]:
        """
        Flags to use for opening.
        
        WebDav e.g. uses \"KeepAlive\" to enable/disable the respective http feature.
        """
        return self._opening_flags
    
    @OpeningFlags.setter
    def OpeningFlags(self, value: typing.Tuple[NamedValue_a37a0af3, ...]) -> None:
        self._opening_flags = value


__all__ = ['OpenCommandArgument3']
