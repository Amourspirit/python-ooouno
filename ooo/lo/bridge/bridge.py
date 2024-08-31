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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.bridge
from __future__ import annotations
from .x_bridge import XBridge as XBridge_8e4e0a1a
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca

class Bridge(XBridge_8e4e0a1a, XComponent_98dc0ab5, XInitialization_d46c0cca):
    """
    Service Class

    This meta service allows the bridgefactory service to instantiate an interprocess bridge using a certain transfer protocol.
    
    Components, that support a certain protocol, must have at least two service names:
    
    The protocol name should be written as common servicenames, first letter is a capital letter, the rest in small letters postfixed by Bridge (e.g.: com.sun.star.bridge.UrpBridge would be correct servicename for the \"urp\" protocol). However, the protocol names are compared case insensitive. If there exist two services supporting the same protocol, it is arbitrary which one is chosen, so this should be omitted.

    See Also:
        `API Bridge <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1bridge_1_1Bridge.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge'
    __ooo_full_ns__: str = 'com.sun.star.bridge.Bridge'
    __ooo_type_name__: str = 'service'


__all__ = ['Bridge']

