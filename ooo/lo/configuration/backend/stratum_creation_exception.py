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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .backend_setup_exception import BackendSetupException as BackendSetupException_68ae15de
from ...uno.x_interface import XInterface as XInterface_8f010a43

class StratumCreationException(BackendSetupException_68ae15de):
    """
    Exception Class

    is passed to an InteractionHandler when creating a stratum backend fails.
    
    **since**
    
        OOo 2.0

    See Also:
        `API StratumCreationException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1configuration_1_1backend_1_1StratumCreationException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.StratumCreationException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.configuration.backend.StratumCreationException'
    __pyunostruct__: str = 'com.sun.star.configuration.backend.StratumCreationException'

    typeName: str = 'com.sun.star.configuration.backend.StratumCreationException'
    """Literal Constant ``com.sun.star.configuration.backend.StratumCreationException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, BackendException: typing.Optional[object] = None, StratumService: typing.Optional[str] = '', StratumData: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            BackendException (object, optional): BackendException value.
            StratumService (str, optional): StratumService value.
            StratumData (str, optional): StratumData value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "BackendException": BackendException,
            "StratumService": StratumService,
            "StratumData": StratumData,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._stratum_service = kwargs["StratumService"]
        self._stratum_data = kwargs["StratumData"]
        inst_keys = ('StratumService', 'StratumData')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def StratumService(self) -> str:
        """
        Identifier of the stratum service that could not be created.
        """
        return self._stratum_service
    
    @StratumService.setter
    def StratumService(self, value: str) -> None:
        self._stratum_service = value

    @property
    def StratumData(self) -> str:
        """
        Initialization data passed to the stratum instance.
        """
        return self._stratum_data
    
    @StratumData.setter
    def StratumData(self, value: str) -> None:
        self._stratum_data = value


__all__ = ['StratumCreationException']

