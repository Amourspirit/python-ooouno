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
# Namespace: com.sun.star.accessibility
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.accessibility import TextSegment as UTextSegment
        # Dynamically create uno com.sun.star.accessibility.TextSegment using uno
        global TextSegment

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.accessibility.TextSegment'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.accessibility'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.accessibility.TextSegment'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(SegmentText = UNO_NONE, SegmentStart = UNO_NONE, SegmentEnd = UNO_NONE):
            ns = 'com.sun.star.accessibility.TextSegment'
            if isinstance(SegmentText, UTextSegment):
                inst = uno.createUnoStruct(ns, SegmentText)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not SegmentText is UNO_NONE:
                if getattr(struct, 'SegmentText') != SegmentText:
                    setattr(struct, 'SegmentText', SegmentText)
            if not SegmentStart is UNO_NONE:
                if getattr(struct, 'SegmentStart') != SegmentStart:
                    setattr(struct, 'SegmentStart', SegmentStart)
            if not SegmentEnd is UNO_NONE:
                if getattr(struct, 'SegmentEnd') != SegmentEnd:
                    setattr(struct, 'SegmentEnd', SegmentEnd)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        TextSegment = _struct_init

    _dynamic_struct()
else:
    from ...lo.accessibility.text_segment import TextSegment as TextSegment

__all__ = ['TextSegment']

