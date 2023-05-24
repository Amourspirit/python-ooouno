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
from typing import cast, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from com.sun.star.sheet.FillMode import FillModeProto

class FillMode(Enum):
    """
    Enum Class


    See Also:
        `API FillMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a75a9acd74effffae38daed55136b0980>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FillMode'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.sheet.FillMode'

    AUTO = cast("FillModeProto", 'AUTO')
    """
    specifies the use of a user-defined list.
    
    function is determined automatically.
    """
    DATE = cast("FillModeProto", 'DATE')
    """
    specifies an arithmetic series for date values.
    
    any date value matching the specified condition is valid.
    """
    GROWTH = cast("FillModeProto", 'GROWTH')
    """
    specifies a geometric series.
    """
    LINEAR = cast("FillModeProto", 'LINEAR')
    """
    specifies an arithmetic series.
    """
    SIMPLE = cast("FillModeProto", 'SIMPLE')
    """
    specifies a constant series.
    """

__all__ = ['FillMode']

