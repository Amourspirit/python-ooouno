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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui.dialogs
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

    class WizardButton(metaclass=UnoConstMeta, type_name="com.sun.star.ui.dialogs.WizardButton", name_space="com.sun.star.ui.dialogs"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.ui.dialogs.WizardButton``"""
        pass

    class WizardButtonEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.ui.dialogs.WizardButton", name_space="com.sun.star.ui.dialogs"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.ui.dialogs.WizardButton`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.ui.dialogs import WizardButton as WizardButton
    else:
        # keep document generators happy
        from ....lo.ui.dialogs.wizard_button import WizardButton as WizardButton

    class WizardButtonEnum(IntEnum):
        """
        Enum of Const Class WizardButton

        denotes the buttons found in a Wizard
        
        **since**
        
            OOo 3.3
        """
        NONE = WizardButton.NONE
        """
        denotes none of the buttons in the wizard
        """
        NEXT = WizardButton.NEXT
        """
        denotes the button used to travel forward through the wizard
        """
        PREVIOUS = WizardButton.PREVIOUS
        """
        denotes the button used to travel backward through the wizard
        """
        FINISH = WizardButton.FINISH
        """
        denotes the button used to finish the wizard
        """
        CANCEL = WizardButton.CANCEL
        """
        denotes the button used to cancel the wizard
        """
        HELP = WizardButton.HELP
        """
        denotes the button used to request help
        """

__all__ = ['WizardButton', 'WizardButtonEnum']
