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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.report.calculation import Calculation as Calculation
with suppress(ImportError):
    from ...dyn.report.calculation import CalculationEnum as CalculationEnum
with suppress(ImportError):
    from ...dyn.report.fixed_line import FixedLine as FixedLine
with suppress(ImportError):
    from ...dyn.report.fixed_text import FixedText as FixedText
with suppress(ImportError):
    from ...dyn.report.force_new_page import ForceNewPage as ForceNewPage
with suppress(ImportError):
    from ...dyn.report.force_new_page import ForceNewPageEnum as ForceNewPageEnum
with suppress(ImportError):
    from ...dyn.report.format_condition import FormatCondition as FormatCondition
with suppress(ImportError):
    from ...dyn.report.formatted_field import FormattedField as FormattedField
with suppress(ImportError):
    from ...dyn.report.function import Function as Function
with suppress(ImportError):
    from ...dyn.report.group import Group as Group
with suppress(ImportError):
    from ...dyn.report.group_keep_together import GroupKeepTogether as GroupKeepTogether
with suppress(ImportError):
    from ...dyn.report.group_keep_together import GroupKeepTogetherEnum as GroupKeepTogetherEnum
with suppress(ImportError):
    from ...dyn.report.group_on import GroupOn as GroupOn
with suppress(ImportError):
    from ...dyn.report.group_on import GroupOnEnum as GroupOnEnum
with suppress(ImportError):
    from ...dyn.report.groups import Groups as Groups
with suppress(ImportError):
    from ...dyn.report.image_control import ImageControl as ImageControl
with suppress(ImportError):
    from ...dyn.report.keep_together import KeepTogether as KeepTogether
with suppress(ImportError):
    from ...dyn.report.keep_together import KeepTogetherEnum as KeepTogetherEnum
with suppress(ImportError):
    from ...dyn.report.report_control_format import ReportControlFormat as ReportControlFormat
with suppress(ImportError):
    from ...dyn.report.report_control_model import ReportControlModel as ReportControlModel
with suppress(ImportError):
    from ...dyn.report.report_definition import ReportDefinition as ReportDefinition
with suppress(ImportError):
    from ...dyn.report.report_engine import ReportEngine as ReportEngine
with suppress(ImportError):
    from ...dyn.report.report_print_option import ReportPrintOption as ReportPrintOption
with suppress(ImportError):
    from ...dyn.report.report_print_option import ReportPrintOptionEnum as ReportPrintOptionEnum
with suppress(ImportError):
    from ...dyn.report.section import Section as Section
with suppress(ImportError):
    from ...dyn.report.section_page_break import SectionPageBreak as SectionPageBreak
with suppress(ImportError):
    from ...dyn.report.section_page_break import SectionPageBreakEnum as SectionPageBreakEnum
with suppress(ImportError):
    from ...dyn.report.shape import Shape as Shape
with suppress(ImportError):
    from ...dyn.report.x_fixed_line import XFixedLine as XFixedLine
with suppress(ImportError):
    from ...dyn.report.x_fixed_text import XFixedText as XFixedText
with suppress(ImportError):
    from ...dyn.report.x_format_condition import XFormatCondition as XFormatCondition
with suppress(ImportError):
    from ...dyn.report.x_formatted_field import XFormattedField as XFormattedField
with suppress(ImportError):
    from ...dyn.report.x_function import XFunction as XFunction
with suppress(ImportError):
    from ...dyn.report.x_functions import XFunctions as XFunctions
with suppress(ImportError):
    from ...dyn.report.x_functions_supplier import XFunctionsSupplier as XFunctionsSupplier
with suppress(ImportError):
    from ...dyn.report.x_group import XGroup as XGroup
with suppress(ImportError):
    from ...dyn.report.x_groups import XGroups as XGroups
with suppress(ImportError):
    from ...dyn.report.x_image_control import XImageControl as XImageControl
with suppress(ImportError):
    from ...dyn.report.x_report_component import XReportComponent as XReportComponent
with suppress(ImportError):
    from ...dyn.report.x_report_control_format import XReportControlFormat as XReportControlFormat
with suppress(ImportError):
    from ...dyn.report.x_report_control_model import XReportControlModel as XReportControlModel
with suppress(ImportError):
    from ...dyn.report.x_report_definition import XReportDefinition as XReportDefinition
with suppress(ImportError):
    from ...dyn.report.x_report_engine import XReportEngine as XReportEngine
with suppress(ImportError):
    from ...dyn.report.x_section import XSection as XSection
with suppress(ImportError):
    from ...dyn.report.x_shape import XShape as XShape
