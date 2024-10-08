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
# Namespace: com.sun.star.xml.dom.events
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class PhaseType(Enum):
    """
    Enum Class

    ENUM PhaseType

    See Also:
        `API PhaseType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1events.html#af00a42ecad444bbda75cde1b64bd7e72>`_
    """
    __ooo_ns__: str = "com.sun.star.xml.dom.events"
    __ooo_full_ns__: str = "com.sun.star.xml.dom.events.PhaseType"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.xml.dom.events.PhaseType"

    AT_TARGET = "AT_TARGET"
    """
    """
    BUBBLING_PHASE = "BUBBLING_PHASE"
    """
    """
    CAPTURING_PHASE = "CAPTURING_PHASE"
    """
    """

__all__ = ["PhaseType"]

