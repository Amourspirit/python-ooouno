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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_controller import XController as XController_b00e0b8f
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924

class StartModule(XController_b00e0b8f):
    """
    Service Class

    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API StartModule <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1StartModule.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.StartModule'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithParentWindow(self, ContainerWindow: XWindow_713b0924) -> None:
        """
        """
        ...

__all__ = ['StartModule']

