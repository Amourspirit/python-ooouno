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

class InvalidRemovedParameterException(Exception_85530a09):
    """
    Exception Class

    indicates that XPackageRegistry.bindPackage() was previously called with a different value for the removed parameter and that the XPackage object created by that call still exist.
    
    **since**
    
        OOo 3.3

    See Also:
        `API InvalidRemovedParameterException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1deployment_1_1InvalidRemovedParameterException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.InvalidRemovedParameterException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.deployment.InvalidRemovedParameterException'
    __pyunostruct__: str = 'com.sun.star.deployment.InvalidRemovedParameterException'

    typeName: str = 'com.sun.star.deployment.InvalidRemovedParameterException'
    """Literal Constant ``com.sun.star.deployment.InvalidRemovedParameterException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, PreviousValue: typing.Optional[bool] = False, Extension: typing.Optional[XPackage_cb1f0c4d] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            PreviousValue (bool, optional): PreviousValue value.
            Extension (XPackage, optional): Extension value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "PreviousValue": PreviousValue,
            "Extension": Extension,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._previous_value = kwargs["PreviousValue"]
        self._extension = kwargs["Extension"]
        inst_keys = ('PreviousValue', 'Extension')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def PreviousValue(self) -> bool:
        """
        the value of the removed parameter which was used in XPackageRegistry.bindPackage() to create the currently existing XPackage object.
        """
        return self._previous_value
    
    @PreviousValue.setter
    def PreviousValue(self, value: bool) -> None:
        self._previous_value = value

    @property
    def Extension(self) -> XPackage_cb1f0c4d:
        """
        the XPackage that was already bound to the provided url parameter during XPackageRegistry.bindPackage().
        
        Must not be NULL.
        """
        return self._extension
    
    @Extension.setter
    def Extension(self, value: XPackage_cb1f0c4d) -> None:
        self._extension = value


__all__ = ['InvalidRemovedParameterException']

