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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.report
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class GroupKeepTogether(metaclass=UnoConstMeta, type_name="com.sun.star.report.GroupKeepTogether", name_space="com.sun.star.report"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.report.GroupKeepTogether``"""
        pass

    class GroupKeepTogetherEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.report.GroupKeepTogether", name_space="com.sun.star.report"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.report.GroupKeepTogether`` as Enum values"""
        pass

else:
    from ...lo.report.group_keep_together import GroupKeepTogether as GroupKeepTogether

    class GroupKeepTogetherEnum(IntEnum):
        """
        Enum of Const Class GroupKeepTogether

        Specifies if groups in a multi column report where the group has the property XGroup.KeepTogether set to WHOLE_GROUP or WITH_FIRST_DETAIL will keep together by page or column.
        """
        PER_PAGE = GroupKeepTogether.PER_PAGE
        """
        Groups are kept together by page.
        """
        PER_COLUMN = GroupKeepTogether.PER_COLUMN
        """
        Groups are kept together by column.
        """

__all__ = ['GroupKeepTogether', 'GroupKeepTogetherEnum']
