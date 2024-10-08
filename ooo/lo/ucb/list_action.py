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
import typing


class ListAction(object):
    """
    Struct Class

    This struct contains information needed in the notifications of a XDynamicResultSet.

    See Also:
        `API ListAction <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1ListAction.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.ListAction'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.ListAction'
    """Literal Constant ``com.sun.star.ucb.ListAction``"""

    def __init__(self, Position: typing.Optional[int] = 0, Count: typing.Optional[int] = 0, ListActionType: typing.Optional[int] = 0, ActionInfo: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Position (int, optional): Position value.
            Count (int, optional): Count value.
            ListActionType (int, optional): ListActionType value.
            ActionInfo (object, optional): ActionInfo value.
        """
        super().__init__()

        if isinstance(Position, ListAction):
            oth: ListAction = Position
            self.Position = oth.Position
            self.Count = oth.Count
            self.ListActionType = oth.ListActionType
            self.ActionInfo = oth.ActionInfo
            return

        kargs = {
            "Position": Position,
            "Count": Count,
            "ListActionType": ListActionType,
            "ActionInfo": ActionInfo,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._position = kwargs["Position"]
        self._count = kwargs["Count"]
        self._list_action_type = kwargs["ListActionType"]
        self._action_info = kwargs["ActionInfo"]


    @property
    def Position(self) -> int:
        """
        The position where something has happened (index begins with 1 as usual with JDBC ).
        
        Its value does not necessary indicate the new position in the new com.sun.star.sdbc.XResultSet, but a position while doing the changes step by step beginning with the old com.sun.star.sdbc.XResultSet.
        """
        return self._position

    @Position.setter
    def Position(self, value: int) -> None:
        self._position = value

    @property
    def Count(self) -> int:
        """
        The count of involved rows.
        """
        return self._count

    @Count.setter
    def Count(self, value: int) -> None:
        self._count = value

    @property
    def ListActionType(self) -> int:
        """
        specifies the kind of modification happened to all assigned rows.
        
        The value of the other members of this struct depend on the value of this member:
        """
        return self._list_action_type

    @ListActionType.setter
    def ListActionType(self, value: int) -> None:
        self._list_action_type = value

    @property
    def ActionInfo(self) -> object:
        """
        depending on the content of ListAction.ListActionType the ListAction.ActionInfo could contain additional information about the changes happened (see table above).
        """
        return self._action_info

    @ActionInfo.setter
    def ActionInfo(self, value: object) -> None:
        self._action_info = value


__all__ = ['ListAction']
