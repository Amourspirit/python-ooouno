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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.xsd
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.xsd import DataTypeClass as DataTypeClass
else:
    from ...lo.xsd.data_type_class import DataTypeClass as DataTypeClass


class DataTypeClassEnum(IntEnum):
    """
    Enum of Const Class DataTypeClass

    These constants specify the class used of an XDataType.
    """
    STRING = DataTypeClass.STRING
    """
    specifies an XSD compliant string type
    """
    BOOLEAN = DataTypeClass.BOOLEAN
    """
    specifies an XSD compliant boolean type
    """
    DECIMAL = DataTypeClass.DECIMAL
    """
    specifies an XSD compliant decimal type
    """
    FLOAT = DataTypeClass.FLOAT
    """
    specifies an XSD compliant float type
    """
    DOUBLE = DataTypeClass.DOUBLE
    """
    specifies an XSD compliant double type
    """
    DURATION = DataTypeClass.DURATION
    """
    specifies an XSD compliant duration type
    """
    DATETIME = DataTypeClass.DATETIME
    """
    specifies an XSD compliant datetime type
    """
    TIME = DataTypeClass.TIME
    """
    specifies an XSD compliant time type
    """
    DATE = DataTypeClass.DATE
    """
    specifies an XSD compliant date type
    """
    gYearMonth = DataTypeClass.gYearMonth
    """
    specifies an XSD compliant gYearMonth type
    """
    gYear = DataTypeClass.gYear
    """
    specifies an XSD compliant gYear type
    """
    gMonthDay = DataTypeClass.gMonthDay
    """
    specifies an XSD compliant gMonthDay type
    """
    gDay = DataTypeClass.gDay
    """
    specifies an XSD compliant gDay type
    """
    gMonth = DataTypeClass.gMonth
    """
    specifies an XSD compliant gMonth type
    """
    hexBinary = DataTypeClass.hexBinary
    """
    specifies an XSD compliant hexBinary type
    """
    base64Binary = DataTypeClass.base64Binary
    """
    specifies an XSD compliant base64Binary type
    """
    anyURI = DataTypeClass.anyURI
    """
    specifies an XSD compliant anyURI type
    """
    QName = DataTypeClass.QName
    """
    specifies an XSD compliant QName type
    """
    NOTATION = DataTypeClass.NOTATION
    """
    specifies an XSD compliant NOTATION type
    """

__all__ = ['DataTypeClass', 'DataTypeClassEnum']