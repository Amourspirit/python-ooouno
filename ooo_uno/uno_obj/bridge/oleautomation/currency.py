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
# Namespace: com.sun.star.bridge.oleautomation
# Libre Office Version: 7.2
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class Currency(object):
        """
        Struct Class

        is the UNO representation of the Automation type CY, also know as CURRENCY.
        
        A CY could actually be represented as hyper in UNO and therefore a typedef from hyper to a currency type would do. But a typedef cannot be expressed in all language bindings. In the case where no typedefs are supported the actual type is used. That is, a typedef'd currency type would be represented as long in Java. The information that the long is a currency type is lost.
        
        When calling Automation objects from UNO the distinction between hyper and a currency type is important. Therefore Currency is declared as struct.
        
        **since**
        
            OOo 1.1.2

        See Also:
            `API Currency <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1Currency.html>`_


        Note:
            | At runtime Currency will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | Currency is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Value: typing.Optional[int] = None):
            self._value = Value

        @property
        def Value(self) -> int:
            """
            corresponds to the Automation type CY.
            """
            return self._value
        
        @Value.setter
        def Value(self, value: int) -> None:
            self._value = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global Currency
        order = ('Value',)

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.bridge.oleautomation.Currency')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        Currency = _struct_init

    _dynamic_struct()

__all__ = ['Currency']
