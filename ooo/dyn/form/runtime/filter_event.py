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
# Namespace: com.sun.star.form.runtime
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.form.runtime import FilterEvent as UFilterEvent
        # Dynamically create uno com.sun.star.form.runtime.FilterEvent using uno
        global FilterEvent

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.form.runtime.FilterEvent'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.form.runtime'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.form.runtime.FilterEvent'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(DisjunctiveTerm = UNO_NONE, FilterComponent = UNO_NONE, PredicateExpression = UNO_NONE, **kwargs):
            ns = 'com.sun.star.form.runtime.FilterEvent'
            if isinstance(DisjunctiveTerm, UFilterEvent):
                inst = uno.createUnoStruct(ns, DisjunctiveTerm)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not DisjunctiveTerm is UNO_NONE:
                if getattr(struct, 'DisjunctiveTerm') != DisjunctiveTerm:
                    setattr(struct, 'DisjunctiveTerm', DisjunctiveTerm)
            if not FilterComponent is UNO_NONE:
                if getattr(struct, 'FilterComponent') != FilterComponent:
                    setattr(struct, 'FilterComponent', FilterComponent)
            if not PredicateExpression is UNO_NONE:
                if getattr(struct, 'PredicateExpression') != PredicateExpression:
                    setattr(struct, 'PredicateExpression', PredicateExpression)
            for k, v in kwargs.items():
                if v is UNO_NONE:
                    continue
                else:
                    setattr(ex, k, v)
            _set_attr(struct)
            _set_fn_attr(struct)
            return struct
        _set_attr(_struct_init)
        FilterEvent = _struct_init

    _dynamic_struct()
else:
    from ....lo.form.runtime.filter_event import FilterEvent as FilterEvent

__all__ = ['FilterEvent']

