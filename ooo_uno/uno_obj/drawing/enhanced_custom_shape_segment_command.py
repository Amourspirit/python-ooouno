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
# Namespace: com.sun.star.drawing
from enum import IntEnum


class EnhancedCustomShapeSegmentCommand(object):
    """
    Const Class


    See Also:
        `API EnhancedCustomShapeSegmentCommand <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeSegmentCommand.html>`_
    """
    UNKNOWN = 0
    MOVETO = 1
    LINETO = 2
    CURVETO = 3
    CLOSESUBPATH = 4
    ENDSUBPATH = 5
    NOFILL = 6
    NOSTROKE = 7
    ANGLEELLIPSETO = 8
    ANGLEELLIPSE = 9
    ARCTO = 10
    ARC = 11
    CLOCKWISEARCTO = 12
    CLOCKWISEARC = 13
    ELLIPTICALQUADRANTX = 14
    ELLIPTICALQUADRANTY = 15
    QUADRATICCURVETO = 16
    ARCANGLETO = 17
    DARKEN = 18
    """
    darken fill color
    """
    DARKENLESS = 19
    """
    darken fill color less
    """
    LIGHTEN = 20
    """
    lighten fill color
    """
    LIGHTENLESS = 21
    """
    lighten fill color less
    """


class EnhancedCustomShapeSegmentCommandEnum(IntEnum):
    """
    Enum of Const Class EnhancedCustomShapeSegmentCommand

    """
    UNKNOWN = EnhancedCustomShapeSegmentCommand.UNKNOWN
    MOVETO = EnhancedCustomShapeSegmentCommand.MOVETO
    LINETO = EnhancedCustomShapeSegmentCommand.LINETO
    CURVETO = EnhancedCustomShapeSegmentCommand.CURVETO
    CLOSESUBPATH = EnhancedCustomShapeSegmentCommand.CLOSESUBPATH
    ENDSUBPATH = EnhancedCustomShapeSegmentCommand.ENDSUBPATH
    NOFILL = EnhancedCustomShapeSegmentCommand.NOFILL
    NOSTROKE = EnhancedCustomShapeSegmentCommand.NOSTROKE
    ANGLEELLIPSETO = EnhancedCustomShapeSegmentCommand.ANGLEELLIPSETO
    ANGLEELLIPSE = EnhancedCustomShapeSegmentCommand.ANGLEELLIPSE
    ARCTO = EnhancedCustomShapeSegmentCommand.ARCTO
    ARC = EnhancedCustomShapeSegmentCommand.ARC
    CLOCKWISEARCTO = EnhancedCustomShapeSegmentCommand.CLOCKWISEARCTO
    CLOCKWISEARC = EnhancedCustomShapeSegmentCommand.CLOCKWISEARC
    ELLIPTICALQUADRANTX = EnhancedCustomShapeSegmentCommand.ELLIPTICALQUADRANTX
    ELLIPTICALQUADRANTY = EnhancedCustomShapeSegmentCommand.ELLIPTICALQUADRANTY
    QUADRATICCURVETO = EnhancedCustomShapeSegmentCommand.QUADRATICCURVETO
    ARCANGLETO = EnhancedCustomShapeSegmentCommand.ARCANGLETO
    DARKEN = EnhancedCustomShapeSegmentCommand.DARKEN
    """
    darken fill color
    """
    DARKENLESS = EnhancedCustomShapeSegmentCommand.DARKENLESS
    """
    darken fill color less
    """
    LIGHTEN = EnhancedCustomShapeSegmentCommand.LIGHTEN
    """
    lighten fill color
    """
    LIGHTENLESS = EnhancedCustomShapeSegmentCommand.LIGHTENLESS
    """
    lighten fill color less
    """

__all__ = ['EnhancedCustomShapeSegmentCommand', 'EnhancedCustomShapeSegmentCommandEnum']
