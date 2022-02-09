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
# Namespace: com.sun.star.inspection
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_property_control import XPropertyControl as XPropertyControl_3f260fe2

class XPropertyControlObserver(ABC):
    """
    specifies an interface for components to observer certain aspects of an XPropertyControl.
    
    **since**
    
        OOo 2.2

    See Also:
        `API XPropertyControlObserver <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XPropertyControlObserver.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.inspection'
    __ooo_full_ns__: str = 'com.sun.star.inspection.XPropertyControlObserver'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.inspection.XPropertyControlObserver'

    @abstractmethod
    def focusGained(self, Control: 'XPropertyControl_3f260fe2') -> None:
        """
        notifies the observer that a certain XPropertyControl's UI representation gained the focus.
        """
    @abstractmethod
    def valueChanged(self, Control: 'XPropertyControl_3f260fe2') -> None:
        """
        notifies the observer that a certain XPropertyControl's value changed.
        """


__all__ = ['XPropertyControlObserver']

