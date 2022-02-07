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
# Namespace: com.sun.star.lang
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        import uno
        # Dynamically create uno struct using uno
        global Locale

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.lang'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.lang.Locale'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(*args, **kwargs):
            arg_len = len(args)
            if arg_len == 1:
                from com.sun.star.lang import Locale as ULocale
                if isinstance(args[0], ULocale):
                    struct = uno.createUnoStruct(
                        'com.sun.star.lang.Locale', args[0])
                    _set_attr(struct)
                    return struct

            key_order = ('Language', 'Country', 'Variant')
            struct = uno.createUnoStruct('com.sun.star.lang.Locale')
            if arg_len > len(key_order):
                raise ValueError("Locale.__init__() To many parameters")
            for i, arg in enumerate(args):
                setattr(struct, key_order[i], arg)
            for k, v in kwargs.items():
                if k in key_order:
                    setattr(struct, k, v)
            _set_attr(struct)
            return struct
        Locale = _struct_init

    _dynamic_struct()
else:
    from ...lo.lang.locale import Locale as Locale

__all__ = ['Locale']

