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
# Namespace: com.sun.star.ucb
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSourceInitialization(XInterface_8f010a43):
    """
    provides the initialization of a component with any source object.

    See Also:
        `API XSourceInitialization <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XSourceInitialization.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XSourceInitialization'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XSourceInitialization'

    @abstractmethod
    def setSource(self, Source: 'XInterface_8f010a43') -> None:
        """
        provides the initialization of a component with any source object.
        
        The service description has to specify which type of interface must be set as parameter.
        
        Hopefully you will only use this, when Source is a com.sun.star.lang.XComponent and this is a com.sun.star.lang.XEventListener. Then you should call com.sun.star.lang.XComponent.addEventListener() from inside the implementation of this method.

        Raises:
            AlreadyInitializedException: ``AlreadyInitializedException``
        """

__all__ = ['XSourceInitialization']
