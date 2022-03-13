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
from .filter_connection import FilterConnection as FilterConnection_f01f0d97
from .filter_operator import FilterOperator as FilterOperator_d5c60cd3


class TableFilterField(object):
    """
    Struct Class

    describes a single condition in a filter descriptor.

    See Also:
        `API TableFilterField <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1TableFilterField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.TableFilterField'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.TableFilterField'
    """Literal Constant ``com.sun.star.sheet.TableFilterField``"""

    def __init__(self, Connection: typing.Optional[FilterConnection_f01f0d97] = FilterConnection_f01f0d97.AND, Field: typing.Optional[int] = 0, Operator: typing.Optional[FilterOperator_d5c60cd3] = FilterOperator_d5c60cd3.EMPTY, IsNumeric: typing.Optional[bool] = False, NumericValue: typing.Optional[float] = 0.0, StringValue: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Connection (FilterConnection, optional): Connection value.
            Field (int, optional): Field value.
            Operator (FilterOperator, optional): Operator value.
            IsNumeric (bool, optional): IsNumeric value.
            NumericValue (float, optional): NumericValue value.
            StringValue (str, optional): StringValue value.
        """
        super().__init__()

        if isinstance(Connection, TableFilterField):
            oth: TableFilterField = Connection
            self.Connection = oth.Connection
            self.Field = oth.Field
            self.Operator = oth.Operator
            self.IsNumeric = oth.IsNumeric
            self.NumericValue = oth.NumericValue
            self.StringValue = oth.StringValue
            return

        kargs = {
            "Connection": Connection,
            "Field": Field,
            "Operator": Operator,
            "IsNumeric": IsNumeric,
            "NumericValue": NumericValue,
            "StringValue": StringValue,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._connection = kwargs["Connection"]
        self._field = kwargs["Field"]
        self._operator = kwargs["Operator"]
        self._is_numeric = kwargs["IsNumeric"]
        self._numeric_value = kwargs["NumericValue"]
        self._string_value = kwargs["StringValue"]


    @property
    def Connection(self) -> FilterConnection_f01f0d97:
        """
        specifies how the condition is connected to the previous condition.
        """
        return self._connection
    
    @Connection.setter
    def Connection(self, value: FilterConnection_f01f0d97) -> None:
        self._connection = value

    @property
    def Field(self) -> int:
        """
        specifies which field (column) is used for the condition.
        """
        return self._field
    
    @Field.setter
    def Field(self, value: int) -> None:
        self._field = value

    @property
    def Operator(self) -> FilterOperator_d5c60cd3:
        """
        specifies the type of the condition.
        """
        return self._operator
    
    @Operator.setter
    def Operator(self, value: FilterOperator_d5c60cd3) -> None:
        self._operator = value

    @property
    def IsNumeric(self) -> bool:
        """
        selects whether the TableFilterField.NumericValue or the TableFilterField.StringValue is used.
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


__all__ = ['TableFilterField']
