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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.embed
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from com.sun.star.embed import XLinkFactory as XLinkFactory
    setattr(XLinkFactory, '__ooo_ns__', 'com.sun.star.embed')
    setattr(XLinkFactory, '__ooo_full_ns__', 'com.sun.star.embed.XLinkFactory')
    setattr(XLinkFactory, '__ooo_type_name__', 'interface')
else:
    if TYPE_CHECKING:
        from com.sun.star.embed import XLinkFactory as XLinkFactory
    else:
        # keep document generators happy
        from ...lo.embed.x_link_factory import XLinkFactory as XLinkFactory

__all__ = ['XLinkFactory']

