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
# Namespace: com.sun.star.security
# Libre Office Version: 7.2
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.security.ExtAltNameType import (DIRECTORY_NAME, DNS_NAME, EDI_PARTY_NAME, IP_ADDRESS, OTHER_NAME, REGISTERED_ID, RFC822_NAME, URL, X400_ADDRESS)


class ExtAltNameType(Enum):
    """
    

    See Also:
        `API ExtAltNameType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1security.html#a5c5a31742567126d2ba88393b05efa3f>`_
    """
    DIRECTORY_NAME = 'DIRECTORY_NAME'
    """
    Currently unsupported.
    """
    DNS_NAME = 'DNS_NAME'
    """
    The entry contains a dns name.
    
    The value of CertAltNameEntry contains a OUString.
    """
    EDI_PARTY_NAME = 'EDI_PARTY_NAME'
    """
    Currently unsupported.
    """
    IP_ADDRESS = 'IP_ADDRESS'
    """
    The entry contains an IP address.
    
    The value of CertAltNameEntry contains a Sequence of sal_Int8.
    """
    OTHER_NAME = 'OTHER_NAME'
    """
    Customize name/value pair The value of CertAltNameEntry contains a NamedValue.
    """
    REGISTERED_ID = 'REGISTERED_ID'
    """
    The entry contains a registered id.
    
    The value of CertAltNameEntry contains a OUString.
    """
    RFC822_NAME = 'RFC822_NAME'
    """
    The entry contains rfc822 name.
    
    The value of CertAltNameEntry contains an OUString.
    """
    URL = 'URL'
    """
    The entry contains a URL.
    
    The value of CertAltNameEntry contains a OUString.
    """
    X400_ADDRESS = 'X400_ADDRESS'
    """
    Currently unsupported.
    """

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global ExtAltNameType
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "DIRECTORY_NAME": DIRECTORY_NAME,
            "DNS_NAME": DNS_NAME,
            "EDI_PARTY_NAME": EDI_PARTY_NAME,
            "IP_ADDRESS": IP_ADDRESS,
            "OTHER_NAME": OTHER_NAME,
            "REGISTERED_ID": REGISTERED_ID,
            "RFC822_NAME": RFC822_NAME,
            "URL": URL,
            "X400_ADDRESS": X400_ADDRESS,
        }
        ExtAltNameType = type('ExtAltNameType', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(ExtAltNameType, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['ExtAltNameType']

