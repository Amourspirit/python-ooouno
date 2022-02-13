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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.ucb import Rule as URule
        # Dynamically create uno com.sun.star.ucb.Rule using uno
        global Rule

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.ucb.Rule'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.ucb'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.ucb.Rule'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Terms = UNO_NONE, Parameter = UNO_NONE, Action = UNO_NONE):
            ns = 'com.sun.star.ucb.Rule'
            if isinstance(Terms, URule):
                inst = uno.createUnoStruct(ns, Terms)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Terms is UNO_NONE:
                if getattr(struct, 'Terms') != Terms:
                    setattr(struct, 'Terms', Terms)
            if not Parameter is UNO_NONE:
                if getattr(struct, 'Parameter') != Parameter:
                    setattr(struct, 'Parameter', Parameter)
            if not Action is UNO_NONE:
                if getattr(struct, 'Action') != Action:
                    setattr(struct, 'Action', Action)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        Rule = _struct_init

    _dynamic_struct()
else:
    from ...lo.ucb.rule import Rule as Rule

__all__ = ['Rule']

