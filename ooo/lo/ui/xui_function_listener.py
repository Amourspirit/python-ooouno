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
# Namespace: com.sun.star.ui
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a

class XUIFunctionListener(XEventListener_c7230c4a):
    """
    special interface to receive notification that a user interface element will execute a function.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUIFunctionListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XUIFunctionListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XUIFunctionListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XUIFunctionListener'

    @abstractmethod
    def functionExecute(self, aUIElementName: str, aCommand: str) -> None:
        """
        gets called to notify a component that a user interface element wants to execute a function.
        """
        ...

__all__ = ['XUIFunctionListener']

