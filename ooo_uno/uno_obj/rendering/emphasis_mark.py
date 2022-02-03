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
# Namespace: com.sun.star.rendering
from enum import IntEnum


class EmphasisMark(object):
    """
    Const Class

    These constants control the automatic rendering of emphasis marks.
    
    These constants control the automatic rendering of emphasis marks for a given font.
    
    **since**
    
        OOo 2.0

    See Also:
        `API EmphasisMark <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1EmphasisMark.html>`_
    """
    NONE = 0
    """
    No automatic emphasis marks.
    """
    DOT_ABOVE = 1
    """
    Automatic emphasis marks as dots above the glyphs.
    """
    DOT_BELOW = 2
    """
    Automatic emphasis marks as dots below the glyphs.
    """
    CIRCLE_ABOVE = 3
    """
    Automatic emphasis marks as circles (unfilled outlines) above the glyphs.
    """
    CIRCLE_BELOW = 4
    """
    Automatic emphasis marks as circles (unfilled outlines) below the glyphs.
    """
    DISC_ABOVE = 5
    """
    Automatic emphasis marks as discs (filled circles) above the glyphs.
    """
    DISC_BELOW = 6
    """
    Automatic emphasis marks as discs (filled circles) below the glyphs.
    """
    ACCENT_ABOVE = 7
    """
    Automatic emphasis marks as accent marks above the glyphs.
    """
    ACCENT_BELOW = 8
    """
    Automatic emphasis marks as accent marks below the glyphs.
    """


class EmphasisMarkEnum(IntEnum):
    """
    Enum of Const Class EmphasisMark

    These constants control the automatic rendering of emphasis marks.
    
    These constants control the automatic rendering of emphasis marks for a given font.
    
    **since**
    
        OOo 2.0
    """
    NONE = EmphasisMark.NONE
    """
    No automatic emphasis marks.
    """
    DOT_ABOVE = EmphasisMark.DOT_ABOVE
    """
    Automatic emphasis marks as dots above the glyphs.
    """
    DOT_BELOW = EmphasisMark.DOT_BELOW
    """
    Automatic emphasis marks as dots below the glyphs.
    """
    CIRCLE_ABOVE = EmphasisMark.CIRCLE_ABOVE
    """
    Automatic emphasis marks as circles (unfilled outlines) above the glyphs.
    """
    CIRCLE_BELOW = EmphasisMark.CIRCLE_BELOW
    """
    Automatic emphasis marks as circles (unfilled outlines) below the glyphs.
    """
    DISC_ABOVE = EmphasisMark.DISC_ABOVE
    """
    Automatic emphasis marks as discs (filled circles) above the glyphs.
    """
    DISC_BELOW = EmphasisMark.DISC_BELOW
    """
    Automatic emphasis marks as discs (filled circles) below the glyphs.
    """
    ACCENT_ABOVE = EmphasisMark.ACCENT_ABOVE
    """
    Automatic emphasis marks as accent marks above the glyphs.
    """
    ACCENT_BELOW = EmphasisMark.ACCENT_BELOW
    """
    Automatic emphasis marks as accent marks below the glyphs.
    """

__all__ = ['EmphasisMark', 'EmphasisMarkEnum']
