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
# Namespace: com.sun.star.reflection
import typing
from abc import abstractmethod
from .x_idl_member import XIdlMember as XIdlMember_e3400cfc
if typing.TYPE_CHECKING:
    from .method_mode import MethodMode as MethodMode_e4910d19
    from .param_info import ParamInfo as ParamInfo_d7210cb0
    from .x_idl_class import XIdlClass as XIdlClass_d63a0c9a

class XIdlMethod(XIdlMember_e3400cfc):
    """
    Reflects an IDL interface method.

    See Also:
        `API XIdlMethod <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XIdlMethod.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.XIdlMethod'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.reflection.XIdlMethod'

    @abstractmethod
    def getExceptionTypes(self) -> 'typing.Tuple[XIdlClass_d63a0c9a, ...]':
        """
        Returns the declared exceptions types of the reflected method.
        """
    @abstractmethod
    def getMode(self) -> 'MethodMode_e4910d19':
        """
        Returns the method mode in which calls are run, i.e.
        
        either oneway or twoway. Method mode oneway denotes that a call may be run asynchronously (thus having no out parameters or return value)
        """
    @abstractmethod
    def getParameterInfos(self) -> 'typing.Tuple[ParamInfo_d7210cb0, ...]':
        """
        Returns formal parameter information of the reflected method in order of IDL declaration.
        
        Parameter information reflects the parameter's access mode (in, out, inout), the parameter's name and formal type.
        """
    @abstractmethod
    def getParameterTypes(self) -> 'typing.Tuple[XIdlClass_d63a0c9a, ...]':
        """
        Returns the formal parameter types of the reflected method in order of IDL declaration.
        """
    @abstractmethod
    def getReturnType(self) -> 'XIdlClass_d63a0c9a':
        """
        Returns the return type of the reflected method.
        """
    @abstractmethod
    def invoke(self, obj: object, args: object) -> object:
        """
        Invokes the reflected method on a given object with the given parameters.
        
        The parameters may be widening converted to fit their exact IDL type, meaning no loss of information.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.reflection.InvocationTargetException: ``InvocationTargetException``
        """


__all__ = ['XIdlMethod']

