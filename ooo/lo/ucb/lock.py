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
from .lock_entry import LockEntry as LockEntry_839e09dd
from .lock_scope import LockScope as LockScope_839109c5
from .lock_type import LockType as LockType_7a09096d
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

    def __init__(self, Scope: typing.Optional[LockScope_839109c5] = LockScope_839109c5.EXCLUSIVE, Type: typing.Optional[LockType_7a09096d] = LockType_7a09096d.WRITE, Depth: typing.Optional[LockDepth_835c09c0] = LockDepth_835c09c0.ZERO, Owner: typing.Optional[object] = None, Timeout: typing.Optional[int] = 0, LockTokens: typing.Optional[typing.Tuple[str, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Scope (LockScope, optional): Scope value.
            Type (LockType, optional): Type value.
            Depth (LockDepth, optional): Depth value.
            Owner (object, optional): Owner value.
            Timeout (int, optional): Timeout value.
            LockTokens (typing.Tuple[str, ...], optional): LockTokens value.
        """

        if isinstance(Scope, Lock):
            oth: Lock = Scope
            self.Scope = oth.Scope
            self.Type = oth.Type
            self.Depth = oth.Depth
            self.Owner = oth.Owner
            self.Timeout = oth.Timeout
            self.LockTokens = oth.LockTokens
            return

        kargs = {
            "Scope": Scope,
            "Type": Type,
            "Depth": Depth,
            "Owner": Owner,
            "Timeout": Timeout,
            "LockTokens": LockTokens,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._depth = kwargs["Depth"]
        self._owner = kwargs["Owner"]
        self._timeout = kwargs["Timeout"]
        self._lock_tokens = kwargs["LockTokens"]
        inst_keys = ('Depth', 'Owner', 'Timeout', 'LockTokens')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


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


__all__ = ['Lock']
