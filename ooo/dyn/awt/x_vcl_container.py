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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.uno_helper import unoclass
    def _dynamic_interface() -> None:
        # Dynamically create uno interface using uno
        global XVclContainer
        XVclContainer = unoclass(
            'com.sun.star.awt.XVclContainer')
        setattr(XVclContainer, ' __ooo_ns__', 'com.sun.star.awt')
        setattr(XVclContainer, ' __ooo_full_ns__', 'com.sun.star.awt.XVclContainer')
        setattr(XVclContainer, ' __ooo_type_name__', 'interface')

    _dynamic_interface()
else:
    from ...lo.awt.x_vcl_container import XVclContainer as XVclContainer

__all__ = ['XVclContainer']

