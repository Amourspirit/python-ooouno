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
# Namespace: com.sun.star.sdb.application
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

    class CopyTableContinuation(metaclass=UnoConstMeta, type_name="com.sun.star.sdb.application.CopyTableContinuation", name_space="com.sun.star.sdb.application"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdb.application.CopyTableContinuation``"""
        pass

    class CopyTableContinuationEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sdb.application.CopyTableContinuation", name_space="com.sun.star.sdb.application"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdb.application.CopyTableContinuation`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.sdb.application import CopyTableContinuation as CopyTableContinuation
    else:
        # keep document generators happy
        from ....lo.sdb.application.copy_table_continuation import CopyTableContinuation as CopyTableContinuation

    class CopyTableContinuationEnum(IntEnum):
        """
        Enum of Const Class CopyTableContinuation

        specifies the possible continuations when copying a table row via a CopyTableWizard failed.
        """
        Proceed = CopyTableContinuation.Proceed
        """
        indicates the error should be ignored, and copying should be continued.
        """
        CallNextHandler = CopyTableContinuation.CallNextHandler
        """
        is used to indicate the next registered XCopyTableListener should be called.
        """
        Cancel = CopyTableContinuation.Cancel
        """
        cancels the whole copying process
        """
        AskUser = CopyTableContinuation.AskUser
        """
        asks the user how the handle the error.
        
        The user can choose between ignoring the error and canceling the copy operation.
        """

__all__ = ['CopyTableContinuation', 'CopyTableContinuationEnum']
