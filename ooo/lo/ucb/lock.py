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
from .lock_entry import LockEntry as LockEntry_839e09dd
import typing
from .lock_depth import LockDepth as LockDepth_835c09c0


class Lock(LockEntry_839e09dd):
    """
    Struct Class

    defines a lock.

    See Also:
        `API Lock <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1Lock.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.Lock'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.Lock'
    """Literal Constant ``com.sun.star.ucb.Lock``"""

    def __init__(self, LockTokens: typing.Tuple[str, ...] = UNO_NONE, Depth: LockDepth_835c09c0 = LockDepth_835c09c0.ZERO, Owner: object = None, Timeout: int = 0, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``LockTokens`` can be another ``Lock`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            LockTokens (Tuple[str, ...], optional): LockTokens value
            Depth (LockDepth, optional): Depth value
            Owner (object, optional): Owner value
            Timeout (int, optional): Timeout value
        """
        super().__init__(**kwargs)
        if isinstance(LockTokens, Lock):
            oth: Lock = LockTokens
            self._lock_tokens = oth.LockTokens
            self._depth = oth.Depth
            self._owner = oth.Owner
            self._timeout = oth.Timeout
            return
        else:
            if LockTokens is UNO_NONE:
                self._lock_tokens = None
            else:
                self._lock_tokens = LockTokens
            self._depth = Depth
            self._owner = Owner
            self._timeout = Timeout



    @property
    def LockTokens(self) -> typing.Tuple[str, ...]:
        """
        the lock tokens.
        
        Each lock token is a URI.
        """
        return self._lock_tokens
    
    @LockTokens.setter
    def LockTokens(self, value: typing.Tuple[str, ...]) -> None:
        self._lock_tokens = value

    @property
    def Depth(self) -> LockDepth_835c09c0:
        """
        defines the lock's depth.
        """
        return self._depth
    
    @Depth.setter
    def Depth(self, value: LockDepth_835c09c0) -> None:
        self._depth = value

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


__all__ = ['Lock']