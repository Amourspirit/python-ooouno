# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CaptionType(metaclass=UnoConstMeta, type_name="com.sun.star.drawing.CaptionType", name_space="com.sun.star.drawing"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.drawing.CaptionType``"""
        pass

    class CaptionTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.drawing.CaptionType", name_space="com.sun.star.drawing"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.drawing.CaptionType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.drawing import CaptionType as CaptionType
    else:
        # keep document generators happy
        from ...lo.drawing.caption_type import CaptionType as CaptionType

    class CaptionTypeEnum(IntEnum):
        """
        Enum of Const Class CaptionType

        This constants specifies the geometry of the line of a CaptionShape.
        """
        straight = CaptionType.straight
        """
        the caption line is a straight line from a caption area edge to the caption point.
        """
        angled = CaptionType.angled
        """
        the caption line is the shortest line from the caption area edge to the caption point.
        """
        connector = CaptionType.connector
        """
        the caption line is build up with a straight line from the caption area edge, followed by the shortest line to the caption area point.
        """

__all__ = ['CaptionType', 'CaptionTypeEnum']
