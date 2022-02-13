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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.rendering import FontMetrics as UFontMetrics
        # Dynamically create uno com.sun.star.rendering.FontMetrics using uno
        global FontMetrics

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.rendering'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.rendering.FontMetrics'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Ascent = UNO_NONE, Descent = UNO_NONE, InternalLeading = UNO_NONE, ExternalLeading = UNO_NONE, ReferenceCharSize = UNO_NONE, UnderlineOffset = UNO_NONE, StrikeThroughOffset = UNO_NONE):
            ns = 'com.sun.star.rendering.FontMetrics'
            if isinstance(Ascent, UFontMetrics):
                inst = uno.createUnoStruct(ns, Ascent)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Ascent is UNO_NONE:
                if getattr(struct, 'Ascent') != Ascent:
                    setattr(struct, 'Ascent', Ascent)
            if not Descent is UNO_NONE:
                if getattr(struct, 'Descent') != Descent:
                    setattr(struct, 'Descent', Descent)
            if not InternalLeading is UNO_NONE:
                if getattr(struct, 'InternalLeading') != InternalLeading:
                    setattr(struct, 'InternalLeading', InternalLeading)
            if not ExternalLeading is UNO_NONE:
                if getattr(struct, 'ExternalLeading') != ExternalLeading:
                    setattr(struct, 'ExternalLeading', ExternalLeading)
            if not ReferenceCharSize is UNO_NONE:
                if getattr(struct, 'ReferenceCharSize') != ReferenceCharSize:
                    setattr(struct, 'ReferenceCharSize', ReferenceCharSize)
            if not UnderlineOffset is UNO_NONE:
                if getattr(struct, 'UnderlineOffset') != UnderlineOffset:
                    setattr(struct, 'UnderlineOffset', UnderlineOffset)
            if not StrikeThroughOffset is UNO_NONE:
                if getattr(struct, 'StrikeThroughOffset') != StrikeThroughOffset:
                    setattr(struct, 'StrikeThroughOffset', StrikeThroughOffset)
            _set_attr(struct)
            return struct
        FontMetrics = _struct_init

    _dynamic_struct()
else:
    from ...lo.rendering.font_metrics import FontMetrics as FontMetrics

__all__ = ['FontMetrics']

