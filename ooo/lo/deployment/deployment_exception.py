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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.deployment
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class DeploymentException(Exception_85530a09):
    """
    Exception Class

    A DeploymentException reflects a deployment error.
    
    **since**
    
        OOo 2.0

    See Also:
        `API DeploymentException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1deployment_1_1DeploymentException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.DeploymentException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.deployment.DeploymentException'
    __pyunostruct__: str = 'com.sun.star.deployment.DeploymentException'

    typeName: str = 'com.sun.star.deployment.DeploymentException'
    """Literal Constant ``com.sun.star.deployment.DeploymentException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Cause: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Cause (object, optional): Cause value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Cause": Cause,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._cause = kwargs["Cause"]
        inst_keys = ('Cause',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Cause(self) -> object:
        """
        reflects the cause of the error.
        
        Commonly an exception.
        """
        return self._cause
    
    @Cause.setter
    def Cause(self, value: object) -> None:
        self._cause = value


__all__ = ['DeploymentException']

