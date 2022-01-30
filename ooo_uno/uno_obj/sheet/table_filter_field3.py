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
import typing
if typing.TYPE_CHECKING:
    from .filter_connection import FilterConnection as FilterConnection_f01f0d97
    from .filter_field_value import FilterFieldValue as FilterFieldValue_ef2a0d68
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class TableFilterField3(object):
        """
        Struct Class

        
        **since**
        
            LibreOffice 3.5

        See Also:
            `API TableFilterField3 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1TableFilterField3.html>`_


        Note:
            | At runtime TableFilterField3 will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | TableFilterField3 is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Connection: 'typing.Optional[FilterConnection_f01f0d97]' = None, Field: typing.Optional[int] = None, Operator: typing.Optional[int] = None, Values: 'typing.Optional[typing.List[FilterFieldValue_ef2a0d68]]' = None):
            self._connection = Connection
            self._field = Field
            self._operator = Operator
            self._values = Values

        @property
        def Connection(self) -> 'FilterConnection_f01f0d97':
            """
            specifies how the condition is connected to the previous condition.
            """
            return self._connection
        
        @Connection.setter
        def Connection(self, value: 'FilterConnection_f01f0d97') -> None:
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

        @property
        def Values(self) -> 'typing.List[FilterFieldValue_ef2a0d68]':
            """
            specifies values to match against.
            
            Each filter field may have one or more values.
            """
            return self._values
        
        @Values.setter
        def Values(self, value: 'typing.List[FilterFieldValue_ef2a0d68]') -> None:
            self._values = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global TableFilterField3
        order = ('Connection', 'Field', 'Operator', 'Values')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.sheet.TableFilterField3')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        TableFilterField3 = _struct_init

    _dynamic_struct()

__all__ = ['TableFilterField3']
