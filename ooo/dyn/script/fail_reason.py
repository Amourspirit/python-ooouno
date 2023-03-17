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
# Libre Office Version: 7.4
# Namespace: com.sun.star.script
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FailReason(metaclass=UnoConstMeta, type_name="com.sun.star.script.FailReason", name_space="com.sun.star.script"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.script.FailReason``"""
        pass

    class FailReasonEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.script.FailReason", name_space="com.sun.star.script"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.script.FailReason`` as Enum values"""
        pass

else:
    from ...lo.script.fail_reason import FailReason as FailReason

    class FailReasonEnum(IntEnum):
        """
        Enum of Const Class FailReason

        These values specify the reason why a type conversion failed.
        """
        OUT_OF_RANGE = FailReason.OUT_OF_RANGE
        """
        The given value does not fit in the range of the destination type.
        """
        IS_NOT_NUMBER = FailReason.IS_NOT_NUMBER
        """
        The given value cannot be converted to a number.
        """
        IS_NOT_ENUM = FailReason.IS_NOT_ENUM
        """
        The given value cannot be converted to an enumeration.
        """
        IS_NOT_BOOL = FailReason.IS_NOT_BOOL
        """
        The given value cannot be converted to a boolean.
        """
        NO_SUCH_INTERFACE = FailReason.NO_SUCH_INTERFACE
        """
        The given value is not an interface or cannot queried to the right interface.
        """
        SOURCE_IS_NO_DERIVED_TYPE = FailReason.SOURCE_IS_NO_DERIVED_TYPE
        """
        The given value cannot be converted to right structure or exception type.
        """
        TYPE_NOT_SUPPORTED = FailReason.TYPE_NOT_SUPPORTED
        """
        The type class of the given value is not supported.
        """
        INVALID = FailReason.INVALID
        """
        The given value cannot be converted and none of the other reasons match.
        """
        NO_DEFAULT_AVAILABLE = FailReason.NO_DEFAULT_AVAILABLE
        """
        This value is deprecated.
        
        Do not use.
        """
        UNKNOWN = FailReason.UNKNOWN
        """
        This value is deprecated.
        
        Do not use.
        """

__all__ = ['FailReason', 'FailReasonEnum']
