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
# Namespace: com.sun.star.ui.dialogs
from enum import IntEnum


class WizardButton(object):
    """
    Const Class

    denotes the buttons found in a Wizard
    
    **since**
    
        OOo 3.3

    See Also:
        `API WizardButton <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1WizardButton.html>`_
    """
    NONE = 0
    """
    denotes none of the buttons in the wizard
    """
    NEXT = 1
    """
    denotes the button used to travel forward through the wizard
    """
    PREVIOUS = 2
    """
    denotes the button used to travel backward through the wizard
    """
    FINISH = 3
    """
    denotes the button used to finish the wizard
    """
    CANCEL = 4
    """
    denotes the button used to cancel the wizard
    """
    HELP = 5
    """
    denotes the button used to request help
    """


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
