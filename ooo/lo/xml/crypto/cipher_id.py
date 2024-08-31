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
# Namespace: com.sun.star.xml.crypto


class CipherID(object):
    """
    Const Class

    The constant set contains identifiers of supported cipher-creation algorithms.
    
    **since**
    
        OOo 3.4

    See Also:
        `API CipherID <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1CipherID.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.CipherID'
    __ooo_type_name__: str = 'const'

    AES_CBC_W3C_PADDING = 1
    """
    identifier of AES algorithm in CBC mode with W3C padding
    """
    BLOWFISH_CFB_8 = 2
    """
    identifier of the Blowfish algorithm in 8-bit CFB mode
    """
    AES_GCM_W3C = 3
    """
    identifier of AES algorithm in GCM mode with 96-bit IV prefixed, 128 bit authentication tag, and no padding, as specified in [XMLENC-CORE1] 5.2.4 AES-GCM.
    
    **since**
    
        LibreOffice 24.2
    """

__all__ = ['CipherID']
