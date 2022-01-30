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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.drawing.DashStyle import (RECT, RECTRELATIVE, ROUND, ROUNDRELATIVE)

if TYPE_CHECKING or _DYNAMIC is False:


    class DashStyle(Enum):
        """
        Enum Class

        

        See Also:
            `API DashStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a89f0dc2e221d6f608088093da27764d1>`_
        """
        RECT = 'RECT'
        """
        the dash is a rectangle
        """
        RECTRELATIVE = 'RECTRELATIVE'
        """
        the dash is a rectangle, with the size of the dash given in relation to the length of the line
        """
        ROUND = 'ROUND'
        """
        the dash is a point
        
        the lines join with an arc
        
        the line will get a half circle as additional cap
        """
        ROUNDRELATIVE = 'ROUNDRELATIVE'
        """
        the dash is a point, with the size of the dash given in relation to the length of the line
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global DashStyle
        _dict = {
            "RECT": RECT,
            "RECTRELATIVE": RECTRELATIVE,
            "ROUND": ROUND,
            "ROUNDRELATIVE": ROUNDRELATIVE,
        }

        DashStyle = type('DashStyle', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(DashStyle, k, v)

    _dynamic_enum()

__all__ = ['DashStyle']

