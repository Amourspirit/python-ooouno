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
# Libre Office Version: 7.3
# Namespace: com.sun.star.xml.crypto
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.xml.crypto import CipherID as CipherID
    if hasattr(CipherID, '_constants') and isinstance(CipherID._constants, dict):
        CipherID._constants['__ooo_ns__'] = 'com.sun.star.xml.crypto'
        CipherID._constants['__ooo_full_ns__'] = 'com.sun.star.xml.crypto.CipherID'
        CipherID._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CipherIDEnum
        ls = [f for f in dir(CipherID) if not callable(getattr(CipherID, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CipherID, name)
        CipherIDEnum = IntFlag('CipherIDEnum', _dict)
    build_enum()
else:
    from ....lo.xml.crypto.cipher_id import CipherID as CipherID

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
