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
# Namespace: com.sun.star.i18n
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class NumberFormatCode(object):
    """
    Struct Class

    Number format code information returned by various XNumberFormatCode methods.

    See Also:
        `API NumberFormatCode <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1NumberFormatCode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.NumberFormatCode'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.NumberFormatCode'
    """Literal Constant ``com.sun.star.i18n.NumberFormatCode``"""

    def __init__(self, Type: typing.Optional[int] = 0, Usage: typing.Optional[int] = 0, Code: typing.Optional[str] = '', DefaultName: typing.Optional[str] = '', NameID: typing.Optional[str] = '', Index: typing.Optional[int] = 0, Default: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Type (int, optional): Type value.
            Usage (int, optional): Usage value.
            Code (str, optional): Code value.
            DefaultName (str, optional): DefaultName value.
            NameID (str, optional): NameID value.
            Index (int, optional): Index value.
            Default (bool, optional): Default value.
        """
        super().__init__()

        if isinstance(Type, NumberFormatCode):
            oth: NumberFormatCode = Type
            self.Type = oth.Type
            self.Usage = oth.Usage
            self.Code = oth.Code
            self.DefaultName = oth.DefaultName
            self.NameID = oth.NameID
            self.Index = oth.Index
            self.Default = oth.Default
            return

        kargs = {
            "Type": Type,
            "Usage": Usage,
            "Code": Code,
            "DefaultName": DefaultName,
            "NameID": NameID,
            "Index": Index,
            "Default": Default,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._type = kwargs["Type"]
        self._usage = kwargs["Usage"]
        self._code = kwargs["Code"]
        self._default_name = kwargs["DefaultName"]
        self._name_id = kwargs["NameID"]
        self._index = kwargs["Index"]
        self._default = kwargs["Default"]


    @property
    def Type(self) -> int:
        """
        One of KNumberFormatType values.
        """
        return self._type

    @Type.setter
    def Type(self, value: int) -> None:
        self._type = value

    @property
    def Usage(self) -> int:
        """
        One of KNumberFormatUsage values.
        """
        return self._usage

    @Usage.setter
    def Usage(self, value: int) -> None:
        self._usage = value

    @property
    def Code(self) -> str:
        """
        Format code, for example, \"YYYY-MM-DD\".
        """
        return self._code

    @Code.setter
    def Code(self, value: str) -> None:
        self._code = value

    @property
    def DefaultName(self) -> str:
        """
        Descriptive name of the format for this locale.
        """
        return self._default_name

    @DefaultName.setter
    def DefaultName(self, value: str) -> None:
        self._default_name = value

    @property
    def NameID(self) -> str:
        """
        Message identifier to be used if the name of the format is localized.
        """
        return self._name_id

    @NameID.setter
    def NameID(self, value: str) -> None:
        self._name_id = value

    @property
    def Index(self) -> int:
        """
        Index of the code as defined in NumberFormatIndex.
        """
        return self._index

    @Index.setter
    def Index(self, value: int) -> None:
        self._index = value

    @property
    def Default(self) -> bool:
        """
        If this format is the default format of the Usage group.
        """
        return self._default

    @Default.setter
    def Default(self, value: bool) -> None:
        self._default = value


__all__ = ['NumberFormatCode']
