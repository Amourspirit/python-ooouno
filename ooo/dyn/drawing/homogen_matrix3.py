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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.drawing import HomogenMatrix3 as UHomogenMatrix3
        # Dynamically create uno com.sun.star.drawing.HomogenMatrix3 using uno
        global HomogenMatrix3

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.drawing'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.drawing.HomogenMatrix3'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Line1 = UNO_NONE, Line2 = UNO_NONE, Line3 = UNO_NONE):
            ns = 'com.sun.star.drawing.HomogenMatrix3'
            if isinstance(Line1, UHomogenMatrix3):
                inst = uno.createUnoStruct(ns, Line1)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Line1 is UNO_NONE:
                if getattr(struct, 'Line1') != Line1:
                    setattr(struct, 'Line1', Line1)
            if not Line2 is UNO_NONE:
                if getattr(struct, 'Line2') != Line2:
                    setattr(struct, 'Line2', Line2)
            if not Line3 is UNO_NONE:
                if getattr(struct, 'Line3') != Line3:
                    setattr(struct, 'Line3', Line3)
            _set_attr(struct)
            return struct
        HomogenMatrix3 = _struct_init

    _dynamic_struct()
else:
    from ...lo.drawing.homogen_matrix3 import HomogenMatrix3 as HomogenMatrix3

__all__ = ['HomogenMatrix3']

