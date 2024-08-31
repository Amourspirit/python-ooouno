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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class ClipboardFormats(object):
    """
    Struct Class

    contains a list of format IDs and names which are part of the system clipboard.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ClipboardFormats <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1ClipboardFormats.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.ClipboardFormats'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.ClipboardFormats'
    """Literal Constant ``com.sun.star.frame.status.ClipboardFormats``"""

    def __init__(self, Identifiers: typing.Optional[typing.Tuple[int, ...]] = (), Names: typing.Optional[typing.Tuple[str, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Identifiers (typing.Tuple[int, ...], optional): Identifiers value.
            Names (typing.Tuple[str, ...], optional): Names value.
        """
        super().__init__()

        if isinstance(Identifiers, ClipboardFormats):
            oth: ClipboardFormats = Identifiers
            self.Identifiers = oth.Identifiers
            self.Names = oth.Names
            return

        kargs = {
            "Identifiers": Identifiers,
            "Names": Names,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._identifiers = kwargs["Identifiers"]
        self._names = kwargs["Names"]


    @property
    def Identifiers(self) -> typing.Tuple[int, ...]:
        """
        specifies a sequence of format IDs which are contained in the system clipboard.
        """
        return self._identifiers

    @Identifiers.setter
    def Identifiers(self, value: typing.Tuple[int, ...]) -> None:
        self._identifiers = value

    @property
    def Names(self) -> typing.Tuple[str, ...]:
        """
        specifies a sequence of format names which are contained in the system clipboard.
        """
        return self._names

    @Names.setter
    def Names(self, value: typing.Tuple[str, ...]) -> None:
        self._names = value


__all__ = ['ClipboardFormats']
