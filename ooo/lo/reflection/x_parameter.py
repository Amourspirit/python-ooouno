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
# Namespace: com.sun.star.reflection
from __future__ import annotations
from abc import abstractmethod
from .x_method_parameter import XMethodParameter as XMethodParameter_3b120f8d

class XParameter(XMethodParameter_3b120f8d):
    """
    Reflects a parameter of an interface method or a service constructor.
    
    This type supersedes XMethodParameter, which only supports parameters of interface methods (which cannot have rest parameters).
    
    **since**
    
        OOo 2.0

    See Also:
        `API XParameter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XParameter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.XParameter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.reflection.XParameter'

    @abstractmethod
    def isRestParameter(self) -> bool:
        """
        Returns whether this is a rest parameter.
        
        A rest parameter must always come last in a parameter list.
        
        Currently, only service constructors can have rest parameters, and those rest parameters must be in parameters of type any.
        """
        ...

__all__ = ['XParameter']

