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


class PathCapType(object):
    """
    Const Class

    These constants determine which shape to use for start or end of a stroked path.
    
    The start and end of stroked paths can have one out of several different shapes (which are, of course, only visible for strokes wider than one device pixel).
    
    **since**
    
        OOo 2.0

    See Also:
        `API PathCapType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1PathCapType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.PathCapType'
    __ooo_type_name__: str = 'const'

    BUTT = 0
    """
    End the path at its start or end point, without any cap.
    """
    ROUND = 1
    """
    Extend the path with a half circle cap, diameter is the line width.
    """
    SQUARE = 2
    """
    Extend the path with a rectangular cap, half the line width long.
    """

__all__ = ['PathCapType']
