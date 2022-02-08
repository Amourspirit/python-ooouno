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
# Namespace: com.sun.star.frame
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.frame import WindowArrange
else:
    from ...lo.frame.window_arrange import WindowArrange as WindowArrange


class WindowArrangeEnum(IntEnum):
    """
    Enum of Const Class WindowArrange

    these constants are used to specify a style of window arrangement
    """
    TILE = WindowArrange.TILE
    """
    arranges the windows in tiles
    """
    VERTICAL = WindowArrange.VERTICAL
    """
    arranges the windows vertically
    """
    HORIZONTAL = WindowArrange.HORIZONTAL
    """
    arranges the windows horizontally
    """
    CASCADE = WindowArrange.CASCADE
    """
    cascades the windows
    """
    MAXIMIZE = WindowArrange.MAXIMIZE
    """
    maximizes all windows
    """
    MINIMIZE = WindowArrange.MINIMIZE
    """
    minimizes all windows
    """

__all__ = ['WindowArrange', 'WindowArrangeEnum']
