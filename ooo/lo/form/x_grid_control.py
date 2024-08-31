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
# Namespace: com.sun.star.form
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_grid import XGrid as XGrid_6836089a
from .x_grid_field_data_supplier import XGridFieldDataSupplier as XGridFieldDataSupplier_34aa0f4c
if typing.TYPE_CHECKING:
    from .x_grid_control_listener import XGridControlListener as XGridControlListener_19a70ec1

class XGridControl(XGrid_6836089a, XGridFieldDataSupplier_34aa0f4c):
    """
    specifies (some) functionality provided by a grid control (aka table control)
    
    **since**
    
        OOo 3.1

    See Also:
        `API XGridControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XGridControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.XGridControl'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.XGridControl'

    @abstractmethod
    def addGridControlListener(self, listener: XGridControlListener_19a70ec1) -> None:
        """
        registers a listener which is to be notified about state changes in the grid control
        """
        ...
    @abstractmethod
    def removeGridControlListener(self, listener: XGridControlListener_19a70ec1) -> None:
        """
        revokes a previously registered grid control listener
        """
        ...

__all__ = ['XGridControl']

