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
from ...lo.awt.font_underline import FontUnderline as FontUnderline


class FontUnderlineEnum(IntEnum):
    """
    Enum of Const Class FontUnderline

    These values are used to specify the kind of underlining.
    
    They may be expanded in future versions.
    """
    NONE = FontUnderline.NONE
    """
    specifies no underlining.
    """
    SINGLE = FontUnderline.SINGLE
    """
    specifies underlining with a single line.
    """
    DOUBLE = FontUnderline.DOUBLE
    """
    specifies underlining with a double line.
    """
    DOTTED = FontUnderline.DOTTED
    """
    specifies underlining with a dotted line.
    """
    DONTKNOW = FontUnderline.DONTKNOW
    """
    The kind of underlining is not known.
    """
    DASH = FontUnderline.DASH
    """
    specifies underlining with a dashed line.
    """
    LONGDASH = FontUnderline.LONGDASH
    """
    specifies underlining with long dashes.
    """
    DASHDOT = FontUnderline.DASHDOT
    """
    specifies underlining with a dash and dot sequence.
    """
    DASHDOTDOT = FontUnderline.DASHDOTDOT
    """
    specifies underlining with a dash, dot, dot sequence.
    """
    SMALLWAVE = FontUnderline.SMALLWAVE
    """
    specifies underlining with a small wave.
    """
    WAVE = FontUnderline.WAVE
    """
    specifies underlining with a wave.
    """
    DOUBLEWAVE = FontUnderline.DOUBLEWAVE
    """
    specifies underlining with a double wave.
    """
    BOLD = FontUnderline.BOLD
    """
    specifies underlining with a bold line.
    """
    BOLDDOTTED = FontUnderline.BOLDDOTTED
    """
    specifies underlining with bold dots.
    """
    BOLDDASH = FontUnderline.BOLDDASH
    """
    specifies underlining with bold dashes.
    """
    BOLDLONGDASH = FontUnderline.BOLDLONGDASH
    """
    specifies underlining with long bold dashes.
    """
    BOLDDASHDOT = FontUnderline.BOLDDASHDOT
    """
    specifies underlining with a dash and dot sequence in bold.
    """
    BOLDDASHDOTDOT = FontUnderline.BOLDDASHDOTDOT
    """
    specifies underlining with a dash, dot, dot sequence in bold.
    """
    BOLDWAVE = FontUnderline.BOLDWAVE
    """
    specifies underlining with a bold wave.
    """

__all__ = ['FontUnderline', 'FontUnderlineEnum']
