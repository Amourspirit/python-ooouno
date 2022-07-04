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
# Namespace: com.sun.star.report.meta
import typing
from abc import abstractmethod, abstractproperty
from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from .x_function_category import XFunctionCategory as XFunctionCategory_59e21055
    from ...sheet.function_argument import FunctionArgument as FunctionArgument_f1080daa

class XFunctionDescription(XPropertySet_bc180bfa):
    """
    identifies a XFunctionDescription which allows to retrieve the meta data of all supported functions.

    See Also:
        `API XFunctionDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1meta_1_1XFunctionDescription.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report.meta'
    __ooo_full_ns__: str = 'com.sun.star.report.meta.XFunctionDescription'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.meta.XFunctionDescription'

    @abstractmethod
    def createFormula(self, arguments: 'typing.Tuple[str, ...]') -> str:
        """

        Raises:
            com.sun.star.lang.DisposedException: ``DisposedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractproperty
    def Arguments(self) -> 'typing.Tuple[FunctionArgument_f1080daa, ...]':
        """
        returns a sequence of localized descriptions of the function's arguments (in the order specified by the function).
        """
        ...

    @abstractproperty
    def Category(self) -> 'XFunctionCategory_59e21055':
        """
        specifies the category number.
        """
        ...

    @abstractproperty
    def Description(self) -> str:
        """
        returns a localized description of the function.
        """
        ...

    @abstractproperty
    def Name(self) -> str:
        """
        returns the localized function's name.
        """
        ...

    @abstractproperty
    def Signature(self) -> str:
        """
        returns the signature of the function.
        """
        ...


__all__ = ['XFunctionDescription']

