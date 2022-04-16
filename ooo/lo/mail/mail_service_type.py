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
# Libre Office Version: 7.3
from enum import Enum


class MailServiceType(Enum):
    """
    Enum Class

    ENUM MailServiceType

    See Also:
        `API MailServiceType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1mail.html#ad93fba9b1c1a9b0a2469f7c1fc392a06>`_
    """
    __ooo_ns__: str = 'com.sun.star.mail'
    __ooo_full_ns__: str = 'com.sun.star.mail.MailServiceType'
    __ooo_type_name__: str = 'enum'

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

__all__ = ['MailServiceType']

