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
# Namespace: com.sun.star.xml.crypto.sax
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.xml.crypto.sax import ElementStackItem as UElementStackItem
        # Dynamically create uno com.sun.star.xml.crypto.sax.ElementStackItem using uno
        global ElementStackItem

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.xml.crypto.sax.ElementStackItem'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.xml.crypto.sax'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.xml.crypto.sax.ElementStackItem'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(isStartElementEvent = UNO_NONE, elementName = UNO_NONE, xAttributes = UNO_NONE):
            ns = 'com.sun.star.xml.crypto.sax.ElementStackItem'
            if isinstance(isStartElementEvent, UElementStackItem):
                inst = uno.createUnoStruct(ns, isStartElementEvent)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not isStartElementEvent is UNO_NONE:
                if getattr(struct, 'isStartElementEvent') != isStartElementEvent:
                    setattr(struct, 'isStartElementEvent', isStartElementEvent)
            if not elementName is UNO_NONE:
                if getattr(struct, 'elementName') != elementName:
                    setattr(struct, 'elementName', elementName)
            if not xAttributes is UNO_NONE:
                if getattr(struct, 'xAttributes') != xAttributes:
                    setattr(struct, 'xAttributes', xAttributes)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        ElementStackItem = _struct_init

    _dynamic_struct()
else:
    from .....lo.xml.crypto.sax.element_stack_item import ElementStackItem as ElementStackItem

__all__ = ['ElementStackItem']
