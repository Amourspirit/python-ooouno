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
import os
from .lock_entry import LockEntry as LockEntry_839e09dd
import typing
if typing.TYPE_CHECKING:
    from .lock_depth import LockDepth as LockDepth_835c09c0
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class Lock(LockEntry_839e09dd):
    """
    Struct Class

    defines a lock.

    See Also:
        `API Lock <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1Lock.html>`_


    Note:
        | At runtime Lock will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | Lock is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Depth: 'typing.Optional[LockDepth_835c09c0]' = None, LockTokens: 'typing.Optional[typing.List[str]]' = None, Owner: typing.Optional[object] = None, Timeout: typing.Optional[int] = None):
        self._depth = Depth
        self._lock_tokens = LockTokens
        self._owner = Owner
        self._timeout = Timeout

    @property
    def Depth(self) -> 'LockDepth_835c09c0':
        """
        defines the lock's depth.
        """
        return self._depth
    
    @Depth.setter
    def Depth(self, value: 'LockDepth_835c09c0') -> None:
        self._depth = value

    @property
    def LockTokens(self) -> 'typing.List[str]':
        """
        the lock tokens.
        
        Each lock token is a URI.
        """
        return self._lock_tokens
    
    @LockTokens.setter
    def LockTokens(self, value: 'typing.List[str]') -> None:
        self._lock_tokens = value

    @property
    def Owner(self) -> object:
        """
        the owner of the lock.
        
        This element provides information sufficient for either directly contacting a principal (such as a telephone number or email URI), or for discovering the principal (such as the URL of a homepage) who owns the lock.
        """
        return self._owner
    
    @Owner.setter
    def Owner(self, value: object) -> None:
        self._owner = value

    @property
    def Timeout(self) -> int:
        """
        a timeout value for the lock.
        
        This element specifies the number of seconds between granting of the lock and the automatic removal of that lock. The value must not be greater than 2^32-1. A value of -1 stands for an infinite lock, that will never be removed automatically.
        """
        return self._timeout
    
    @Timeout.setter
    def Timeout(self, value: int) -> None:
        self._timeout = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global Lock
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Depth', 'LockTokens', 'Owner', 'Timeout')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.ucb.Lock')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        Lock = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['Lock']
