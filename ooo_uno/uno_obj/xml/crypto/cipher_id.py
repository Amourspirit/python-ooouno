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
# Namespace: com.sun.star.xml.crypto
from enum import IntFlag


class CipherID(object):
    """
    Const Class

    The constant set contains identifiers of supported cipher-creation algorithms.
    
    **since**
    
        OOo 3.4

    See Also:
        `API CipherID <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1CipherID.html>`_
    """
    AES_CBC_W3C_PADDING = 1
    """
    identifier of AES algorithm in CBC mode with W3C padding
    """
    BLOWFISH_CFB_8 = 2
    """
    identifier of the Blowfish algorithm in 8-bit CFB mode
    """


class CipherIDEnum(IntFlag):
    """
    Enum of Const Class CipherID

    The constant set contains identifiers of supported cipher-creation algorithms.
    
    **since**
    
        OOo 3.4
    """
    AES_CBC_W3C_PADDING = CipherID.AES_CBC_W3C_PADDING
    """
    identifier of AES algorithm in CBC mode with W3C padding
    """
    BLOWFISH_CFB_8 = CipherID.BLOWFISH_CFB_8
    """
    identifier of the Blowfish algorithm in 8-bit CFB mode
    """

__all__ = ['CipherID', 'CipherIDEnum']
