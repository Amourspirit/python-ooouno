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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.mail
# Libre Office Version: 7.2
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.mail.MailServiceType import (IMAP, POP3, SMTP)


class MailServiceType(Enum):
    """
    ENUM MailServiceType

    See Also:
        `API MailServiceType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1mail.html#ad93fba9b1c1a9b0a2469f7c1fc392a06>`_
    """
    IMAP = 'IMAP'
    """
    A IMAP service.
    """
    POP3 = 'POP3'
    """
    A POP3 service.
    """
    SMTP = 'SMTP'
    """
    A SMTP service.
    """

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global MailServiceType
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "IMAP": IMAP,
            "POP3": POP3,
            "SMTP": SMTP,
        }
        MailServiceType = type('MailServiceType', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(MailServiceType, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['MailServiceType']

