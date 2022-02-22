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
# Namespace: com.sun.star.accessibility
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    import uno
 
    def _get_class():
        orig_init = None
        def init(self, TargetSet = UNO_NONE, RelationType = UNO_NONE):
            if getattr(TargetSet, "__class__", None) == self.__class__:
                orig_init(self, TargetSet)
                return
            else:
                orig_init(self)
            if not TargetSet is UNO_NONE:
                if getattr(self, 'TargetSet') != TargetSet:
                    setattr(self, 'TargetSet', TargetSet)
            if not RelationType is UNO_NONE:
                if getattr(self, 'RelationType') != RelationType:
                    setattr(self, 'RelationType', RelationType)

        type_name = 'com.sun.star.accessibility.AccessibleRelation'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.accessibility'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    AccessibleRelation = _get_class()


else:
    from ...lo.accessibility.accessible_relation import AccessibleRelation as AccessibleRelation

__all__ = ['AccessibleRelation']

