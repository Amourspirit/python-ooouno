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
# Namespace: com.sun.star.security
# Libre Office Version: 7.4
from typing import cast
from enum import Enum
from com.sun.star.security.ExtAltNameType import ExtAltNameTypeProto

class ExtAltNameType(Enum):
    """
    Enum Class


    See Also:
        `API ExtAltNameType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1security.html#a5c5a31742567126d2ba88393b05efa3f>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.ExtAltNameType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.security.ExtAltNameType'

    DIRECTORY_NAME = cast(ExtAltNameTypeProto, 'DIRECTORY_NAME')
    """
    Currently unsupported.
    """
    DNS_NAME = cast(ExtAltNameTypeProto, 'DNS_NAME')
    """
    The entry contains a dns name.
    
    The value of CertAltNameEntry contains a OUString.
    """
    EDI_PARTY_NAME = cast(ExtAltNameTypeProto, 'EDI_PARTY_NAME')
    """
    Currently unsupported.
    """
    IP_ADDRESS = cast(ExtAltNameTypeProto, 'IP_ADDRESS')
    """
    The entry contains an IP address.
    
    The value of CertAltNameEntry contains a Sequence of sal_Int8.
    """
    OTHER_NAME = cast(ExtAltNameTypeProto, 'OTHER_NAME')
    """
    Customize name/value pair The value of CertAltNameEntry contains a NamedValue.
    """
    REGISTERED_ID = cast(ExtAltNameTypeProto, 'REGISTERED_ID')
    """
    The entry contains a registered id.
    
    The value of CertAltNameEntry contains a OUString.
    """
    RFC822_NAME = cast(ExtAltNameTypeProto, 'RFC822_NAME')
    """
    The entry contains rfc822 name.
    
    The value of CertAltNameEntry contains an OUString.
    """
    URL = cast(ExtAltNameTypeProto, 'URL')
    """
    The entry contains a URL.
    
    The value of CertAltNameEntry contains a OUString.
    """
    X400_ADDRESS = cast(ExtAltNameTypeProto, 'X400_ADDRESS')
    """
    Currently unsupported.
    """

__all__ = ['ExtAltNameType']

