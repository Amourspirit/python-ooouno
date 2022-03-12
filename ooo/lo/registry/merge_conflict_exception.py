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
# Namespace: com.sun.star.registry
# Libre Office Version: 7.2
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class MergeConflictException(Exception_85530a09):
    """
    Exception Class

    is thrown if entries of two registries are contradictory in the context of XSimpleRegistry.mergeKey()e() method.

    See Also:
        `API MergeConflictException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1registry_1_1MergeConflictException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.registry'
    __ooo_full_ns__: str = 'com.sun.star.registry.MergeConflictException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.registry.MergeConflictException'
    __pyunostruct__: str = 'com.sun.star.registry.MergeConflictException'

    typeName: str = 'com.sun.star.registry.MergeConflictException'
    """Literal Constant ``com.sun.star.registry.MergeConflictException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        super()._init(**kwargs)


