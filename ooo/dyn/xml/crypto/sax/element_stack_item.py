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
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    import uno
 
    def _get_class():
        orig_init = None
        def init(self, isStartElementEvent = UNO_NONE, elementName = UNO_NONE, xAttributes = UNO_NONE):
            if getattr(isStartElementEvent, "__class__", None) == self.__class__:
                orig_init(self, isStartElementEvent)
                return
            else:
                orig_init(self)
            if not isStartElementEvent is UNO_NONE:
                if getattr(self, 'isStartElementEvent') != isStartElementEvent:
                    setattr(self, 'isStartElementEvent', isStartElementEvent)
            if not elementName is UNO_NONE:
                if getattr(self, 'elementName') != elementName:
                    setattr(self, 'elementName', elementName)
            if not xAttributes is UNO_NONE:
                if getattr(self, 'xAttributes') != xAttributes:
                    setattr(self, 'xAttributes', xAttributes)

        type_name = 'com.sun.star.xml.crypto.sax.ElementStackItem'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.xml.crypto.sax'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    ElementStackItem = _get_class()


else:
    from .....lo.xml.crypto.sax.element_stack_item import ElementStackItem as ElementStackItem

__all__ = ['ElementStackItem']

