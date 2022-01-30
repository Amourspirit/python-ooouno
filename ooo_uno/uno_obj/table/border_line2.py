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
# Namespace: com.sun.star.table
# Libre Office Version: 7.2
from .border_line import BorderLine as BorderLine_a3f80af6
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class BorderLine2(BorderLine_a3f80af6):
        """
        Struct Class

        A border line, extended with line style.
        
        **since**
        
            LibreOffice 3.4

        See Also:
            `API BorderLine2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1BorderLine2.html>`_


        Note:
            | At runtime BorderLine2 will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | BorderLine2 is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, LineStyle: typing.Optional[int] = None, LineWidth: typing.Optional[int] = None):
            self._line_style = LineStyle
            self._line_width = LineWidth

        @property
        def LineStyle(self) -> int:
            """
            Style of the border.
            """
            return self._line_style
        
        @LineStyle.setter
        def LineStyle(self, value: int) -> None:
            self._line_style = value

        @property
        def LineWidth(self) -> int:
            """
            Width of the border, this is the base to compute all the lines and gaps widths.
            
            These widths computations are based on the LineStyle property
            
            This property is prevailing on the old Out, In and Dist width from BorderLine. If this property is set to 0, then the other widths will be used to guess the border width.
            """
            return self._line_width
        
        @LineWidth.setter
        def LineWidth(self, value: int) -> None:
            self._line_width = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global BorderLine2
        order = ('LineStyle', 'LineWidth')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.table.BorderLine2')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        BorderLine2 = _struct_init

    _dynamic_struct()

__all__ = ['BorderLine2']
