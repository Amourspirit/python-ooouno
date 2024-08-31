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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.inspection
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class InteractiveSelectionResult(Enum):
    """
    Enum Class


    See Also:
        `API InteractiveSelectionResult <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1inspection.html#a2c7cbb6dbe76b989188c75ba8e400876>`_
    """
    __ooo_ns__: str = "com.sun.star.inspection"
    __ooo_full_ns__: str = "com.sun.star.inspection.InteractiveSelectionResult"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.inspection.InteractiveSelectionResult"

    Cancelled = "Cancelled"
    """
    The interactive selection of a property value was canceled.
    """
    ObtainedValue = "ObtainedValue"
    """
    The interactive selection of a property value succeeded, a new property value has been obtained, but not yet set at the inspected component.
    
    In this case, the obtained value is passed to the caller of XPropertyHandler.onInteractivePropertySelection(), which is responsible for forwarding this value to the inspected component.
    """
    Pending = "Pending"
    """
    The interactive selection of a property value is still pending.
    
    This is usually used when this selection involves non-modal user interface.
    """
    Success = "Success"
    """
    The interactive selection of a property value succeeded, and the new property value chosen by the user has already been set at the inspected component.
    """

__all__ = ["InteractiveSelectionResult"]

