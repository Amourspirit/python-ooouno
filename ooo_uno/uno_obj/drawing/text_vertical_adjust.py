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
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.drawing.TextVerticalAdjust import (BLOCK, BOTTOM, CENTER, TOP)


class TextVerticalAdjust(Enum):
    """
    

    See Also:
        `API TextVerticalAdjust <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a4c2c10f0a1a5fa20d9f200d0fb5707ad>`_
    """
    BLOCK = 'BLOCK'
    """
    The text extends from the left to the right edge of the shape.
    
    The text extends from the top to the bottom edge of the shape.
    """
    BOTTOM = 'BOTTOM'
    """
    the connection line leaves the connected object from the bottom,
    
    The text is positioned below the main line.
    
    The bottom edge of the text is adjusted to the bottom edge of the shape.
    """
    CENTER = 'CENTER'
    """
    The text is centered inside the shape.
    """
    TOP = 'TOP'
    """
    the connection line leaves the connected object from the top,
    
    The text is positioned above the main line.
    
    The top edge of the text is adjusted to the top edge of the shape.
    """

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global TextVerticalAdjust
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "BLOCK": BLOCK,
            "BOTTOM": BOTTOM,
            "CENTER": CENTER,
            "TOP": TOP,
        }
        TextVerticalAdjust = type('TextVerticalAdjust', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(TextVerticalAdjust, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['TextVerticalAdjust']

