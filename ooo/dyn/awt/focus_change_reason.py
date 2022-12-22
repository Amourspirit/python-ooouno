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
# Namespace: com.sun.star.awt
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FocusChangeReason(metaclass=UnoConstMeta, type_name="com.sun.star.awt.FocusChangeReason", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.FocusChangeReason``"""
        pass

    class FocusChangeReasonEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.FocusChangeReason", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.FocusChangeReason`` as Enum values"""
        pass

else:
    from ...lo.awt.focus_change_reason import FocusChangeReason as FocusChangeReason

    class FocusChangeReasonEnum(IntFlag):
        """
        Enum of Const Class FocusChangeReason

        A combination of these values can be used to specify the reason for a focus change.
        """
        TAB = FocusChangeReason.TAB
        """
        Focus changed because TAB was pressed.
        """
        CURSOR = FocusChangeReason.CURSOR
        """
        Focus changed because Key Left/Right/Up/Down was pressed.
        """
        MNEMONIC = FocusChangeReason.MNEMONIC
        """
        Focus changed because mnemonic key was pressed.
        """
        FORWARD = FocusChangeReason.FORWARD
        """
        Changed Focus to the next control.
        """
        BACKWARD = FocusChangeReason.BACKWARD
        """
        Changed Focus to the previous control.
        """
        AROUND = FocusChangeReason.AROUND
        """
        Changed Focus forward from last to first or backward from first to last.
        """
        UNIQUEMNEMONIC = FocusChangeReason.UNIQUEMNEMONIC
        """
        Focus changed because mnemonic key was pressed and this mnemonic is unique.
        """

__all__ = ['FocusChangeReason', 'FocusChangeReasonEnum']
