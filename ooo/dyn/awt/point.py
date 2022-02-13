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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.awt import Point as UPoint
        # Dynamically create uno com.sun.star.awt.Point using uno
        global Point

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.awt'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.awt.Point'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(X = UNO_NONE, Y = UNO_NONE):
            ns = 'com.sun.star.awt.Point'
            if isinstance(X, UPoint):
                inst = uno.createUnoStruct(ns, X)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not X is UNO_NONE:
                if getattr(struct, 'X') != X:
                    setattr(struct, 'X', X)
            if not Y is UNO_NONE:
                if getattr(struct, 'Y') != Y:
                    setattr(struct, 'Y', Y)
            _set_attr(struct)
            return struct
        Point = _struct_init

    _dynamic_struct()
else:
    from ...lo.awt.point import Point as Point

__all__ = ['Point']

