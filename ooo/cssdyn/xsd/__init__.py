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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.xsd.boolean import Boolean as Boolean
with suppress(ImportError):
    from ...dyn.xsd.data_type_class import DataTypeClass as DataTypeClass
with suppress(ImportError):
    from ...dyn.xsd.data_type_class import DataTypeClassEnum as DataTypeClassEnum
with suppress(ImportError):
    from ...dyn.xsd.date import Date as Date
with suppress(ImportError):
    from ...dyn.xsd.date_time import DateTime as DateTime
with suppress(ImportError):
    from ...dyn.xsd.day import Day as Day
with suppress(ImportError):
    from ...dyn.xsd.decimal import Decimal as Decimal
with suppress(ImportError):
    from ...dyn.xsd.month import Month as Month
with suppress(ImportError):
    from ...dyn.xsd.string import String as String
with suppress(ImportError):
    from ...dyn.xsd.time import Time as Time
with suppress(ImportError):
    from ...dyn.xsd.white_space_treatment import WhiteSpaceTreatment as WhiteSpaceTreatment
with suppress(ImportError):
    from ...dyn.xsd.white_space_treatment import WhiteSpaceTreatmentEnum as WhiteSpaceTreatmentEnum
with suppress(ImportError):
    from ...dyn.xsd.x_data_type import XDataType as XDataType
with suppress(ImportError):
    from ...dyn.xsd.year import Year as Year
