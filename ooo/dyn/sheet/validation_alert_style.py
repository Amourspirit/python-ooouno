# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import TYPE_CHECKING


if TYPE_CHECKING:

    class ValidationAlertStyle(uno.Enum):
        """
        Enum Class


        See Also:
            `API ValidationAlertStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#aecf58149730f4c8c5c18c70f3c7c5db7>`_
        """
        __ooo_ns__: str = ...
        __ooo_full_ns__: str = ...
        __ooo_type_name__: str = ...

        @property
        def typeName(self) -> str:
            ...

        INFO: ValidationAlertStyle = ...
        """
        information message is shown and the user is asked whether the change will be accepted (defaulted to \"Yes\").
        """
        MACRO: ValidationAlertStyle = ...
        """
        macro is executed.
        """
        STOP: ValidationAlertStyle = ...
        """
        error message is shown and the change is rejected.
        """
        WARNING: ValidationAlertStyle = ...
        """
        warning message is shown and the user is asked whether the change will be accepted (defaulted to \"No\").
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class ValidationAlertStyle(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.ValidationAlertStyle", name_space="com.sun.star.sheet"):
        """Dynamically created class that represents ``com.sun.star.sheet.ValidationAlertStyle`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['ValidationAlertStyle']

