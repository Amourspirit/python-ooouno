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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.2
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.chart2.CurveStyle import (B_SPLINES, CUBIC_SPLINES, LINES, NURBS, STEP_CENTER_X, STEP_CENTER_Y, STEP_END, STEP_START)


class CurveStyle(Enum):
    """
    

    See Also:
        `API CurveStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#a6eee32347565343ce84b84adb82da419>`_
    """
    B_SPLINES = 'B_SPLINES'
    """
    Data points are connected via a parametric, interpolating B-spline curve.
    """
    CUBIC_SPLINES = 'CUBIC_SPLINES'
    """
    Data points are connected via a smoothed cubic spline curve.
    
    The data points themselves are part of to the curve.
    """
    LINES = 'LINES'
    """
    Lines between data points are not smoothed.
    """
    NURBS = 'NURBS'
    """
    Non-uniform rational b-splines.
    """
    STEP_CENTER_X = 'STEP_CENTER_X'
    """
    Data points are connected via a 3-segmented stepped line.
    
    The lines is horizontal till the center of the X values.
    """
    STEP_CENTER_Y = 'STEP_CENTER_Y'
    """
    Data points are connected via a 3-segmented stepped line.
    
    The lines is horizontal at the center of the Y values.
    """
    STEP_END = 'STEP_END'
    """
    Data points are connected via a 2-segmented stepped line.
    
    The line ends horizontally.
    """
    STEP_START = 'STEP_START'
    """
    Data points are connected via a 2-segmented stepped line.
    
    The line starts horizontally.
    """

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global CurveStyle
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "B_SPLINES": B_SPLINES,
            "CUBIC_SPLINES": CUBIC_SPLINES,
            "LINES": LINES,
            "NURBS": NURBS,
            "STEP_CENTER_X": STEP_CENTER_X,
            "STEP_CENTER_Y": STEP_CENTER_Y,
            "STEP_END": STEP_END,
            "STEP_START": STEP_START,
        }
        CurveStyle = type('CurveStyle', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(CurveStyle, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['CurveStyle']

