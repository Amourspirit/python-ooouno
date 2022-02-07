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
if typing.TYPE_CHECKING:
    from .enhanced_custom_shape_parameter import EnhancedCustomShapeParameter as EnhancedCustomShapeParameter_d6171317


class EnhancedCustomShapeParameterPair(object):
    """
    Struct Class

    specifies the coordinates used with EnhancedCustomShapes

    See Also:
        `API EnhancedCustomShapeParameterPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeParameterPair.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.EnhancedCustomShapeParameterPair'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.EnhancedCustomShapeParameterPair'
    """Literal Constant ``com.sun.star.drawing.EnhancedCustomShapeParameterPair``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``EnhancedCustomShapeParameterPair`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``EnhancedCustomShapeParameterPair``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            First (EnhancedCustomShapeParameter, optional): First value
            Second (EnhancedCustomShapeParameter, optional): Second value
        """
        self._first = None
        self._second = None

        key_order = ('First', 'Second')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], EnhancedCustomShapeParameterPair):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("EnhancedCustomShapeParameterPair.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def First(self) -> 'EnhancedCustomShapeParameter_d6171317':
        return self._first
    
    @First.setter
    def First(self, value: 'EnhancedCustomShapeParameter_d6171317') -> None:
        self._first = value

    @property
    def Second(self) -> 'EnhancedCustomShapeParameter_d6171317':
        return self._second
    
    @Second.setter
    def Second(self, value: 'EnhancedCustomShapeParameter_d6171317') -> None:
        self._second = value


__all__ = ['EnhancedCustomShapeParameterPair']
