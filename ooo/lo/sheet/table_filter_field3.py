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
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from .filter_connection import FilterConnection as FilterConnection_f01f0d97
from .filter_field_value import FilterFieldValue as FilterFieldValue_ef2a0d68


class TableFilterField3(object):
    """
    Struct Class

    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API TableFilterField3 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1TableFilterField3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.TableFilterField3'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.TableFilterField3'
    """Literal Constant ``com.sun.star.sheet.TableFilterField3``"""

    def __init__(self, Values: typing.Optional[typing.Tuple[FilterFieldValue_ef2a0d68, ...]] = (), Connection: typing.Optional[FilterConnection_f01f0d97] = FilterConnection_f01f0d97.AND, Field: typing.Optional[int] = 0, Operator: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Values (typing.Tuple[FilterFieldValue, ...], optional): Values value.
            Connection (FilterConnection, optional): Connection value.
            Field (int, optional): Field value.
            Operator (int, optional): Operator value.
        """
        super().__init__()

        if isinstance(Values, TableFilterField3):
            oth: TableFilterField3 = Values
            self.Values = oth.Values
            self.Connection = oth.Connection
            self.Field = oth.Field
            self.Operator = oth.Operator
            return

        kargs = {
            "Values": Values,
            "Connection": Connection,
            "Field": Field,
            "Operator": Operator,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._values = kwargs["Values"]
        self._connection = kwargs["Connection"]
        self._field = kwargs["Field"]
        self._operator = kwargs["Operator"]


    @property
    def Values(self) -> typing.Tuple[FilterFieldValue_ef2a0d68, ...]:
        """
        specifies values to match against.
        
        Each filter field may have one or more values.
        """
        return self._values
    
    @Values.setter
    def Values(self, value: typing.Tuple[FilterFieldValue_ef2a0d68, ...]) -> None:
        self._values = value

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
    def Operator(self) -> int:
        """
        specifies the type of the condition as defined in FilterOperator2.
        """
        return self._operator
    
    @Operator.setter
    def Operator(self, value: int) -> None:
        self._operator = value


__all__ = ['TableFilterField3']
