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
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import MessageBoxButtons as MessageBoxButtons
    if hasattr(MessageBoxButtons, '_constants') and isinstance(MessageBoxButtons._constants, dict):
        MessageBoxButtons._constants['__ooo_ns__'] = 'com.sun.star.awt'
        MessageBoxButtons._constants['__ooo_full_ns__'] = 'com.sun.star.awt.MessageBoxButtons'
        MessageBoxButtons._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global MessageBoxButtonsEnum
        ls = [f for f in dir(MessageBoxButtons) if not callable(getattr(MessageBoxButtons, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(MessageBoxButtons, name)
        MessageBoxButtonsEnum = IntEnum('MessageBoxButtonsEnum', _dict)
    build_enum()
else:
    from ...lo.awt.message_box_buttons import MessageBoxButtons as MessageBoxButtons

    class MessageBoxButtonsEnum(IntEnum):
        """
        Enum of Const Class MessageBoxButtons

        defines constants for the possible message box button combinations.
        """
        BUTTONS_OK = MessageBoxButtons.BUTTONS_OK
        """
        specifies a message with \"OK\" button.
        """
        BUTTONS_OK_CANCEL = MessageBoxButtons.BUTTONS_OK_CANCEL
        """
        specifies a message box with \"OK\" and \"CANCEL\" button.
        """
        BUTTONS_YES_NO = MessageBoxButtons.BUTTONS_YES_NO
        """
        specifies a message box with \"YES\" and \"NO\" button.
        """
        BUTTONS_YES_NO_CANCEL = MessageBoxButtons.BUTTONS_YES_NO_CANCEL
        """
        specifies a message box with \"YES\", \"NO\" and \"CANCEL\" button.
        """
        BUTTONS_RETRY_CANCEL = MessageBoxButtons.BUTTONS_RETRY_CANCEL
        """
        specifies a message box with \"RETRY\" and \"CANCEL\" button.
        """
        BUTTONS_ABORT_IGNORE_RETRY = MessageBoxButtons.BUTTONS_ABORT_IGNORE_RETRY
        """
        specifies a message box with \"ABORT\", \"IGNORE\" and \"RETRY\" button.
        """
        DEFAULT_BUTTON_OK = MessageBoxButtons.DEFAULT_BUTTON_OK
        """
        specifies that OK is the default button.
        """
        DEFAULT_BUTTON_CANCEL = MessageBoxButtons.DEFAULT_BUTTON_CANCEL
        """
        specifies that CANCEL is the default button.
        """
        DEFAULT_BUTTON_RETRY = MessageBoxButtons.DEFAULT_BUTTON_RETRY
        """
        specifies that RETRY is the default button.
        """
        DEFAULT_BUTTON_YES = MessageBoxButtons.DEFAULT_BUTTON_YES
        """
        specifies that YES is the default button.
        """
        DEFAULT_BUTTON_NO = MessageBoxButtons.DEFAULT_BUTTON_NO
        """
        specifies that NO is the default button.
        """
        DEFAULT_BUTTON_IGNORE = MessageBoxButtons.DEFAULT_BUTTON_IGNORE
        """
        specifies that IGNORE is the default button.
        """

__all__ = ['MessageBoxButtons', 'MessageBoxButtonsEnum']
