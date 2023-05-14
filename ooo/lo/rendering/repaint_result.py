# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering


class RepaintResult(object):
    """
    Const Class

    These constants specify the result of the XCachedPrimitive render operation.
    
    **since**
    
        OOo 2.0

    See Also:
        `API RepaintResult <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1RepaintResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.RepaintResult'
    __ooo_type_name__: str = 'const'

    REDRAWN = 1
    """
    Repaint succeeded, primitive has been exactly reproduced.
    """
    DRAFTED = 2
    """
    Repaint succeeded, primitive has been reproduced in preview quality.
    """
    FAILED = 3
    """
    Repaint failed altogether.
    """

__all__ = ['RepaintResult']
