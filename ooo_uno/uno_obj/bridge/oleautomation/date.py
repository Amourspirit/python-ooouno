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
import os
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class Date(object):
    """
    Struct Class

    is the UNO representation of the Automation type DATE.
    
    A DATE could actually be represented as double in UNO and therefore a typedef from double to a date type would do. But a typedef cannot be expressed in all language bindings. In the case where no typedefs are supported the actual type is used. That is, a typedef'd date type would be represented as double in Java. The information that the double is a date type is lost.
    
    When calling Automation objects from UNO the distinction between double and date type is important. Therefore Date is declared as struct.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Date <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1Date.html>`_


    Note:
        | At runtime Date will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | Date is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Value: typing.Optional[float] = None):
        self._value = Value

    @property
    def Value(self) -> float:
        """
        corresponds to the Automation type DATE.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: float) -> None:
        self._value = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global Date
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Value',)
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.bridge.oleautomation.Date')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        Date = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['Date']
