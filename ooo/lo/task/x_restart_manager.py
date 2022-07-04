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
# Libre Office Version: 7.3
# Namespace: com.sun.star.task
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class XRestartManager(XInterface_8f010a43):
    """
    allows to try to restart the office.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XRestartManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XRestartManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XRestartManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XRestartManager'

    @abstractmethod
    def isRestartRequested(self, bInitialized: bool) -> bool:
        """
        allows to get info whether the restart has been requested and provide the initialization status.
        
        The office has to call this method just before the main loop has been started, with the TRUE as argument, so that the implementation knows that the office is initialized. If the method returns TRUE, the office should restart without starting the main loop.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def requestRestart(self, xInteractionHandler: 'XInteractionHandler_bf80e51') -> None:
        """
        let the office restart asynchronously

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XRestartManager']

