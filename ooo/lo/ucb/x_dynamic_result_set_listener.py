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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .list_event import ListEvent as ListEvent_83fa09e0

class XDynamicResultSetListener(XEventListener_c7230c4a):
    """
    used to receive notifications from an XDynamicResultSet.

    See Also:
        `API XDynamicResultSetListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XDynamicResultSetListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XDynamicResultSetListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XDynamicResultSetListener'

    @abstractmethod
    def notify(self, Changes: ListEvent_83fa09e0) -> None:
        """
        A method used to propagate changes of a result set.
        
        In the first notify-call the listener gets two(!) com.sun.star.sdbc.XResultSets and has to hold them. The com.sun.star.sdbc.XResultSets are implementations of the service ContentResultSet.
        
        The notified new com.sun.star.sdbc.XResultSet will stay valid after returning from this method. The old one will become invalid after returning.
        
        While in notify-call the listener is allowed to read from old and new result set, except in the first call, where only the new result set is valid.
        
        The Listener is allowed to stay (block) this call, until he really wants to use the new result set. The only situation, where the listener has to return immediately is while he disposes his broadcaster or while he is removing himself as listener (otherwise you deadlock)!!!
        """
        ...

__all__ = ['XDynamicResultSetListener']

