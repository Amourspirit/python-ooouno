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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.sheet import LocalizedName as ULocalizedName
        # Dynamically create uno com.sun.star.sheet.LocalizedName using uno
        global LocalizedName

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.sheet.LocalizedName'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.sheet'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.sheet.LocalizedName'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Locale = UNO_NONE, Name = UNO_NONE):
            ns = 'com.sun.star.sheet.LocalizedName'
            if isinstance(Locale, ULocalizedName):
                inst = uno.createUnoStruct(ns, Locale)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Locale is UNO_NONE:
                if getattr(struct, 'Locale') != Locale:
                    setattr(struct, 'Locale', Locale)
            if not Name is UNO_NONE:
                if getattr(struct, 'Name') != Name:
                    setattr(struct, 'Name', Name)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        LocalizedName = _struct_init

    _dynamic_struct()
else:
    from ...lo.sheet.localized_name import LocalizedName as LocalizedName

__all__ = ['LocalizedName']

