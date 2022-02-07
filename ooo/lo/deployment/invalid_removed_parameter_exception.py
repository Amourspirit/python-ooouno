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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.deployment
# Libre Office Version: 7.2
import typing
from ..uno.exception import Exception as Exception_85530a09
if typing.TYPE_CHECKING:
    from .x_package import XPackage as XPackage_cb1f0c4d

class InvalidRemovedParameterException(Exception_85530a09):
    """
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

    Extension: 'XPackage_cb1f0c4d' = None
    """
        the XPackage that was already bound to the provided url parameter during XPackageRegistry.bindPackage().
        
        Must not be NULL.
    """

    PreviousValue: bool = None
    """
        the value of the removed parameter which was used in XPackageRegistry.bindPackage() to create the currently existing XPackage object.
    """


