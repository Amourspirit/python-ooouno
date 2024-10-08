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
# Namespace: com.sun.star.sheet
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class DataPilotFieldFilter(object):
    """
    Struct Class


    See Also:
        `API DataPilotFieldFilter <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldFilter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldFilter'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DataPilotFieldFilter'
    """Literal Constant ``com.sun.star.sheet.DataPilotFieldFilter``"""

    def __init__(self, FieldName: typing.Optional[str] = '', MatchValueName: typing.Optional[str] = '', MatchValue: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            FieldName (str, optional): FieldName value.
            MatchValueName (str, optional): MatchValueName value.
            MatchValue (str, optional): MatchValue value.
        """
        super().__init__()

        if isinstance(FieldName, DataPilotFieldFilter):
            oth: DataPilotFieldFilter = FieldName
            self.FieldName = oth.FieldName
            self.MatchValueName = oth.MatchValueName
            self.MatchValue = oth.MatchValue
            return

        kargs = {
            "FieldName": FieldName,
            "MatchValueName": MatchValueName,
            "MatchValue": MatchValue,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._field_name = kwargs["FieldName"]
        self._match_value_name = kwargs["MatchValueName"]
        self._match_value = kwargs["MatchValue"]


    @property
    def FieldName(self) -> str:
        """
        Field name.
        """
        return self._field_name

    @FieldName.setter
    def FieldName(self, value: str) -> None:
        self._field_name = value

    @property
    def MatchValueName(self) -> str:
        """
        String value that needs to match against, locale dependent.
        
        This is the value as name/label as also displayed in the filter popup dialog, maybe formatted by user applied number formats.
        """
        return self._match_value_name

    @MatchValueName.setter
    def MatchValueName(self, value: str) -> None:
        self._match_value_name = value

    @property
    def MatchValue(self) -> str:
        """
        String value that needs to match against, locale independent.
        
        This is the underlying value formatted in a standardized way, for example ISO 8601 YYYY-MM-DD for dates.
        """
        return self._match_value

    @MatchValue.setter
    def MatchValue(self, value: str) -> None:
        self._match_value = value


__all__ = ['DataPilotFieldFilter']
