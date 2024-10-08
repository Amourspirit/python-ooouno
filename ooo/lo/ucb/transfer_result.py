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


class TransferResult(object):
    """
    Struct Class

    Information about a transfer activity.

    See Also:
        `API TransferResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1TransferResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.TransferResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.TransferResult'
    """Literal Constant ``com.sun.star.ucb.TransferResult``"""

    def __init__(self, Source: typing.Optional[str] = '', Target: typing.Optional[str] = '', Result: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Source (str, optional): Source value.
            Target (str, optional): Target value.
            Result (object, optional): Result value.
        """
        super().__init__()

        if isinstance(Source, TransferResult):
            oth: TransferResult = Source
            self.Source = oth.Source
            self.Target = oth.Target
            self.Result = oth.Result
            return

        kargs = {
            "Source": Source,
            "Target": Target,
            "Result": Result,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._source = kwargs["Source"]
        self._target = kwargs["Target"]
        self._result = kwargs["Result"]


    @property
    def Source(self) -> str:
        """
        The URL of the source object.
        """
        return self._source

    @Source.setter
    def Source(self, value: str) -> None:
        self._source = value

    @property
    def Target(self) -> str:
        """
        The URL of the target folder into which to transfer (a copy of) the source object.
        """
        return self._target

    @Target.setter
    def Target(self, value: str) -> None:
        self._target = value

    @property
    def Result(self) -> object:
        """
        Either void if the transfer has been carried out successfully, or an exception indicating the kind of failure.
        """
        return self._result

    @Result.setter
    def Result(self, value: object) -> None:
        self._result = value


__all__ = ['TransferResult']
