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
# Libre Office Version: 7.3
# Namespace: com.sun.star.rendering
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rendering import PanoseSerifStyle as PanoseSerifStyle
    if hasattr(PanoseSerifStyle, '_constants') and isinstance(PanoseSerifStyle._constants, dict):
        PanoseSerifStyle._constants['__ooo_ns__'] = 'com.sun.star.rendering'
        PanoseSerifStyle._constants['__ooo_full_ns__'] = 'com.sun.star.rendering.PanoseSerifStyle'
        PanoseSerifStyle._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global PanoseSerifStyleEnum
        ls = [f for f in dir(PanoseSerifStyle) if not callable(getattr(PanoseSerifStyle, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(PanoseSerifStyle, name)
        PanoseSerifStyleEnum = IntEnum('PanoseSerifStyleEnum', _dict)
    build_enum()
else:
    from ...lo.rendering.panose_serif_style import PanoseSerifStyle as PanoseSerifStyle

    class PanoseSerifStyleEnum(IntEnum):
        """
        Enum of Const Class PanoseSerifStyle

        """
        ANYTHING = PanoseSerifStyle.ANYTHING
        NO_FIT = PanoseSerifStyle.NO_FIT
        COVE = PanoseSerifStyle.COVE
        OBTUSE_COVE = PanoseSerifStyle.OBTUSE_COVE
        SQUARE_COVE = PanoseSerifStyle.SQUARE_COVE
        OBTUSE_SQUARE_COVE = PanoseSerifStyle.OBTUSE_SQUARE_COVE
        SQUARE = PanoseSerifStyle.SQUARE
        THIN = PanoseSerifStyle.THIN
        BONE = PanoseSerifStyle.BONE
        EXAGGERATED = PanoseSerifStyle.EXAGGERATED
        TRIANGLE = PanoseSerifStyle.TRIANGLE
        NORMAL_SANS = PanoseSerifStyle.NORMAL_SANS
        OBTUSE_SANS = PanoseSerifStyle.OBTUSE_SANS
        PERP_SANS = PanoseSerifStyle.PERP_SANS
        FLARED = PanoseSerifStyle.FLARED
        ROUNDED = PanoseSerifStyle.ROUNDED

__all__ = ['PanoseSerifStyle', 'PanoseSerifStyleEnum']
