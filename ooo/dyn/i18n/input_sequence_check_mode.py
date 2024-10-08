# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.i18n
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class InputSequenceCheckMode(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.InputSequenceCheckMode", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.InputSequenceCheckMode``"""
        pass

    class InputSequenceCheckModeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.InputSequenceCheckMode", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.InputSequenceCheckMode`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.i18n import InputSequenceCheckMode as InputSequenceCheckMode
    else:
        # keep document generators happy
        from ...lo.i18n.input_sequence_check_mode import InputSequenceCheckMode as InputSequenceCheckMode

    class InputSequenceCheckModeEnum(IntEnum):
        """
        Enum of Const Class InputSequenceCheckMode

        Input check mode constants to use with XInputSequenceChecker.checkInputSequence()
        
        **since**
        
            OOo 1.1.2
        """
        PASSTHROUGH = InputSequenceCheckMode.PASSTHROUGH
        """
        Pass through mode (no checking)
        """
        BASIC = InputSequenceCheckMode.BASIC
        """
        Basic checking mode.
        """
        STRICT = InputSequenceCheckMode.STRICT
        """
        Strict checking mode.
        """

__all__ = ['InputSequenceCheckMode', 'InputSequenceCheckModeEnum']
