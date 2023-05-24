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
    from com.sun.star.sheet.GeneralFunction import GeneralFunctionProto

class GeneralFunction(Enum):
    """
    Enum Class


    See Also:
        `API GeneralFunction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#ad184d5bd9055f3b4fd57ce72c781758d>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.GeneralFunction'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.sheet.GeneralFunction'

    AUTO = cast("GeneralFunctionProto", 'AUTO')
    """
    specifies the use of a user-defined list.
    
    function is determined automatically.
    """
    AVERAGE = cast("GeneralFunctionProto", 'AVERAGE')
    """
    average of all numerical values is calculated.
    """
    COUNT = cast("GeneralFunctionProto", 'COUNT')
    """
    all values, including non-numerical values, are counted.
    """
    COUNTNUMS = cast("GeneralFunctionProto", 'COUNTNUMS')
    """
    numerical values are counted.
    """
    MAX = cast("GeneralFunctionProto", 'MAX')
    """
    maximum value of all numerical values is calculated.
    """
    MIN = cast("GeneralFunctionProto", 'MIN')
    """
    minimum value of all numerical values is calculated.
    """
    NONE = cast("GeneralFunctionProto", 'NONE')
    """
    no cells are moved.
    
    sheet is not linked.
    
    new values are used without changes.
    
    nothing is calculated.
    
    nothing is imported.
    
    no condition is specified.
    """
    PRODUCT = cast("GeneralFunctionProto", 'PRODUCT')
    """
    product of all numerical values is calculated.
    """
    STDEV = cast("GeneralFunctionProto", 'STDEV')
    """
    standard deviation is calculated based on a sample.
    """
    STDEVP = cast("GeneralFunctionProto", 'STDEVP')
    """
    standard deviation is calculated based on the entire population.
    """
    SUM = cast("GeneralFunctionProto", 'SUM')
    """
    sum of all numerical values is calculated.
    """
    VAR = cast("GeneralFunctionProto", 'VAR')
    """
    variance is calculated based on a sample.
    """
    VARP = cast("GeneralFunctionProto", 'VARP')
    """
    variance is calculated based on the entire population.
    """

__all__ = ['GeneralFunction']

