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
# Namespace: com.sun.star.util
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class AliasProgrammaticPair(object):
    """
    Struct Class

    represents an entry from a component which implements the XLocalizedAliases.

    See Also:
        `API AliasProgrammaticPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1AliasProgrammaticPair.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.AliasProgrammaticPair'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.AliasProgrammaticPair'
    """Literal Constant ``com.sun.star.util.AliasProgrammaticPair``"""

    def __init__(self, Alias: typing.Optional[str] = '', ProgrammaticName: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Alias (str, optional): Alias value.
            ProgrammaticName (str, optional): ProgrammaticName value.
        """
        super().__init__()

        if isinstance(Alias, AliasProgrammaticPair):
            oth: AliasProgrammaticPair = Alias
            self.Alias = oth.Alias
            self.ProgrammaticName = oth.ProgrammaticName
            return

        kargs = {
            "Alias": Alias,
            "ProgrammaticName": ProgrammaticName,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._alias = kwargs["Alias"]
        self._programmatic_name = kwargs["ProgrammaticName"]


    @property
    def Alias(self) -> str:
        """
        determines the name which is registered as an alias for a programmatic name.
        """
        return self._alias

    @Alias.setter
    def Alias(self, value: str) -> None:
        self._alias = value

    @property
    def ProgrammaticName(self) -> str:
        """
        determines which programmatic name belongs to the alias.
        """
        return self._programmatic_name

    @ProgrammaticName.setter
    def ProgrammaticName(self, value: str) -> None:
        self._programmatic_name = value


__all__ = ['AliasProgrammaticPair']
