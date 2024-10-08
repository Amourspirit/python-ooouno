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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XGrid(XInterface_8f010a43):
    """
    provides the possibility of setting and retrieving the position of the current cell in a grid control.
    
    Note that a grid control does not allow free control over the current row: In such a control, every line represents a row of data of the underlying com.sun.star.form.component.DataForm. Thus, the current row of the grid control always equals the current row of the com.sun.star.form.component.DataForm, and can be affected only by changing the latter.The current column of a grid control, whoever, can be freely controlled.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XGrid <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XGrid.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.XGrid'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.XGrid'

    @abstractmethod
    def getCurrentColumnPosition(self) -> int:
        """
        retrieves the current column position.
        """
        ...
    @abstractmethod
    def setCurrentColumnPosition(self, nPos: int) -> None:
        """
        sets the current column position.
        """
        ...

__all__ = ['XGrid']

