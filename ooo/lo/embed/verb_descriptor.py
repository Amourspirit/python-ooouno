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
# Namespace: com.sun.star.embed
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class VerbDescriptor(object):
    """
    Struct Class

    describes a verb.

    See Also:
        `API VerbDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1embed_1_1VerbDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.VerbDescriptor'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.embed.VerbDescriptor'
    """Literal Constant ``com.sun.star.embed.VerbDescriptor``"""

    def __init__(self, VerbID: typing.Optional[int] = 0, VerbName: typing.Optional[str] = '', VerbFlags: typing.Optional[int] = 0, VerbAttributes: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            VerbID (int, optional): VerbID value.
            VerbName (str, optional): VerbName value.
            VerbFlags (int, optional): VerbFlags value.
            VerbAttributes (int, optional): VerbAttributes value.
        """
        super().__init__()

        if isinstance(VerbID, VerbDescriptor):
            oth: VerbDescriptor = VerbID
            self.VerbID = oth.VerbID
            self.VerbName = oth.VerbName
            self.VerbFlags = oth.VerbFlags
            self.VerbAttributes = oth.VerbAttributes
            return

        kargs = {
            "VerbID": VerbID,
            "VerbName": VerbName,
            "VerbFlags": VerbFlags,
            "VerbAttributes": VerbAttributes,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._verb_id = kwargs["VerbID"]
        self._verb_name = kwargs["VerbName"]
        self._verb_flags = kwargs["VerbFlags"]
        self._verb_attributes = kwargs["VerbAttributes"]


    @property
    def VerbID(self) -> int:
        """
        specifies the id of the verb.
        """
        return self._verb_id

    @VerbID.setter
    def VerbID(self, value: int) -> None:
        self._verb_id = value

    @property
    def VerbName(self) -> str:
        """
        specifies the name of the verb.
        """
        return self._verb_name

    @VerbName.setter
    def VerbName(self, value: str) -> None:
        self._verb_name = value

    @property
    def VerbFlags(self) -> int:
        """
        specifies the flags that are set for the verb.
        
        The flags can be used to build the verb's menu.
        """
        return self._verb_flags

    @VerbFlags.setter
    def VerbFlags(self, value: int) -> None:
        self._verb_flags = value

    @property
    def VerbAttributes(self) -> int:
        """
        specifies the attributes of the verb.
        
        It can take values from VerbAttributes.
        """
        return self._verb_attributes

    @VerbAttributes.setter
    def VerbAttributes(self, value: int) -> None:
        self._verb_attributes = value


__all__ = ['VerbDescriptor']
