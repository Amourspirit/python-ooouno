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
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    import uno
 
    def _get_class():
        orig_init = None
        def init(self, Properties = UNO_NONE, Type = UNO_NONE, Attributes = UNO_NONE):
            if getattr(Properties, "__class__", None) == self.__class__:
                orig_init(self, Properties)
                return
            else:
                orig_init(self)
            if not Properties is UNO_NONE:
                if getattr(self, 'Properties') != Properties:
                    setattr(self, 'Properties', Properties)
            if not Type is UNO_NONE:
                if getattr(self, 'Type') != Type:
                    setattr(self, 'Type', Type)
            if not Attributes is UNO_NONE:
                if getattr(self, 'Attributes') != Attributes:
                    setattr(self, 'Attributes', Attributes)

        type_name = 'com.sun.star.ucb.ContentInfo'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.ucb'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    ContentInfo = _get_class()


else:
    from ...lo.ucb.content_info import ContentInfo as ContentInfo

__all__ = ['ContentInfo']

