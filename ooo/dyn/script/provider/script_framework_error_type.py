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
# Libre Office Version: 7.2
# Namespace: com.sun.star.script.provider
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.script.provider import ScriptFrameworkErrorType
else:
    from ....lo.script.provider.script_framework_error_type import ScriptFrameworkErrorType as ScriptFrameworkErrorType


class ScriptFrameworkErrorTypeEnum(IntEnum):
    """
    Enum of Const Class ScriptFrameworkErrorType

    is a checked exception that represents an error encountered by the Scripting Framework whilst executing a script
    """
    UNKNOWN = ScriptFrameworkErrorType.UNKNOWN
    """
    Unknown.
    """
    NOTSUPPORTED = ScriptFrameworkErrorType.NOTSUPPORTED
    """
    ProviderNotSupported.
    """
    NO_SUCH_SCRIPT = ScriptFrameworkErrorType.NO_SUCH_SCRIPT
    """
    the requested method, and/or with the requested signature, does not exist
    """
    MALFORMED_URL = ScriptFrameworkErrorType.MALFORMED_URL
    """
    the requested method, with the requested signature, does not exist
    """

__all__ = ['ScriptFrameworkErrorType', 'ScriptFrameworkErrorTypeEnum']
