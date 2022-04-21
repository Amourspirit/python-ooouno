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
# Namespace: com.sun.star.text
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.text import WrapInfluenceOnPosition as WrapInfluenceOnPosition
    if hasattr(WrapInfluenceOnPosition, '_constants') and isinstance(WrapInfluenceOnPosition._constants, dict):
        WrapInfluenceOnPosition._constants['__ooo_ns__'] = 'com.sun.star.text'
        WrapInfluenceOnPosition._constants['__ooo_full_ns__'] = 'com.sun.star.text.WrapInfluenceOnPosition'
        WrapInfluenceOnPosition._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global WrapInfluenceOnPositionEnum
        ls = [f for f in dir(WrapInfluenceOnPosition) if not callable(getattr(WrapInfluenceOnPosition, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(WrapInfluenceOnPosition, name)
        WrapInfluenceOnPositionEnum = IntEnum('WrapInfluenceOnPositionEnum', _dict)
    build_enum()
else:
    from ...lo.text.wrap_influence_on_position import WrapInfluenceOnPosition as WrapInfluenceOnPosition

    class WrapInfluenceOnPositionEnum(IntEnum):
        """
        Enum of Const Class WrapInfluenceOnPosition

        These values specify the influence of the wrapping style of a floating screen object when it's positioned.
        """
        ONCE_SUCCESSIVE = WrapInfluenceOnPosition.ONCE_SUCCESSIVE
        """
        wrapping style has no influence on the position and the floating screen object is successive positioned.
        """
        ONCE_CONCURRENT = WrapInfluenceOnPosition.ONCE_CONCURRENT
        """
        wrapping style has no influence on the position and the floating screen object is concurrent positioned.
        """
        ITERATIVE = WrapInfluenceOnPosition.ITERATIVE
        """
        wrapping style has influence on the position and the floating screen object is iterative positioned.
        """

__all__ = ['WrapInfluenceOnPosition', 'WrapInfluenceOnPositionEnum']
