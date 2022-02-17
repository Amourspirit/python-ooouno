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
# Namespace: com.sun.star.mozilla
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.mozilla import MenuMultipleChange as UMenuMultipleChange
        # Dynamically create uno com.sun.star.mozilla.MenuMultipleChange using uno
        global MenuMultipleChange

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.mozilla.MenuMultipleChange'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.mozilla'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.mozilla.MenuMultipleChange'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Image = UNO_NONE, ID = UNO_NONE, GroupID = UNO_NONE, PreItemID = UNO_NONE, ItemText = UNO_NONE, IsVisible = UNO_NONE, IsActive = UNO_NONE, IsCheckable = UNO_NONE, IsChecked = UNO_NONE):
            ns = 'com.sun.star.mozilla.MenuMultipleChange'
            if isinstance(Image, UMenuMultipleChange):
                inst = uno.createUnoStruct(ns, Image)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Image is UNO_NONE:
                if getattr(struct, 'Image') != Image:
                    setattr(struct, 'Image', Image)
            if not ID is UNO_NONE:
                if getattr(struct, 'ID') != ID:
                    setattr(struct, 'ID', ID)
            if not GroupID is UNO_NONE:
                if getattr(struct, 'GroupID') != GroupID:
                    setattr(struct, 'GroupID', GroupID)
            if not PreItemID is UNO_NONE:
                if getattr(struct, 'PreItemID') != PreItemID:
                    setattr(struct, 'PreItemID', PreItemID)
            if not ItemText is UNO_NONE:
                if getattr(struct, 'ItemText') != ItemText:
                    setattr(struct, 'ItemText', ItemText)
            if not IsVisible is UNO_NONE:
                if getattr(struct, 'IsVisible') != IsVisible:
                    setattr(struct, 'IsVisible', IsVisible)
            if not IsActive is UNO_NONE:
                if getattr(struct, 'IsActive') != IsActive:
                    setattr(struct, 'IsActive', IsActive)
            if not IsCheckable is UNO_NONE:
                if getattr(struct, 'IsCheckable') != IsCheckable:
                    setattr(struct, 'IsCheckable', IsCheckable)
            if not IsChecked is UNO_NONE:
                if getattr(struct, 'IsChecked') != IsChecked:
                    setattr(struct, 'IsChecked', IsChecked)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        MenuMultipleChange = _struct_init

    _dynamic_struct()
else:
    from ...lo.mozilla.menu_multiple_change import MenuMultipleChange as MenuMultipleChange

__all__ = ['MenuMultipleChange']
