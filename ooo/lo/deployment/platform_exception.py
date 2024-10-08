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
from .x_package import XPackage as XPackage_cb1f0c4d

class PlatformException(Exception_85530a09):
    """
    Exception Class

    A DeploymentException indicates that the current platform is not supported.
    
    **since**
    
        OOo 3.0

    See Also:
        `API PlatformException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1deployment_1_1PlatformException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.PlatformException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.deployment.PlatformException'
    __pyunostruct__: str = 'com.sun.star.deployment.PlatformException'

    typeName: str = 'com.sun.star.deployment.PlatformException'
    """Literal Constant ``com.sun.star.deployment.PlatformException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, package: typing.Optional[XPackage_cb1f0c4d] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            package (XPackage, optional): package value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "package": package,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._package = kwargs["package"]
        inst_keys = ('package',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def package(self) -> XPackage_cb1f0c4d:
        """
        The package which does not support the current platform.
        """
        return self._package
    
    @package.setter
    def package(self, value: XPackage_cb1f0c4d) -> None:
        self._package = value


__all__ = ['PlatformException']

