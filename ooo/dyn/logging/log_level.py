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
# Namespace: com.sun.star.logging
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class LogLevel(metaclass=UnoConstMeta, type_name="com.sun.star.logging.LogLevel", name_space="com.sun.star.logging"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.logging.LogLevel``"""
        pass

    class LogLevelEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.logging.LogLevel", name_space="com.sun.star.logging"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.logging.LogLevel`` as Enum values"""
        pass

else:
    from ...lo.logging.log_level import LogLevel as LogLevel

    class LogLevelEnum(IntEnum):
        """
        Enum of Const Class LogLevel

        specifies levels to distinguish between severities of logged events
        
        **since**
        
            OOo 2.3
        """
        OFF = LogLevel.OFF
        """
        specifies that no messages are to be logged at all
        
        This level can be set at an XLogger to completely prevent logging. You will usually not use it with a concrete log event.
        """
        SEVERE = LogLevel.SEVERE
        """
        denotes a serious failure to be logged
        """
        WARNING = LogLevel.WARNING
        """
        denotes a potential problem to be logged
        """
        INFO = LogLevel.INFO
        """
        denotes an informational message to be logged
        """
        CONFIG = LogLevel.CONFIG
        """
        denotes a static configuration message to be logged
        """
        FINE = LogLevel.FINE
        """
        denotes basic tracing information to be logged
        """
        FINER = LogLevel.FINER
        """
        denotes more fine-grained tracing information to be logged
        """
        FINEST = LogLevel.FINEST
        """
        denotes highly detailed tracing information to be logged
        """
        ALL = LogLevel.ALL
        """
        specifies that all messages should be logged
        
        This level can be set at an XLogger to enable logging of absolutely all events. You will usually not use it with a concrete log event.
        """

__all__ = ['LogLevel', 'LogLevelEnum']
