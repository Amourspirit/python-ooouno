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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.i18n import Currency as UCurrency
        # Dynamically create uno com.sun.star.i18n.Currency using uno
        global Currency

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.i18n.Currency'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.i18n'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.i18n.Currency'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(ID = UNO_NONE, Symbol = UNO_NONE, BankSymbol = UNO_NONE, Name = UNO_NONE, Default = UNO_NONE, UsedInCompatibleFormatCodes = UNO_NONE, DecimalPlaces = UNO_NONE):
            ns = 'com.sun.star.i18n.Currency'
            if isinstance(ID, UCurrency):
                inst = uno.createUnoStruct(ns, ID)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not ID is UNO_NONE:
                if getattr(struct, 'ID') != ID:
                    setattr(struct, 'ID', ID)
            if not Symbol is UNO_NONE:
                if getattr(struct, 'Symbol') != Symbol:
                    setattr(struct, 'Symbol', Symbol)
            if not BankSymbol is UNO_NONE:
                if getattr(struct, 'BankSymbol') != BankSymbol:
                    setattr(struct, 'BankSymbol', BankSymbol)
            if not Name is UNO_NONE:
                if getattr(struct, 'Name') != Name:
                    setattr(struct, 'Name', Name)
            if not Default is UNO_NONE:
                if getattr(struct, 'Default') != Default:
                    setattr(struct, 'Default', Default)
            if not UsedInCompatibleFormatCodes is UNO_NONE:
                if getattr(struct, 'UsedInCompatibleFormatCodes') != UsedInCompatibleFormatCodes:
                    setattr(struct, 'UsedInCompatibleFormatCodes', UsedInCompatibleFormatCodes)
            if not DecimalPlaces is UNO_NONE:
                if getattr(struct, 'DecimalPlaces') != DecimalPlaces:
                    setattr(struct, 'DecimalPlaces', DecimalPlaces)
            _set_attr(struct)
            _set_fn_attr(struct)
            return struct
        _set_attr(_struct_init)
        Currency = _struct_init

    _dynamic_struct()
else:
    from ...lo.i18n.currency import Currency as Currency

__all__ = ['Currency']

