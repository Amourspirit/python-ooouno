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
# Namespace: com.sun.star.ucb
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.ucb import ContentResultSetCapability as ContentResultSetCapability
    if hasattr(ContentResultSetCapability, '_constants') and isinstance(ContentResultSetCapability._constants, dict):
        ContentResultSetCapability._constants['__ooo_ns__'] = 'com.sun.star.ucb'
        ContentResultSetCapability._constants['__ooo_full_ns__'] = 'com.sun.star.ucb.ContentResultSetCapability'
        ContentResultSetCapability._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ContentResultSetCapabilityEnum
        ls = [f for f in dir(ContentResultSetCapability) if not callable(getattr(ContentResultSetCapability, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ContentResultSetCapability, name)
        ContentResultSetCapabilityEnum = IntEnum('ContentResultSetCapabilityEnum', _dict)
    build_enum()
else:
    from ...lo.ucb.content_result_set_capability import ContentResultSetCapability as ContentResultSetCapability

    class ContentResultSetCapabilityEnum(IntEnum):
        """
        Enum of Const Class ContentResultSetCapability

        These values are used to specify the capabilities of an XDynamicResultSet.
        """
        SORTED = ContentResultSetCapability.SORTED
        """
        indicates that a ContentResultSet is properly sorted, exactly following the rules given during the ContentResultSet was created.
        """

__all__ = ['ContentResultSetCapability', 'ContentResultSetCapabilityEnum']
