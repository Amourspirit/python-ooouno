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
        from com.sun.star.ucb import FolderListEntry as UFolderListEntry
        # Dynamically create uno com.sun.star.ucb.FolderListEntry using uno
        global FolderListEntry

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.ucb.FolderListEntry'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.ucb'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.ucb.FolderListEntry'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Title = UNO_NONE, ID = UNO_NONE, Subscribed = UNO_NONE, New = UNO_NONE, Removed = UNO_NONE, Purge = UNO_NONE):
            ns = 'com.sun.star.ucb.FolderListEntry'
            if isinstance(Title, UFolderListEntry):
                inst = uno.createUnoStruct(ns, Title)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Title is UNO_NONE:
                if getattr(struct, 'Title') != Title:
                    setattr(struct, 'Title', Title)
            if not ID is UNO_NONE:
                if getattr(struct, 'ID') != ID:
                    setattr(struct, 'ID', ID)
            if not Subscribed is UNO_NONE:
                if getattr(struct, 'Subscribed') != Subscribed:
                    setattr(struct, 'Subscribed', Subscribed)
            if not New is UNO_NONE:
                if getattr(struct, 'New') != New:
                    setattr(struct, 'New', New)
            if not Removed is UNO_NONE:
                if getattr(struct, 'Removed') != Removed:
                    setattr(struct, 'Removed', Removed)
            if not Purge is UNO_NONE:
                if getattr(struct, 'Purge') != Purge:
                    setattr(struct, 'Purge', Purge)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        FolderListEntry = _struct_init

    _dynamic_struct()
else:
    from ...lo.ucb.folder_list_entry import FolderListEntry as FolderListEntry

__all__ = ['FolderListEntry']
