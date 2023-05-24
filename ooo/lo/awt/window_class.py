# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from typing import cast
from enum import Enum
from com.sun.star.awt.WindowClass import WindowClassProto

class WindowClass(Enum):
    """
    Enum Class


    See Also:
        `API WindowClass <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#add6041e42e466bb2170771f84663460b>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.WindowClass'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.awt.WindowClass'

    CONTAINER = cast(WindowClassProto, 'CONTAINER')
    """
    is a container that may contain other components.
    
    It is not a top window.
    """
    MODALTOP = cast(WindowClassProto, 'MODALTOP')
    """
    is a modal top level window on the desktop.
    
    It is also a container.
    """
    SIMPLE = cast(WindowClassProto, 'SIMPLE')
    """
    is the simplest window.
    
    It can be a container.
    """
    TOP = cast(WindowClassProto, 'TOP')
    """
    specifies a top level window on the desktop.
    
    It is also a container.
    """

__all__ = ['WindowClass']

