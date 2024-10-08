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
# Namespace: com.sun.star.task
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_status_indicator_factory import XStatusIndicatorFactory as XStatusIndicatorFactory_49e4100c
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924
    from ..frame.x_frame import XFrame as XFrame_7a570956

class StatusIndicatorFactory(XStatusIndicatorFactory_49e4100c):
    """
    Service Class

    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API StatusIndicatorFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1task_1_1StatusIndicatorFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.StatusIndicatorFactory'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithFrame(self, Frame: XFrame_7a570956, DisableReschedule: bool, AllowParentShow: bool) -> None:
        """
        """
        ...
    @abstractmethod
    def createWithWindow(self, ParentWindow: XWindow_713b0924, DisableReschedule: bool, AllowParentShow: bool) -> None:
        """
        """
        ...

__all__ = ['StatusIndicatorFactory']

