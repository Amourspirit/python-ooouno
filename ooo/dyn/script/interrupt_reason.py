# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.script.InterruptReason import BreakPoint as INTERRUPT_REASON_BreakPoint
    from com.sun.star.script.InterruptReason import Cancel as INTERRUPT_REASON_Cancel
    from com.sun.star.script.InterruptReason import CompileError as INTERRUPT_REASON_CompileError
    from com.sun.star.script.InterruptReason import RuntimeError as INTERRUPT_REASON_RuntimeError
    from com.sun.star.script.InterruptReason import Step as INTERRUPT_REASON_Step
    from com.sun.star.script.InterruptReason import StepOut as INTERRUPT_REASON_StepOut
    from com.sun.star.script.InterruptReason import StepOver as INTERRUPT_REASON_StepOver
    from com.sun.star.script.InterruptReason import StepStatement as INTERRUPT_REASON_StepStatement

    class InterruptReason(uno.Enum):
        """
        Enum Class


        See Also:
            `API InterruptReason <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1script.html#a298e9238891ddece524d1b3732aa33e4>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.script.InterruptReason', value)

        __ooo_ns__: str = 'com.sun.star.script'
        __ooo_full_ns__: str = 'com.sun.star.script.InterruptReason'
        __ooo_type_name__: str = 'enum'

        BreakPoint: InterruptReason = INTERRUPT_REASON_BreakPoint
        """
        script stopped at a breakpoint.
        """
        Cancel: InterruptReason = INTERRUPT_REASON_Cancel
        """
        script in the engine was cancelled.
        
        script execution was cancelled.
        """
        CompileError: InterruptReason = INTERRUPT_REASON_CompileError
        """
        script has invalid syntax.
        """
        RuntimeError: InterruptReason = INTERRUPT_REASON_RuntimeError
        """
        runtime error occurred during script execution.
        """
        Step: InterruptReason = INTERRUPT_REASON_Step
        """
        script stops because only one scripting engine command was executed.
        """
        StepOut: InterruptReason = INTERRUPT_REASON_StepOut
        """
        script stops because it leaves a function.
        """
        StepOver: InterruptReason = INTERRUPT_REASON_StepOver
        """
        script stops because one step was executed.
        """
        StepStatement: InterruptReason = INTERRUPT_REASON_StepStatement
        """
        script stop because one step was executed.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class InterruptReason(metaclass=UnoEnumMeta, type_name="com.sun.star.script.InterruptReason", name_space="com.sun.star.script"):
        """Dynamically created class that represents ``com.sun.star.script.InterruptReason`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['InterruptReason']
