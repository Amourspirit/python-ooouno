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
# Libre Office Version: 7.3
# Namespace: com.sun.star.util
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XStringSubstitution(XInterface_8f010a43):
    """
    A common interface for substituting string variables with other strings.
    
    The substitution algorithm and the syntax for a string variable are not part of this interface definition. Please look at the documentation of the implementation that must specify these parameters.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XStringSubstitution <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XStringSubstitution.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XStringSubstitution'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XStringSubstitution'

    @abstractmethod
    def getSubstituteVariableValue(self, variable: str) -> str:
        """
        Returns the current value of a variable.
        
        The method iterates through its internal variable list and tries to find the given variable. If the variable is unknown a com.sun.star.container.NoSuchElementException is thrown.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def reSubstituteVariables(self, aText: str) -> str:
        """
        Tries to replace parts of aText with variables that represents these sub strings.
        
        The method iterates through its internal variable list and tries to match parts of the given string Tries to replace parts of aText with variables that represents these sub strings.If more than one variable matches the one with the longest matching sub string will be chosen.
        """
        ...
    @abstractmethod
    def substituteVariables(self, aText: str, bSubstRequired: bool) -> str:
        """
        Exchanges variables inside a given text with a substitution text defined for the variables.
        
        The method iterates through its internal variables list to match the variables in the given string. A match replaces the variable with the string defined for this variable. If no variable can be found in the string it will be returned unchanged. The behavior if a variable is found in the string but it is unknown for the implementation depends on the parameter bSubstRequired.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...

__all__ = ['XStringSubstitution']

