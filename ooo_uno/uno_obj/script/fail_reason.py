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
# Namespace: com.sun.star.script
from ooo_uno.base.const import ConstIntBase


class FailReason(ConstIntBase):
    """
    These values specify the reason why a type conversion failed.

    See Also:
        `API FailReason <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1script_1_1FailReason.html>`_
    """
    OUT_OF_RANGE = 1
    """
    The given value does not fit in the range of the destination type.
    """
    IS_NOT_NUMBER = 2
    """
    The given value cannot be converted to a number.
    """
    IS_NOT_ENUM = 3
    """
    The given value cannot be converted to an enumeration.
    """
    IS_NOT_BOOL = 4
    """
    The given value cannot be converted to a boolean.
    """
    NO_SUCH_INTERFACE = 5
    """
    The given value is not an interface or cannot queried to the right interface.
    """
    SOURCE_IS_NO_DERIVED_TYPE = 6
    """
    The given value cannot be converted to right structure or exception type.
    """
    TYPE_NOT_SUPPORTED = 7
    """
    The type class of the given value is not supported.
    """
    INVALID = 8
    """
    The given value cannot be converted and none of the other reasons match.
    """
    NO_DEFAULT_AVAILABLE = 9
    """
    This value is deprecated.
    
    Do not use.
    """
    UNKNOWN = 10
    """
    This value is deprecated.
    
    Do not use.
    """

