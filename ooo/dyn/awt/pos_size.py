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
# Namespace: com.sun.star.awt
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

    class PosSize(metaclass=UnoConstMeta, type_name="com.sun.star.awt.PosSize", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.PosSize``"""
        pass

    class PosSizeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.PosSize", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.PosSize`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.awt import PosSize as PosSize
    else:
        # keep document generators happy
        from ...lo.awt.pos_size import PosSize as PosSize

    class PosSizeEnum(IntEnum):
        """
        Enum of Const Class PosSize

        These constants are used to flag the parameters of a rectangle.
        """
        X = PosSize.X
        """
        flags the x-coordinate.
        """
        Y = PosSize.Y
        """
        flags the y-coordinate.
        """
        WIDTH = PosSize.WIDTH
        """
        flags the width.
        """
        HEIGHT = PosSize.HEIGHT
        """
        flags the height.
        """
        POS = PosSize.POS
        """
        flags the x- and y-coordinate.
        """
        SIZE = PosSize.SIZE
        """
        flags the width and height.
        """
        POSSIZE = PosSize.POSSIZE
        """
        flags the x- and y-coordinate, width and height.
        """

__all__ = ['PosSize', 'PosSizeEnum']
