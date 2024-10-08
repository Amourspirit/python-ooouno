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
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 2024.2
import typing
from .backend_access_exception import BackendAccessException as BackendAccessException_7cb5161f
from ...uno.x_interface import XInterface as XInterface_8f010a43

class InsufficientAccessRightsException(BackendAccessException_7cb5161f):
    """
    Exception Class

    Exception thrown when access to the underlying backend fails because of insufficient access rights to some needed resource.
    
    Examples of this include
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API InsufficientAccessRightsException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1configuration_1_1backend_1_1InsufficientAccessRightsException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.InsufficientAccessRightsException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.configuration.backend.InsufficientAccessRightsException'
    __pyunostruct__: str = 'com.sun.star.configuration.backend.InsufficientAccessRightsException'

    typeName: str = 'com.sun.star.configuration.backend.InsufficientAccessRightsException'
    """Literal Constant ``com.sun.star.configuration.backend.InsufficientAccessRightsException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, TargetException: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            TargetException (object, optional): TargetException value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "TargetException": TargetException,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        super()._init(**kwargs)


__all__ = ['InsufficientAccessRightsException']

