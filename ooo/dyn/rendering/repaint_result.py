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
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rendering import RepaintResult as RepaintResult
    if hasattr(RepaintResult, '_constants') and isinstance(RepaintResult._constants, dict):
        RepaintResult._constants['__ooo_ns__'] = 'com.sun.star.rendering'
        RepaintResult._constants['__ooo_full_ns__'] = 'com.sun.star.rendering.RepaintResult'
        RepaintResult._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global RepaintResultEnum
        ls = [f for f in dir(RepaintResult) if not callable(getattr(RepaintResult, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(RepaintResult, name)
        RepaintResultEnum = IntEnum('RepaintResultEnum', _dict)
    build_enum()
else:
    from ...lo.rendering.repaint_result import RepaintResult as RepaintResult

    class RepaintResultEnum(IntEnum):
        """
        Enum of Const Class RepaintResult

        These constants specify the result of the XCachedPrimitive render operation.
        
        **since**
        
            OOo 2.0
        """
        REDRAWN = RepaintResult.REDRAWN
        """
        Repaint succeeded, primitive has been exactly reproduced.
        """
        DRAFTED = RepaintResult.DRAFTED
        """
        Repaint succeeded, primitive has been reproduced in preview quality.
        """
        FAILED = RepaintResult.FAILED
        """
        Repaint failed altogether.
        """

__all__ = ['RepaintResult', 'RepaintResultEnum']
