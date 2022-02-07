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
# Namespace: com.sun.star.awt
from enum import IntEnum
from ...lo.awt.scroll_bar_orientation import ScrollBarOrientation as ScrollBarOrientation


class ScrollBarOrientationEnum(IntEnum):
    """
    Enum of Const Class ScrollBarOrientation

    These constants are used to specify the orientation of a scroll bar.
    """
    HORIZONTAL = ScrollBarOrientation.HORIZONTAL
    """
    specifies a horizontal scroll bar.
    """
    VERTICAL = ScrollBarOrientation.VERTICAL
    """
    specifies a vertical scroll bar.
    """

__all__ = ['ScrollBarOrientation', 'ScrollBarOrientationEnum']
