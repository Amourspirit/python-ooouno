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


class DataTypeClass(object):
    """
    Const Class

    These constants specify the class used of an XDataType.

    See Also:
        `API DataTypeClass <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xsd_1_1DataTypeClass.html>`_
    """
    STRING = 1
    """
    specifies an XSD compliant string type
    """
    BOOLEAN = 2
    """
    specifies an XSD compliant boolean type
    """
    DECIMAL = 3
    """
    specifies an XSD compliant decimal type
    """
    FLOAT = 4
    """
    specifies an XSD compliant float type
    """
    DOUBLE = 5
    """
    specifies an XSD compliant double type
    """
    DURATION = 6
    """
    specifies an XSD compliant duration type
    """
    DATETIME = 7
    """
    specifies an XSD compliant datetime type
    """
    TIME = 8
    """
    specifies an XSD compliant time type
    """
    DATE = 9
    """
    specifies an XSD compliant date type
    """
    gYearMonth = 10
    """
    specifies an XSD compliant gYearMonth type
    """
    gYear = 11
    """
    specifies an XSD compliant gYear type
    """
    gMonthDay = 12
    """
    specifies an XSD compliant gMonthDay type
    """
    gDay = 13
    """
    specifies an XSD compliant gDay type
    """
    gMonth = 14
    """
    specifies an XSD compliant gMonth type
    """
    hexBinary = 15
    """
    specifies an XSD compliant hexBinary type
    """
    base64Binary = 16
    """
    specifies an XSD compliant base64Binary type
    """
    anyURI = 17
    """
    specifies an XSD compliant anyURI type
    """
    QName = 18
    """
    specifies an XSD compliant QName type
    """
    NOTATION = 19
    """
    specifies an XSD compliant NOTATION type
    """


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
