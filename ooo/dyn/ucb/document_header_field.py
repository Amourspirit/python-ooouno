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
        from com.sun.star.ucb import DocumentHeaderField as UDocumentHeaderField
        # Dynamically create uno com.sun.star.ucb.DocumentHeaderField using uno
        global DocumentHeaderField

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.ucb'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.ucb.DocumentHeaderField'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Name = UNO_NONE, Value = UNO_NONE):
            ns = 'com.sun.star.ucb.DocumentHeaderField'
            if isinstance(Name, UDocumentHeaderField):
                inst = uno.createUnoStruct(ns, Name)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Name is UNO_NONE:
                if getattr(struct, 'Name') != Name:
                    setattr(struct, 'Name', Name)
            if not Value is UNO_NONE:
                if getattr(struct, 'Value') != Value:
                    setattr(struct, 'Value', Value)
            _set_attr(struct)
            return struct
        DocumentHeaderField = _struct_init

    _dynamic_struct()
else:
    from ...lo.ucb.document_header_field import DocumentHeaderField as DocumentHeaderField

__all__ = ['DocumentHeaderField']

