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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.text import RelOrientation as RelOrientation
    if hasattr(RelOrientation, '_constants') and isinstance(RelOrientation._constants, dict):
        RelOrientation._constants['__ooo_ns__'] = 'com.sun.star.text'
        RelOrientation._constants['__ooo_full_ns__'] = 'com.sun.star.text.RelOrientation'
        RelOrientation._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global RelOrientationEnum
        ls = [f for f in dir(RelOrientation) if not callable(getattr(RelOrientation, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(RelOrientation, name)
        RelOrientationEnum = IntEnum('RelOrientationEnum', _dict)
    build_enum()
else:
    from ...lo.text.rel_orientation import RelOrientation as RelOrientation

    class RelOrientationEnum(IntEnum):
        """
        Enum of Const Class RelOrientation

        These values define the reference position of relative orientations.
        
        **since**
        
            LibreOffice 7.0
        """
        FRAME = RelOrientation.FRAME
        """
        paragraph, including margins
        """
        PRINT_AREA = RelOrientation.PRINT_AREA
        """
        paragraph, without margins
        """
        CHAR = RelOrientation.CHAR
        """
        at a character
        """
        PAGE_LEFT = RelOrientation.PAGE_LEFT
        """
        inside the left page margin
        """
        PAGE_RIGHT = RelOrientation.PAGE_RIGHT
        """
        inside the right page margin
        """
        FRAME_LEFT = RelOrientation.FRAME_LEFT
        """
        inside the left paragraph margin
        """
        FRAME_RIGHT = RelOrientation.FRAME_RIGHT
        """
        inside the right paragraph margin
        """
        PAGE_FRAME = RelOrientation.PAGE_FRAME
        """
        page includes margins for page-anchored frames identical with RelOrientation.FRAME
        """
        PAGE_PRINT_AREA = RelOrientation.PAGE_PRINT_AREA
        """
        page without borders (for page anchored frames identical with RelOrientation.PRINT_AREA).
        """
        TEXT_LINE = RelOrientation.TEXT_LINE
        """
        at the top of the text line, only sensible for vertical orientation.
        
        **since**
        
            OOo 2.0
        """
        PAGE_PRINT_AREA_BOTTOM = RelOrientation.PAGE_PRINT_AREA_BOTTOM
        """
        Bottom page border (page area below PAGE_PRINT_AREA).
        
        **since**
        
            LibreOffice 7.0
        """
        PAGE_PRINT_AREA_TOP = RelOrientation.PAGE_PRINT_AREA_TOP
        """
        Top page border (page area above PAGE_PRINT_AREA).
        
        **since**
        
            LibreOffice 7.1
        """

__all__ = ['RelOrientation', 'RelOrientationEnum']
