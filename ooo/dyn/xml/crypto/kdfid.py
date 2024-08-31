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

    class KDFID(metaclass=UnoConstMeta, type_name="com.sun.star.xml.crypto.KDFID", name_space="com.sun.star.xml.crypto"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.xml.crypto.KDFID``"""
        pass

    class KDFIDEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.xml.crypto.KDFID", name_space="com.sun.star.xml.crypto"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.xml.crypto.KDFID`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.xml.crypto import KDFID as KDFID
    else:
        # keep document generators happy
        from ....lo.xml.crypto.kdfid import KDFID as KDFID

    class KDFIDEnum(IntEnum):
        """
        Enum of Const Class KDFID

        Constants to identify Key Derivation Function.
        
        **since**
        
            LibreOffice 24.2
        """
        PBKDF2 = KDFID.PBKDF2
        """
        PBKDF2.
        
        Derive key material from password. When used with ODF, the \"StartKeyGenerationAlgorithm\" is applied to the password and the result is passed to KDF.
        """
        PGP_RSA_OAEP_MGF1P = KDFID.PGP_RSA_OAEP_MGF1P
        """
        OpenPGP/GnuPG.
        
        Of course this is public key encryption, but it does produce key material for symmetric encryption. When used with ODF, the \"StartKeyGenerationAlgorithm\" digest is not used, as the input is not a password.
        """
        Argon2id = KDFID.Argon2id
        """
        Argon2id.
        
        Derive key material from password. When used with ODF, the \"StartKeyGenerationAlgorithm\" is applied to the password and the result is passed to KDF.
        """

__all__ = ['KDFID', 'KDFIDEnum']