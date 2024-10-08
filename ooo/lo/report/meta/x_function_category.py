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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.report.meta
from __future__ import annotations
import typing
from abc import abstractmethod
from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ...container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from .x_function_description import XFunctionDescription as XFunctionDescription_8d8d119b

class XFunctionCategory(XPropertySet_bc180bfa, XIndexAccess_f0910d6d):
    """
    identifies a XFunctionCategory which allows to retrieve the meta data of all supported functions.

    See Also:
        `API XFunctionCategory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1meta_1_1XFunctionCategory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report.meta'
    __ooo_full_ns__: str = 'com.sun.star.report.meta.XFunctionCategory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.meta.XFunctionCategory'

    @abstractmethod
    def getFunction(self, position: int) -> XFunctionDescription_8d8d119b:
        """
        same as getByIndex.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @property
    @abstractmethod
    def Name(self) -> str:
        """
        returns the localized category's name.
        """
        ...

    @property
    @abstractmethod
    def Number(self) -> int:
        """
        specifies the category number.
        """
        ...


__all__ = ['XFunctionCategory']

