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
        def init(self, Criteria = UNO_NONE, Recursion = UNO_NONE, IncludeBase = UNO_NONE, RespectFolderViewRestrictions = UNO_NONE, RespectDocViewRestrictions = UNO_NONE, FollowIndirections = UNO_NONE):
            if getattr(Criteria, "__class__", None) == self.__class__:
                orig_init(self, Criteria)
                return
            else:
                orig_init(self)
            if not Criteria is UNO_NONE:
                if getattr(self, 'Criteria') != Criteria:
                    setattr(self, 'Criteria', Criteria)
            if not Recursion is UNO_NONE:
                if getattr(self, 'Recursion') != Recursion:
                    setattr(self, 'Recursion', Recursion)
            if not IncludeBase is UNO_NONE:
                if getattr(self, 'IncludeBase') != IncludeBase:
                    setattr(self, 'IncludeBase', IncludeBase)
            if not RespectFolderViewRestrictions is UNO_NONE:
                if getattr(self, 'RespectFolderViewRestrictions') != RespectFolderViewRestrictions:
                    setattr(self, 'RespectFolderViewRestrictions', RespectFolderViewRestrictions)
            if not RespectDocViewRestrictions is UNO_NONE:
                if getattr(self, 'RespectDocViewRestrictions') != RespectDocViewRestrictions:
                    setattr(self, 'RespectDocViewRestrictions', RespectDocViewRestrictions)
            if not FollowIndirections is UNO_NONE:
                if getattr(self, 'FollowIndirections') != FollowIndirections:
                    setattr(self, 'FollowIndirections', FollowIndirections)

        type_name = 'com.sun.star.ucb.SearchInfo'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.ucb'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    SearchInfo = _get_class()


else:
    from ...lo.ucb.search_info import SearchInfo as SearchInfo

__all__ = ['SearchInfo']

