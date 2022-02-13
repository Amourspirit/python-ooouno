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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.frame.status import Verb as UVerb
        # Dynamically create uno com.sun.star.frame.status.Verb using uno
        global Verb

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.frame.status'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.frame.status.Verb'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(VerbId = UNO_NONE, VerbName = UNO_NONE, VerbIsOnMenu = UNO_NONE, VerbIsConst = UNO_NONE):
            ns = 'com.sun.star.frame.status.Verb'
            if isinstance(VerbId, UVerb):
                inst = uno.createUnoStruct(ns, VerbId)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not VerbId is UNO_NONE:
                if getattr(struct, 'VerbId') != VerbId:
                    setattr(struct, 'VerbId', VerbId)
            if not VerbName is UNO_NONE:
                if getattr(struct, 'VerbName') != VerbName:
                    setattr(struct, 'VerbName', VerbName)
            if not VerbIsOnMenu is UNO_NONE:
                if getattr(struct, 'VerbIsOnMenu') != VerbIsOnMenu:
                    setattr(struct, 'VerbIsOnMenu', VerbIsOnMenu)
            if not VerbIsConst is UNO_NONE:
                if getattr(struct, 'VerbIsConst') != VerbIsConst:
                    setattr(struct, 'VerbIsConst', VerbIsConst)
            _set_attr(struct)
            return struct
        Verb = _struct_init

    _dynamic_struct()
else:
    from ....lo.frame.status.verb import Verb as Verb

__all__ = ['Verb']

