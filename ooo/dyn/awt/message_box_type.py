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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import TYPE_CHECKING


if TYPE_CHECKING:

    class MessageBoxType(uno.Enum):
        """
        Enum Class


        See Also:
            `API MessageBoxType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#ad249d76933bdf54c35f4eaf51a5b7965>`_
        """
        __ooo_ns__: str = ...
        __ooo_full_ns__: str = ...
        __ooo_type_name__: str = ...

        @property
        def typeName(self) -> str:
            ...

        ERRORBOX: MessageBoxType = ...
        """
        A message box to provide an error message to the user.
        """
        INFOBOX: MessageBoxType = ...
        """
        A message box to inform the user about a certain event.
        """
        MESSAGEBOX: MessageBoxType = ...
        """
        A normal message box.
        """
        QUERYBOX: MessageBoxType = ...
        """
        A message box to query information from the user.
        """
        WARNINGBOX: MessageBoxType = ...
        """
        A message to warn the user about a certain problem.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class MessageBoxType(metaclass=UnoEnumMeta, type_name="com.sun.star.awt.MessageBoxType", name_space="com.sun.star.awt"):
        """Dynamically created class that represents ``com.sun.star.awt.MessageBoxType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['MessageBoxType']

