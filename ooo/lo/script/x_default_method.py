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
# Namespace: com.sun.star.script
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XDefaultMethod(XInterface_8f010a43):
    """
    An object supporting this interface indicates to interested parties or clients the name of the default method for this object.
    
    For example where ExampleObject is an instance of an Object that supports this interface which returns the default method name \"defaultMethod\".A scripting engine could use this information to support syntax like
    
    \"ExampleObject( Param1 ... ParamN )\"
    
    which would be equivalent to writing
    
    \"ExampleObject.defaultMethod( Param1 ... ParamN )\"

    See Also:
        `API XDefaultMethod <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XDefaultMethod.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XDefaultMethod'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XDefaultMethod'

    @abstractmethod
    def getDefaultMethodName(self) -> str:
        """
        Returns the name of the default method.
        """
        ...

__all__ = ['XDefaultMethod']

