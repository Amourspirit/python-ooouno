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
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.2
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class IntegerRectangle2D(object):
        """
        Struct Class

        This structure contains the necessary information for a two-dimensional rectangle.
        
        **since**
        
            OOo 2.0

        See Also:
            `API IntegerRectangle2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1IntegerRectangle2D.html>`_


        Note:
            | At runtime IntegerRectangle2D will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | IntegerRectangle2D is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, X1: typing.Optional[int] = None, X2: typing.Optional[int] = None, Y1: typing.Optional[int] = None, Y2: typing.Optional[int] = None):
            self._x1 = X1
            self._x2 = X2
            self._y1 = Y1
            self._y2 = Y2

        @property
        def X1(self) -> int:
            """
            X coordinate of upper left corner.
            """
            return self._x1
        
        @X1.setter
        def X1(self, value: int) -> None:
            self._x1 = value

        @property
        def X2(self) -> int:
            """
            X coordinate of lower right corner.
            
            Must be greater than X1 for non-empty rectangles.
            """
            return self._x2
        
        @X2.setter
        def X2(self, value: int) -> None:
            self._x2 = value

        @property
        def Y1(self) -> int:
            """
            Y coordinate of upper left corner.
            """
            return self._y1
        
        @Y1.setter
        def Y1(self, value: int) -> None:
            self._y1 = value

        @property
        def Y2(self) -> int:
            """
            Y coordinate of lower right corner.
            
            Must be greater than y1 for non-empty rectangles.
            """
            return self._y2
        
        @Y2.setter
        def Y2(self, value: int) -> None:
            self._y2 = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global IntegerRectangle2D
        order = ('X1', 'X2', 'Y1', 'Y2')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.geometry.IntegerRectangle2D')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        IntegerRectangle2D = _struct_init

    _dynamic_struct()

__all__ = ['IntegerRectangle2D']
