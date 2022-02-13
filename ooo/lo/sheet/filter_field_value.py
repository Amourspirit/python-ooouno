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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..util.color import Color as Color_68e908c5


class FilterFieldValue(object):
    """
    Struct Class

    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API FilterFieldValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1FilterFieldValue.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FilterFieldValue'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.FilterFieldValue'
    """Literal Constant ``com.sun.star.sheet.FilterFieldValue``"""

    def __init__(self, IsNumeric: bool = False, NumericValue: float = 0.0, StringValue: str = '', FilterType: int = None, ColorValue: Color_68e908c5 = None) -> None:
        """
        Constructor

        Other Arguments:
            ``IsNumeric`` can be another ``FilterFieldValue`` instance,
                in which case other named args are ignored.

        Arguments:
            IsNumeric (bool, optional): IsNumeric value
            NumericValue (float, optional): NumericValue value
            StringValue (str, optional): StringValue value
            FilterType (int, optional): FilterType value
            ColorValue (Color, optional): ColorValue value
        """
        if isinstance(IsNumeric, FilterFieldValue):
            oth: FilterFieldValue = IsNumeric
            self._is_numeric = oth.IsNumeric
            self._numeric_value = oth.NumericValue
            self._string_value = oth.StringValue
            self._filter_type = oth.FilterType
            self._color_value = oth.ColorValue
            return
        else:
            self._is_numeric = IsNumeric
            self._numeric_value = NumericValue
            self._string_value = StringValue
            self._filter_type = FilterType
            self._color_value = ColorValue



    @property
    def IsNumeric(self) -> bool:
        """
        selects whether the TableFilterFieldValue.NumericValue or the TableFilterFieldValue.StringValue is used.
        """
        return self._is_numeric
    
    @IsNumeric.setter
    def IsNumeric(self, value: bool) -> None:
        self._is_numeric = value

    @property
    def NumericValue(self) -> float:
        """
        specifies a numeric value for the condition.
        """
        return self._numeric_value
    
    @NumericValue.setter
    def NumericValue(self, value: float) -> None:
        self._numeric_value = value

    @property
    def StringValue(self) -> str:
        """
        specifies a string value for the condition.
        """
        return self._string_value
    
    @StringValue.setter
    def StringValue(self, value: str) -> None:
        self._string_value = value

    @property
    def FilterType(self) -> int:
        """
        Which field should be used for filtering:
        
        **since**
        
            LibreOffice 7.2
        """
        return self._filter_type
    
    @FilterType.setter
    def FilterType(self, value: int) -> None:
        self._filter_type = value

    @property
    def ColorValue(self) -> Color_68e908c5:
        """
        The color which is used for filtering.
        
        **since**
        
            LibreOffice 7.2
        """
        return self._color_value
    
    @ColorValue.setter
    def ColorValue(self, value: Color_68e908c5) -> None:
        self._color_value = value


__all__ = ['FilterFieldValue']
