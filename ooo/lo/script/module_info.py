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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43


class ModuleInfo(object):
    """
    Struct Class


    See Also:
        `API ModuleInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1ModuleInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.ModuleInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.ModuleInfo'
    """Literal Constant ``com.sun.star.script.ModuleInfo``"""

    def __init__(self, ModuleObject: XInterface_8f010a43 = None, ModuleType: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``ModuleObject`` can be another ``ModuleInfo`` instance,
                in which case other named args are ignored.

        Arguments:
            ModuleObject (XInterface, optional): ModuleObject value
            ModuleType (int, optional): ModuleType value
        """
        if isinstance(ModuleObject, ModuleInfo):
            oth: ModuleInfo = ModuleObject
            self._module_object = oth.ModuleObject
            self._module_type = oth.ModuleType
            return
        else:
            self._module_object = ModuleObject
            self._module_type = ModuleType



    @property
    def ModuleObject(self) -> XInterface_8f010a43:
        return self._module_object
    
    @ModuleObject.setter
    def ModuleObject(self, value: XInterface_8f010a43) -> None:
        self._module_object = value

    @property
    def ModuleType(self) -> int:
        return self._module_type
    
    @ModuleType.setter
    def ModuleType(self, value: int) -> None:
        self._module_type = value


__all__ = ['ModuleInfo']