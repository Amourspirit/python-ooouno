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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.awt import FontDescriptor as UFontDescriptor
        # Dynamically create uno com.sun.star.awt.FontDescriptor using uno
        global FontDescriptor

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.awt.FontDescriptor'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.awt'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.awt.FontDescriptor'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Name = UNO_NONE, Height = UNO_NONE, Width = UNO_NONE, StyleName = UNO_NONE, Family = UNO_NONE, CharSet = UNO_NONE, Pitch = UNO_NONE, CharacterWidth = UNO_NONE, Weight = UNO_NONE, Slant = UNO_NONE, Underline = UNO_NONE, Strikeout = UNO_NONE, Orientation = UNO_NONE, Kerning = UNO_NONE, WordLineMode = UNO_NONE, Type = UNO_NONE):
            ns = 'com.sun.star.awt.FontDescriptor'
            if isinstance(Name, UFontDescriptor):
                inst = uno.createUnoStruct(ns, Name)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Name is UNO_NONE:
                if getattr(struct, 'Name') != Name:
                    setattr(struct, 'Name', Name)
            if not Height is UNO_NONE:
                if getattr(struct, 'Height') != Height:
                    setattr(struct, 'Height', Height)
            if not Width is UNO_NONE:
                if getattr(struct, 'Width') != Width:
                    setattr(struct, 'Width', Width)
            if not StyleName is UNO_NONE:
                if getattr(struct, 'StyleName') != StyleName:
                    setattr(struct, 'StyleName', StyleName)
            if not Family is UNO_NONE:
                if getattr(struct, 'Family') != Family:
                    setattr(struct, 'Family', Family)
            if not CharSet is UNO_NONE:
                if getattr(struct, 'CharSet') != CharSet:
                    setattr(struct, 'CharSet', CharSet)
            if not Pitch is UNO_NONE:
                if getattr(struct, 'Pitch') != Pitch:
                    setattr(struct, 'Pitch', Pitch)
            if not CharacterWidth is UNO_NONE:
                if getattr(struct, 'CharacterWidth') != CharacterWidth:
                    setattr(struct, 'CharacterWidth', CharacterWidth)
            if not Weight is UNO_NONE:
                if getattr(struct, 'Weight') != Weight:
                    setattr(struct, 'Weight', Weight)
            if not Slant is UNO_NONE:
                if getattr(struct, 'Slant') != Slant:
                    setattr(struct, 'Slant', Slant)
            if not Underline is UNO_NONE:
                if getattr(struct, 'Underline') != Underline:
                    setattr(struct, 'Underline', Underline)
            if not Strikeout is UNO_NONE:
                if getattr(struct, 'Strikeout') != Strikeout:
                    setattr(struct, 'Strikeout', Strikeout)
            if not Orientation is UNO_NONE:
                if getattr(struct, 'Orientation') != Orientation:
                    setattr(struct, 'Orientation', Orientation)
            if not Kerning is UNO_NONE:
                if getattr(struct, 'Kerning') != Kerning:
                    setattr(struct, 'Kerning', Kerning)
            if not WordLineMode is UNO_NONE:
                if getattr(struct, 'WordLineMode') != WordLineMode:
                    setattr(struct, 'WordLineMode', WordLineMode)
            if not Type is UNO_NONE:
                if getattr(struct, 'Type') != Type:
                    setattr(struct, 'Type', Type)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        FontDescriptor = _struct_init

    _dynamic_struct()
else:
    from ...lo.awt.font_descriptor import FontDescriptor as FontDescriptor

__all__ = ['FontDescriptor']
