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
# Namespace: com.sun.star.accessibility
from __future__ import annotations
from .x_accessible import XAccessible as XAccessible_1cbc0eb6

class Accessible(XAccessible_1cbc0eb6):
    """
    Service Class

    Every class has to support this service in order to be accessible.
    
    It provides the means to derive a XAccessibleContext object–which may but usually is not the same object as the object that supports the XAccessible interface–that provides the actual information that is needed to make it accessible.
    
    Service Accessible is just a wrapper for the interface XAccessible. See the interface's documentation for more information.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Accessible <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1accessibility_1_1Accessible.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.Accessible'
    __ooo_type_name__: str = 'service'


__all__ = ['Accessible']

