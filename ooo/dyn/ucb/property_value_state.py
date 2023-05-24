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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class PropertyValueState(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.PropertyValueState", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.PropertyValueState`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.ucb.PropertyValueState import INVALID_NAME as PROPERTY_VALUE_STATE_INVALID_NAME
        from com.sun.star.ucb.PropertyValueState import INVALID_TYPE as PROPERTY_VALUE_STATE_INVALID_TYPE
        from com.sun.star.ucb.PropertyValueState import PROCESSED as PROPERTY_VALUE_STATE_PROCESSED
        from com.sun.star.ucb.PropertyValueState import UNPROCESSED as PROPERTY_VALUE_STATE_UNPROCESSED

        class PropertyValueState(uno.Enum):
            """
            Enum Class


            See Also:
                `API PropertyValueState <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#a82ef3fdcd414866879e7aae1e52748d0>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.ucb.PropertyValueState', value)

            __ooo_ns__: str = 'com.sun.star.ucb'
            __ooo_full_ns__: str = 'com.sun.star.ucb.PropertyValueState'
            __ooo_type_name__: str = 'enum'

            INVALID_NAME = PROPERTY_VALUE_STATE_INVALID_NAME
            """
            The given property name/handle is invalid.
            """
            INVALID_TYPE = PROPERTY_VALUE_STATE_INVALID_TYPE
            """
            The given property type is invalid.
            """
            PROCESSED = PROPERTY_VALUE_STATE_PROCESSED
            """
            The value was obtained.
            """
            UNPROCESSED = PROPERTY_VALUE_STATE_UNPROCESSED
            """
            The property value was not obtained yet.
            """
    else:
        # keep document generators happy
        from ...lo.ucb.property_value_state import PropertyValueState as PropertyValueState


__all__ = ['PropertyValueState']
