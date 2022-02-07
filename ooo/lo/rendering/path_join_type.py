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


class PathJoinType(object):
    """
    Const Class

    Determines which shape to use when joining path segments.
    
    The joins between different paths segments can be formed out of several different shapes (which are of course only visible for strokes wider than one device pixel).
    
    **since**
    
        OOo 2.0

    See Also:
        `API PathJoinType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1PathJoinType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.PathJoinType'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    Do not join the path segments at all.
    
    This join type might lead, depending on the angle between the segments, to visible cracks at the meeting points.
    """
    MITER = 1
    """
    Join the path segment by extending the outer border until they intersect.
    """
    ROUND = 2
    """
    Join the path segment with a pie-like patch, such that the outer line of the meeting point is round.
    """
    BEVEL = 3
    """
    Join the path segment by connecting the outer ends of the abutting segments with a straight line.
    """

__all__ = ['PathJoinType']
