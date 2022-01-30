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
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.security.CertificateContainerStatus import (NOCERT, TRUSTED, UNTRUSTED)

if TYPE_CHECKING or _DYNAMIC is False:


    class CertificateContainerStatus(Enum):
        """
        Enum Class

        

        See Also:
            `API CertificateContainerStatus <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1security.html#abd9126083ddb902b337383198d342e9f>`_
        """
        NOCERT = 'NOCERT'
        """
        The certificate was not found.
        """
        TRUSTED = 'TRUSTED'
        """
        The certificate was found and is trusted.
        """
        UNTRUSTED = 'UNTRUSTED'
        """
        The certificate was found but is untrusted.
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global CertificateContainerStatus
        _dict = {
            "NOCERT": NOCERT,
            "TRUSTED": TRUSTED,
            "UNTRUSTED": UNTRUSTED,
        }

        CertificateContainerStatus = type('CertificateContainerStatus', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(CertificateContainerStatus, k, v)

    _dynamic_enum()

__all__ = ['CertificateContainerStatus']

