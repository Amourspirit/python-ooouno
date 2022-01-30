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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class EnhancedCustomShapeParameter(object):
        """
        Struct Class

        specifies a single value which is used with EnhancedCustomShapes

        See Also:
            `API EnhancedCustomShapeParameter <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeParameter.html>`_


        Note:
            | At runtime EnhancedCustomShapeParameter will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | EnhancedCustomShapeParameter is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Type: typing.Optional[int] = None, Value: typing.Optional[object] = None):
            self._type = Type
            self._value = Value

        @property
        def Type(self) -> int:
            return self._type
        
        @Type.setter
        def Type(self, value: int) -> None:
            self._type = value

        @property
        def Value(self) -> object:
            """
            the any can be of type long or double
            """
            return self._value
        
        @Value.setter
        def Value(self, value: object) -> None:
            self._value = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global EnhancedCustomShapeParameter
        order = ('Type', 'Value')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.drawing.EnhancedCustomShapeParameter')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        EnhancedCustomShapeParameter = _struct_init

    _dynamic_struct()

__all__ = ['EnhancedCustomShapeParameter']
