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


class FontEmphasisMark(object):
    """
    Const Class

    These values are used to specify the kind of emphasis mark.
    
    They may be expanded in future versions.

    See Also:
        `API FontEmphasisMark <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1FontEmphasisMark.html>`_
    """
    NONE = 0
    """
    specifies no emphasis mark.
    """
    DOT = 1
    """
    specifies emphasis mark dot.
    """
    CIRCLE = 2
    """
    specifies emphasis mark circle.
    """
    DISC = 3
    """
    specifies emphasis mark disc.
    """
    ACCENT = 4
    """
    specifies emphasis mark accent.
    """
    ABOVE = 4096
    """
    specifies that the emphasis mark should be positioned above the characters.
    """
    BELOW = 8192
    """
    specifies that the emphasis mark should be positioned below the characters.
    """


class FontEmphasisMarkEnum(IntEnum):
    """
    Enum of Const Class FontEmphasisMark

    These values are used to specify the kind of emphasis mark.
    
    They may be expanded in future versions.
    """
    NONE = FontEmphasisMark.NONE
    """
    specifies no emphasis mark.
    """
    DOT = FontEmphasisMark.DOT
    """
    specifies emphasis mark dot.
    """
    CIRCLE = FontEmphasisMark.CIRCLE
    """
    specifies emphasis mark circle.
    """
    DISC = FontEmphasisMark.DISC
    """
    specifies emphasis mark disc.
    """
    ACCENT = FontEmphasisMark.ACCENT
    """
    specifies emphasis mark accent.
    """
    ABOVE = FontEmphasisMark.ABOVE
    """
    specifies that the emphasis mark should be positioned above the characters.
    """
    BELOW = FontEmphasisMark.BELOW
    """
    specifies that the emphasis mark should be positioned below the characters.
    """

__all__ = ['FontEmphasisMark', 'FontEmphasisMarkEnum']
