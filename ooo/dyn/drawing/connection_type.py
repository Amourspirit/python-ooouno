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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import uno_enum_class_new
    from com.sun.star.drawing.ConnectionType import (AUTO, BOTTOM, LEFT, RIGHT, SPECIAL, TOP)

    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global ConnectionType
        _dict = {
            "AUTO": AUTO,
            "BOTTOM": BOTTOM,
            "LEFT": LEFT,
            "RIGHT": RIGHT,
            "SPECIAL": SPECIAL,
            "TOP": TOP,
        }

        ConnectionType = type('ConnectionType', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(ConnectionType, k, v)
        setattr(ConnectionType, '__ooo_ns__', 'com.sun.star.drawing')
        setattr(ConnectionType, '__ooo_full_ns__', 'com.sun.star.drawing.ConnectionType')
        setattr(ConnectionType, '__ooo_type_name__', 'enum')
    _dynamic_enum()
else:
    from ...lo.drawing.connection_type import ConnectionType as ConnectionType

__all__ = ['ConnectionType']

