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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from .open_command_argument import OpenCommandArgument as OpenCommandArgument_fb0a0dd6
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..beans.property import Property as Property_8f4e0a76
import typing
from .numbered_sorting_info import NumberedSortingInfo as NumberedSortingInfo_fd0e0de6


class OpenCommandArgument2(OpenCommandArgument_fb0a0dd6):
    """
    Struct Class

    The argument for commands like \"open\", \"update\", and \"synchronize\".
    
    This struct extends the original OpenCommandArgument, which must not be changed for compatibility reasons.

    See Also:
        `API OpenCommandArgument2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1OpenCommandArgument2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.OpenCommandArgument2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.OpenCommandArgument2'
    """Literal Constant ``com.sun.star.ucb.OpenCommandArgument2``"""

    def __init__(self, Mode: typing.Optional[int] = 0, Priority: typing.Optional[int] = 0, Sink: typing.Optional[XInterface_8f010a43] = None, Properties: typing.Optional[typing.Tuple[Property_8f4e0a76, ...]] = (), SortingInfo: typing.Optional[typing.Tuple[NumberedSortingInfo_fd0e0de6, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Mode (int, optional): Mode value.
            Priority (int, optional): Priority value.
            Sink (XInterface, optional): Sink value.
            Properties (typing.Tuple[Property, ...], optional): Properties value.
            SortingInfo (typing.Tuple[NumberedSortingInfo, ...], optional): SortingInfo value.
        """

        if isinstance(Mode, OpenCommandArgument2):
            oth: OpenCommandArgument2 = Mode
            self.Mode = oth.Mode
            self.Priority = oth.Priority
            self.Sink = oth.Sink
            self.Properties = oth.Properties
            self.SortingInfo = oth.SortingInfo
            return

        kargs = {
            "Mode": Mode,
            "Priority": Priority,
            "Sink": Sink,
            "Properties": Properties,
            "SortingInfo": SortingInfo,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._sorting_info = kwargs["SortingInfo"]
        inst_keys = ('SortingInfo',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def SortingInfo(self) -> typing.Tuple[NumberedSortingInfo_fd0e0de6, ...]:
        """
        The sort criteria for the rows of the returned ContentResultSet.
        
        The result set implementation may ignore this parameter, if it cannot sort the data by the given criteria in an efficient way (i.e. directly using the underlying data source -> SQL-database -> ORDER BY).
        """
        return self._sorting_info

    @SortingInfo.setter
    def SortingInfo(self, value: typing.Tuple[NumberedSortingInfo_fd0e0de6, ...]) -> None:
        self._sorting_info = value


__all__ = ['OpenCommandArgument2']
