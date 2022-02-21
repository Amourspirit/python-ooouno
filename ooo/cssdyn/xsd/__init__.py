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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ...dyn.xsd.boolean import Boolean as Boolean
except ImportError:
    pass
try:
    from ...dyn.xsd.data_type_class import DataTypeClass as DataTypeClass
except ImportError:
    pass
try:
    from ...dyn.xsd.data_type_class import DataTypeClassEnum as DataTypeClassEnum
except ImportError:
    pass
try:
    from ...dyn.xsd.date import Date as Date
except ImportError:
    pass
try:
    from ...dyn.xsd.date_time import DateTime as DateTime
except ImportError:
    pass
try:
    from ...dyn.xsd.day import Day as Day
except ImportError:
    pass
try:
    from ...dyn.xsd.decimal import Decimal as Decimal
except ImportError:
    pass
try:
    from ...dyn.xsd.month import Month as Month
except ImportError:
    pass
try:
    from ...dyn.xsd.string import String as String
except ImportError:
    pass
try:
    from ...dyn.xsd.time import Time as Time
except ImportError:
    pass
try:
    from ...dyn.xsd.white_space_treatment import WhiteSpaceTreatment as WhiteSpaceTreatment
except ImportError:
    pass
try:
    from ...dyn.xsd.white_space_treatment import WhiteSpaceTreatmentEnum as WhiteSpaceTreatmentEnum
except ImportError:
    pass
try:
    from ...dyn.xsd.x_data_type import XDataType as XDataType
except ImportError:
    pass
try:
    from ...dyn.xsd.year import Year as Year
except ImportError:
    pass
