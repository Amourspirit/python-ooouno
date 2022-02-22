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
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    import uno
 
    def _get_class():
        orig_init = None
        def init(self, Spellout = UNO_NONE, **kwargs):
            if getattr(Spellout, "__class__", None) == self.__class__:
                orig_init(self, Spellout)
                return
            else:
                orig_init(self)
            if not Spellout is UNO_NONE:
                if getattr(self, 'Spellout') != Spellout:
                    setattr(self, 'Spellout', Spellout)
            for k, v in kwargs.items():
                if v is UNO_NONE:
                    continue
                else:
                    setattr(self, k, v)

        type_name = 'com.sun.star.i18n.NativeNumberXmlAttributes2'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.i18n'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    NativeNumberXmlAttributes2 = _get_class()


else:
    from ...lo.i18n.native_number_xml_attributes2 import NativeNumberXmlAttributes2 as NativeNumberXmlAttributes2

__all__ = ['NativeNumberXmlAttributes2']

