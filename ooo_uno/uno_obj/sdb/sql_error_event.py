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
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.2
import os
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class SQLErrorEvent(EventObject_a3d70b03):
    """
    Struct Class

    is invoked in case of fired database exception triggered by a database object.

    See Also:
        `API SQLErrorEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1SQLErrorEvent.html>`_


    Note:
        | At runtime SQLErrorEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | SQLErrorEvent is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Reason: typing.Optional[object] = None):
        self._reason = Reason

    @property
    def Reason(self) -> object:
        """
        contains the exception that is going to be fired.
        """
        return self._reason
    
    @Reason.setter
    def Reason(self, value: object) -> None:
        self._reason = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global SQLErrorEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Reason',)
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.sdb.SQLErrorEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        SQLErrorEvent = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['SQLErrorEvent']
