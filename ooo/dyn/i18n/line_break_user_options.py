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
        from com.sun.star.i18n import LineBreakUserOptions as ULineBreakUserOptions
        # Dynamically create uno com.sun.star.i18n.LineBreakUserOptions using uno
        global LineBreakUserOptions

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.i18n.LineBreakUserOptions'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.i18n'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.i18n.LineBreakUserOptions'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(forbiddenBeginCharacters = UNO_NONE, forbiddenEndCharacters = UNO_NONE, applyForbiddenRules = UNO_NONE, allowPunctuationOutsideMargin = UNO_NONE, allowHyphenateEnglish = UNO_NONE):
            ns = 'com.sun.star.i18n.LineBreakUserOptions'
            if isinstance(forbiddenBeginCharacters, ULineBreakUserOptions):
                inst = uno.createUnoStruct(ns, forbiddenBeginCharacters)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not forbiddenBeginCharacters is UNO_NONE:
                if getattr(struct, 'forbiddenBeginCharacters') != forbiddenBeginCharacters:
                    setattr(struct, 'forbiddenBeginCharacters', forbiddenBeginCharacters)
            if not forbiddenEndCharacters is UNO_NONE:
                if getattr(struct, 'forbiddenEndCharacters') != forbiddenEndCharacters:
                    setattr(struct, 'forbiddenEndCharacters', forbiddenEndCharacters)
            if not applyForbiddenRules is UNO_NONE:
                if getattr(struct, 'applyForbiddenRules') != applyForbiddenRules:
                    setattr(struct, 'applyForbiddenRules', applyForbiddenRules)
            if not allowPunctuationOutsideMargin is UNO_NONE:
                if getattr(struct, 'allowPunctuationOutsideMargin') != allowPunctuationOutsideMargin:
                    setattr(struct, 'allowPunctuationOutsideMargin', allowPunctuationOutsideMargin)
            if not allowHyphenateEnglish is UNO_NONE:
                if getattr(struct, 'allowHyphenateEnglish') != allowHyphenateEnglish:
                    setattr(struct, 'allowHyphenateEnglish', allowHyphenateEnglish)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        LineBreakUserOptions = _struct_init

    _dynamic_struct()
else:
    from ...lo.i18n.line_break_user_options import LineBreakUserOptions as LineBreakUserOptions

__all__ = ['LineBreakUserOptions']

