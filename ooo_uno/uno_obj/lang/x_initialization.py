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
# Namespace: com.sun.star.lang
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XInitialization(XInterface_8f010a43):
    """
    initializes an object directly after its creation.
    
    This interface works together with factories. If you want to initialize the object after creation, you should support this interface and you may support other interfaces which offer type-safe initialization methods.
    
    Instead of calling XSingleComponentFactory.createInstanceWithContext() and later initialize(), you should call XSingleComponentFactory.createInstanceWithArgumentsAndContext() to pass the arguments to the instance. The reason is, that a component may want to return the same instance for the same set of parameters, and it can do so by implementing the factory itself.

    See Also:
        `API XInitialization <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XInitialization.html>`_
    """

    @abstractmethod
    def initialize(self, aArguments: 'typing.List[object]') -> None:
        """
        initializes the object.
        
        It should be called directly after the object is created.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """

__all__ = ['XInitialization']

